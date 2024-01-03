import setuptools
from setuptools import find_packages
from sunbraid._version import __version__

if __name__ == "__main__":
    setuptools.setup(
        name='sunbraid',  # Replace with your package's name
        author='Estevão Uyrá',
        author_email='estevao.uyra.pv@gmail.com',
        version=__version__,
        packages=find_packages(include=['sunbraid']),   
        package_data={
        "sunbraid": ["static.json"],
    }
)
