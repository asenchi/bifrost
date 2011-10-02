import os
import sys

from setuptools import setup, find_packages, Command

VERSION = __import__("bifrost").__version__

install_requires = []
try:
    import importlib
except ImportError:
    install_requires.append("importlib")
install_requires.extend([
    'tnetstring==0.2.0',
    'pyzmq==2.1.7',
])

is_cpy = sys.version_info
is_pypy = hasattr(sys, "pypy_version_info")

# At some point we may support pypy using redis rather than 0mq.
if is_pypy:
    raise Exception("bifrost doesn't currently work with PyPy.")

setup(
    name="bifrost",
    version=VERSION,
    description="Gossip protocol layer.",
    license="MIT",
    url="https://github.com/asenchi/bifrost",
    author="Curt Micol",
    author_email="asenchi@asenchi.com",
    zip_safe=False,
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Topic :: Software Development :: Libraries :: Application Frameworks",
      "Programming Language :: Python :: 2.6",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: 3",
    ],
    test_suite="tests",
)
