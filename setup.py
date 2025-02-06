from setuptools import setup, find_packages

setup(
    name="advimg",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["cryptography", "opencv-python", "numpy", "Pillow"],
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    description="Advanced image processing with encryption, compression, and steganography.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sumedh1599/advimg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
