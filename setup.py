from setuptools import setup, find_packages

setup(
    name="VietnamLeadExtractor",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "transformers",
        "torch",
        "click",
        "requests",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "vle=main:cli",
        ],
    },
)
