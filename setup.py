from setuptools import setup, find_packages

setup(
    name="diabetes_detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas==2.0.3",
        "scikit-learn==1.5.1",
        "flask==2.3.2",
        "numpy==1.24.3"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Flask app for diabetes prediction",
    python_requires=">=3.9"
)