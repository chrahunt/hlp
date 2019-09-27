from setuptools import find_packages, setup


setup(
    name="hlp",
    version="0.1.0",
    entry_points={"console_scripts": ["hlp = hlp.cli:main"]},
    packages=find_packages(),
)
