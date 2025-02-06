# advimg

`advimg` is an advanced image processing library that enhances traditional image handling with **AES encryption, Gzip compression, and steganography**.

## Features

- **Gzip compression for efficient image storage**
- **AES encryption for secure image storage**
- **Steganography (Hide messages inside images)**
- **Multi-threaded image compression**
- **Automatic key generation for encryption**

## Installation

```bash
pip install advimg

USAGE:
from advimg import advimg

image_path = "test.jpg"
key = advimg.generate_key()

image = advimg.load_image(image_path)
compressed = advimg.compress_image(image)
decompressed = advimg.decompress_image(compressed)

encrypted = advimg.encrypt_image(image, key)
decrypted = advimg.decrypt_image(encrypted, key)

hidden_image = advimg.hide_data_in_image(image, "Hidden Message")
extracted_data = advimg.extract_data_from_image(hidden_image, len("Hidden Message"))

print("Extracted Data:", extracted_data)
```
