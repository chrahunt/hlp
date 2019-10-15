import io
import os

from setuptools import find_packages, setup


path = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(path, "README.md")
with io.open(readme_path, encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="hlp",
    version="0.2.1",
    author="Chris Hunt",
    author_email="chrahunt@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Documentation",
    ],
    description="Python help CLI",
    entry_points={"console_scripts": ["hlp = hlp.cli:main"]},
    keywords=["help", "cli", "command"],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=2.7",
    url="https://github.com/chrahunt/hlp",
)
