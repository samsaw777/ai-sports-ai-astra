# Packages setup file

from setuptools import setup, find_packages

setup(
    name= "ai-wizard-system",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "uvicorn",
        "python-multipart",
        "pydantic",
        "pydantic-settings",
        "openai",
        "fastapi[standard]",
        "python-jose[cryptography]",
        "aiohttp",
        "python-dotenv",
    ],
    python_requires=">=3.8",
)