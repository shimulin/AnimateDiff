from setuptools import setup, find_packages

setup(
    name="animatediff",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # 列出專案所需的依賴項，例如：
        "torch==2.3.1",
        "torchvision==0.18.1",
        "diffusers==0.11.1",
        "transformers==4.25.1",
        "xformers==0.0.27",
        "imageio==2.27.0",
        "imageio-ffmpeg==0.4.9",
        "decord==0.6.0",
        "omegaconf==2.3.0",
        "gradio==3.36.1",
        "safetensors",
        "einops",
        "wandb"
    ],
)
