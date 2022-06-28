"""
bilby_pipe
==========

bilby_pipe is a python3 tool for automating the process of running `bilby
<https://git.ligo.org/lscsoft/bilby>`_ for gravitational parameter
estimation on computing clusters.

"""

from . import bilbyargparser, main, parser, utils

__short_version__ = utils.get_version_information().split(":", 1)[0]
__long_version__ = utils.get_version_information()

from . import _version

__version__ = _version.get_versions()["version"]
