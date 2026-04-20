# AI Image Compression Tool

This repository provides an AI-powered image compression tool that uses state-of-the-art deep learning techniques to reduce image file sizes without a significant loss in quality.

## Features
- Compress JPEG, PNG, and BMP images
- Utilize a pre-trained AI model for efficient compression
- Easy-to-use CLI interface

## Requirements
- Python >= 3.7
- Pillow library
- TensorFlow library

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py --input example.jpg --output compressed.jpg --quality 80
```
Arguments:
- `--input`: Path to the input image file
- `--output`: Path to the output compressed image
- `--quality`: Image quality level after compression (1-100, optional, default is 80)

## License
MIT License