from manimlib.imports import *
from PIL import Image
import numpy as np

class FourierImageRotation(Scene):
    """Display the Fourier transform of an image and rotate it."""

    def construct(self):
        image_path = "my_image.png"  # Change this to your PNG file

        # Load the image and convert to grayscale array
        img = Image.open(image_path).convert("L")
        arr = np.array(img)

        # Compute 2D Fourier transform and shift zero freq to center
        fft = np.fft.fftshift(np.fft.fft2(arr))
        magnitude = np.abs(fft)
        magnitude = np.log(magnitude + 1e-3)
        magnitude -= magnitude.min()
        magnitude /= magnitude.max()
        mag_image = (magnitude * 255).astype(np.uint8)
        mag_image = np.stack([mag_image]*3, axis=-1)

        # Create manim ImageMobjects
        original = ImageMobject(image_path)
        spectrum = ImageMobject(mag_image)

        original.scale_to_fit_height(3)
        spectrum.scale_to_fit_height(3)
        original.shift(LEFT*3)
        spectrum.shift(RIGHT*3)

        self.play(FadeIn(original))
        self.wait(1)
        self.play(FadeIn(spectrum))
        self.wait(1)
        self.play(Rotate(spectrum, TAU, rate_func=linear, run_time=4))
        self.wait(1)
