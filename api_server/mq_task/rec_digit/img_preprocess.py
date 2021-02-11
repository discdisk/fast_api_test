import base64
import numpy as np
import io
from PIL import Image


def process(img_text: str) -> np.ndarray:
    img_bytes = base64.b64decode(img_text.split(',')[-1])
    pic = Image.open(io.BytesIO(img_bytes))

    pic = pic.convert('L').resize((28, 28))
    pic_M = np.array(pic)
    threshold, upper, lower = 150., 0., 1.0
    pic_M = np.where(pic_M > threshold, upper, lower)
    pic_M = np.array([[pic_M]], dtype=np.float32)
    return pic_M
