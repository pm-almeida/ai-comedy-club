from setuptools import setup, find_packages

setup(
    name="ComedyClubChallenge",
    version="0.1",
    packages=find_packages(),

    install_requires=[
        "fastapi",
        "uvicorn",
        "transformers>=4.0",
        "textblob>=0.15.3",
        "torch>=1.8.1",
        "pytest>=6.2.2",
        "openai>=0.27.8",
        "mock>=5.0.2",
        "python-dotenv>=1.0.0",
        "gpt-2-simple",
        "alt-profanity-check>=1.2.2",
        "sentencepiece=0.1.99",
        "datasets=2.13.1",
        "accelerate=0.20.3",
        "scikit-learn=1.2.2",
    ],
    author="Konfuzio",
    description="A challenge for Python developers to create AI agents that tell and rate jokes.",
    license="MIT",
)
