#!/usr/bin/env python

from distutils.core import setup

setup(name              = "python-tropo-webapi",
      version           = "0.1.0",
      url               = "http://github.com/tropo/python-webapi",
      maintainer        = "Voxeo",
      maintainer_email  = "support@tropo.com",
      long_description  = "Python Tropo WebAPI implementation",
      platforms         = ["Platform Independent"],
      classifiers       = [
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      py_modules = ['tropo'],
)

