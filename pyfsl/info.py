#! /usr/bin/env python
##########################################################################
# NSAp - Copyright (C) CEA, 2013
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# pyFsl current version
version_major = 1
version_minor = 0
version_micro = 0

# Expected by setup.py: string of form "X.Y.Z"
__version__ = "{0}.{1}.{2}".format(version_major, version_minor, version_micro)

# Define default FSL path for the package
DEFAULT_FSL_PATH = "/etc/fsl/5.0/fsl.sh"

# Define FreeSurfer supported version
FSL_RELEASE = "5.0.9"

# Expected by setup.py: the status of the project
CLASSIFIERS = ["Development Status :: 5 - Production/Stable",
               "Environment :: Console",
               "Environment :: X11 Applications :: Qt",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering",
               "Topic :: Utilities"]

# Project descriptions
description = """[pyFsl]
This package provides common scripts:

* pyfsl_bedpostx:
* pyfsl_:
"""
long_description = """
======================
pyFsl
======================

Python wrappers for FSL: wrap the FSL software and simplify
scripting calls. Such calls can be performed through the use of a
dedicated function of the package.
"""

# Main setup parameters
NAME = "pyFsl"
ORGANISATION = "CEA"
MAINTAINER = "Antoine Grigis"
MAINTAINER_EMAIL = "antoine.grigis@cea.fr"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/neurospin/pyfsl"
DOWNLOAD_URL = "https://github.com/neurospin/pyfsl"
LICENSE = "CeCILL-B"
CLASSIFIERS = CLASSIFIERS
AUTHOR = "pyFsl developers"
AUTHOR_EMAIL = "antoine.grigis@cea.fr"
PLATFORMS = "OS Independent"
ISRELEASE = True
VERSION = __version__
PROVIDES = ["pyfsl"]
REQUIRES = [
    "numpy>=1.6.1",
    "scipy>=0.9.0",
    "nibabel>=1.1.0"
]
EXTRA_REQUIRES = {}
