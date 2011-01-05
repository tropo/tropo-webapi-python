#!/usr/bin/env python

from distutils.core import setup

setup(name              = "tropo-webapi-python",
      version           = "0.1.0",
      url               = "http://github.com/tropo/tropo-webapi-python",
      author            = "Voxeo Corp.",
      author_email      = "support@tropo.com",
      description       = "Python library for building voice/SMS/IM/Twitter apps at Tropo.com",
      long_description  = "This module implements a set of classes and methods for manipulating the Web API for the Tropo cloud communications service at http://www.tropo.com/",
      platforms         = ["Platform Independent"],
      license           = "MIT",
      maintainer        = "Dan York",
      maintainer_email  = "dyork@voxeo.com",
      classifiers       = [
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      py_modules = ['tropo'],
)

