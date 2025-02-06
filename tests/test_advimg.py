import unittest
import sys
import os
import numpy as np

# Ensure the test script finds advimg properly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from advimg import advimg
from cryptography.fernet import Fernet

class TestAdvImg(unittest.TestCase):
    def setUp(self):
        self.image_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        self.key = advimg.generate_key()

    def test_compress_decompress_image(self):
        compressed = advimg.compress_image(self.image_array)
        decompressed = advimg.decompress_image(compressed)
        self.assertEqual(self.image_array.shape, decompressed.shape)

    def test_encrypt_decrypt_image(self):
        encrypted = advimg.encrypt_image(self.image_array, self.key)
        decrypted = advimg.decrypt_image(encrypted, self.key)
        self.assertEqual(self.image_array.shape, decrypted.shape)

    def test_hide_extract_data(self):
        secret = "Brewlock"
        modified_image = advimg.hide_data_in_image(self.image_array, secret)
        extracted = advimg.extract_data_from_image(modified_image, len(secret))
        self.assertEqual(secret, extracted)

if __name__ == "__main__":
    unittest.main()
