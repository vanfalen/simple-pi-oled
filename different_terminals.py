from demo_opts import get_device
from luma.core.virtual import terminal
from PIL import ImageFont
from pathlib import Path
def make_font(name, size):
    font_path = str(Path(__file__).resolve().parent.joinpath('fonts', name))
    return ImageFont.truetype(font_path, size)

