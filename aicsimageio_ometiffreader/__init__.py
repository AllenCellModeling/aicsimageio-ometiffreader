# -*- coding: utf-8 -*-

"""Top-level package for aicsimageio_ometiffreader."""

__author__ = "Eva Maxfield Brown"
__email__ = "evamxfieldbrown@gmail.com"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "0.0.0"


def get_module_version() -> str:
    return __version__


from .reader_metadata import ReaderMetadata  # noqa: F401
