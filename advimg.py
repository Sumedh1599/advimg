import cv2
import numpy as np
import os
import base64
import threading
from cryptography.fernet import Fernet
from PIL import Image
import io

class advimg:
    """Advanced image processing with encryption, compression, and metadata control."""

    @staticmethod
    def load_image(image_path: str) -> np.ndarray:
        """Load an image from a file into a NumPy array."""
        return cv2.imread(image_path)

    @staticmethod
    def save_image(image_array: np.ndarray, save_path: str):
        """Save a NumPy array as an image file."""
        cv2.imwrite(save_path, image_array)

    @staticmethod
    def compress_image(image_array: np.ndarray, quality: int = 50) -> bytes:
        """Compress an image using JPEG encoding."""
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        _, buffer = cv2.imencode(".jpg", image_array, encode_param)
        return buffer.tobytes()

    @staticmethod
    def decompress_image(compressed_data: bytes) -> np.ndarray:
        """Decompress JPEG-compressed image data."""
        nparr = np.frombuffer(compressed_data, np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    @staticmethod
    def generate_key() -> str:
        """Generate a secure encryption key."""
        return Fernet.generate_key().decode()

    @staticmethod
    def encrypt_image(image_array: np.ndarray, key: str) -> bytes:
        """Encrypt an image using AES encryption."""
        cipher = Fernet(key.encode())
        _, buffer = cv2.imencode(".png", image_array)
        return cipher.encrypt(buffer.tobytes())

    @staticmethod
    def decrypt_image(encrypted_data: bytes, key: str) -> np.ndarray:
        """Decrypt an AES-encrypted image."""
        cipher = Fernet(key.encode())
        decrypted_bytes = cipher.decrypt(encrypted_data)
        nparr = np.frombuffer(decrypted_bytes, np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    @staticmethod
    def hide_data_in_image(image_array: np.ndarray, secret_data: str) -> np.ndarray:
        """Hide text data inside an image using steganography."""
        binary_secret = ''.join(format(ord(char), '08b') for char in secret_data)
        flat_image = image_array.flatten()
        for i in range(len(binary_secret)):
            flat_image[i] = (flat_image[i] & 0xFE) | int(binary_secret[i])
        return flat_image.reshape(image_array.shape)

    @staticmethod
    def extract_data_from_image(image_array: np.ndarray, data_length: int) -> str:
        """Extract hidden text data from an image."""
        flat_image = image_array.flatten()
        binary_data = ''.join(str(flat_image[i] & 1) for i in range(data_length * 8))
        return ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))

    @staticmethod
    def multi_threaded_compression(images: list) -> list:
        """Perform multi-threaded image compression."""
        results = []
        lock = threading.Lock()

        def worker(image):
            compressed_value = advimg.compress_image(image)
            with lock:
                results.append(compressed_value)

        threads = [threading.Thread(target=worker, args=(img,)) for img in images]
        for t in threads: t.start()
        for t in threads: t.join()

        return results

if __name__ == "__main__":
    image_path = "test.jpg"
    key = advimg.generate_key()

    image = advimg.load_image(image_path)
    compressed = advimg.compress_image(image)
    decompressed = advimg.decompress_image(compressed)

    encrypted = advimg.encrypt_image(image, key)
    decrypted = advimg.decrypt_image(encrypted, key)

    hidden_image = advimg.hide_data_in_image(image, "Hidden Message")
    extracted_data = advimg.extract_data_from_image(hidden_image, len("Hidden Message"))

    print("Encryption Successful:", encrypted[:10])
    print("Extracted Data:", extracted_data)
