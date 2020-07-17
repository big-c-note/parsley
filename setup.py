import setuptools
from typing import List
import glob

import parsley


def get_scripts_from_bin() -> List[str]:
    """Get all local scripts from bin so they are included in the package."""
    return glob.glob("bin/*")


def get_package_description() -> str:
    """Returns a description of this package from the markdown files."""
    with open("README.md", "r") as stream:
        readme: str = stream.read()
    return readme


setuptools.setup(
    name="parsley",
    version=parsley.__version__,
    author="Colin Manko",
    author_email="colin@colinmanko.com",
    description="Unsupervised semantic clustering made easy.",
    long_description=get_package_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/big-c-note/parsley",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    scripts=get_scripts_from_bin(),
    python_requires=">=3.7",
)
