from io import BytesIO
from pathlib import Path

from django.conf import settings
from PIL import Image, ImageDraw, ImageFont


def draw_to_image(shirt_color, text, fill, font):
    pre_image_path = Path(settings.MEDIA_ROOT / "pre" / f"{shirt_color}.png")
    font_path = Path(settings.MEDIA_ROOT / "fonts" / f"{font}.ttf")
    image = Image.open(pre_image_path)
    draw_coordinates = (image.width * 0.3, image.height / 2)
    drawer = ImageDraw.Draw(image)
    drawer.text(
        draw_coordinates,
        text=text,
        fill=f"#{fill}",
        font=ImageFont.truetype(font_path, size=24),
    )

    blob = BytesIO()
    image.save(blob, format="PNG")
    return blob
