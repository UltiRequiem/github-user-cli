from setuptools import setup
from distutils.core import setup
from githubapi.version import __version__

setup(
    name="githubapi",
    version=__version__,
    python_requires=">=3.6",
    description="A wrapper for the GitHub Api.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="UltiRequiem",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/githubapi",
    license="MIT",
    packages=["githubapi"],
    install_requires=["requests==2.25.1"],
    entry_points={"console_scripts": ["githubapi = githubapi.githubapi:main"]},
    classifiers=[
        "Programming Language :: Python",
    ],
)
