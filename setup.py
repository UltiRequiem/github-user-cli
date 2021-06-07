from setuptools import setup
from distutils.core import setup
from githubapi2.version import __version__

setup(
    name="githubapi2",
    version=__version__,
    python_requires=">=3.6",
    description="A wrapper for the GitHub Api.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="UltiRequiem",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/githubapi2",
    license="MIT",
    packages=["githubapi2"],
    install_requires=["requests==2.25.1"],
    entry_points={"console_scripts": ["github_user = githubapi2.githubuser:run"]},
    classifiers=[
        "Programming Language :: Python",
    ],
)
