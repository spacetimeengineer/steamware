from setuptools import setup, find_packages

setup(
    name="steamware",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A modular part family and hardware assembly language for 3D printing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/spacetimeengineer/STEAMWare",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "loguru",
    ],
    entry_points={
        "console_scripts": [
            "steamware=steamware:main",  # Replace `main` with the actual function in your script
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)