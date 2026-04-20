import argparse
from PIL import Image
import tensorflow as tf
import numpy as np

def compress_image(input_path, output_path, quality):
    # Load image as a numpy array
    img = Image.open(input_path)
    img_array = np.asarray(img)

    # Placeholder dummy AI model for demonstration purposes
    # Replace this with a real pre-trained model for advanced compression
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=img_array.shape),
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
        tf.keras.layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')
    ])
    compressed_image = model.predict(img_array[None, ...])[0]

    # Convert back to PIL Image and save with given quality
    compressed_image = Image.fromarray((compressed_image * 255).astype(np.uint8))
    compressed_image.save(output_path, quality=quality)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI-powered image compression tool.")
    parser.add_argument('--input', type=str, required=True, help='Path to the input image file')
    parser.add_argument('--output', type=str, required=True, help='Path to save the compressed image')
    parser.add_argument('--quality', type=int, default=80, help='Quality of the compressed image (1-100)')
    
    args = parser.parse_args()

    compress_image(args.input, args.output, args.quality)