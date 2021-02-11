import numpy as np
import chainer
from chainer import ChainList
import chainer.functions as F
import chainer.links as L
from .img_preprocess import process
from pathlib import Path

# Network definition


class MLP(ChainList):

    def __init__(self, conv_layer=[], fully_connect_layer=[10, 2]):
        super(MLP, self).__init__()
        self.n1 = len(conv_layer)
        self.n2 = len(fully_connect_layer)
        with self.init_scope():
            for n in conv_layer:
                self.add_link(L.Convolution2D(
                    None, out_channels=n, ksize=(3, 3), stride=1))
            for n in fully_connect_layer:
                self.add_link(L.Linear(None, n))

    def __call__(self, x):
        out = x
        for i1 in range(self.n1):
            out = F.relu(self[i1](out))
            out = F.max_pooling_2d(out, 2)
        for i2 in range(self.n2):
            out = F.relu(self[i1+1+i2](out))
        return out


# load the classifier
file_name = Path(str(Path(__file__).parent.absolute()) +
                 '/Model_gpu_C16_f30_20_10')
model = MLP(conv_layer=[16], fully_connect_layer=[30, 20, 10])
chainer.serializers.load_npz(file_name, model)


def ocr(jpgtxt: str) -> int:
    data = process(jpgtxt)
    data = model(data).data
    return int(np.argmax(data))
