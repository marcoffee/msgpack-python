#!/usr/bin/env python
import os
import sys

from Cython.Build import cythonize
from setuptools import Extension, setup

PYPY = hasattr(sys, "pypy_version_info")

libraries = []
macros = []
ext_modules = []

if sys.platform == "win32":
    libraries.append("ws2_32")
    macros = [("__LITTLE_ENDIAN__", "1")]

if not PYPY and not os.environ.get("MSGPACK_PUREPYTHON"):
    ext_modules.append(
        Extension(
            "msgpack._cmsgpack",
            sources=["msgpack/_cmsgpack.pyx"],
            libraries=libraries,
            include_dirs=["."],
            define_macros=macros,
        )
    )

    ext_modules = cythonize(ext_modules)

del libraries, macros

setup(
    ext_modules=ext_modules,
    packages=["msgpack"],
)
