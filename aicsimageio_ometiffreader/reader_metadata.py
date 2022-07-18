#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base_image_reader
from typing import List

###############################################################################


class ReaderMetadata(base_image_reader.ReaderMetadata):
    @staticmethod
    def get_supported_extensions() -> List[str]:
        return ["ome.tif", "ome.tiff"]

    @staticmethod
    def get_reader() -> base_image_reader.reader.Reader:
        from .ome_tiff_reader import OmeTiffReader

        return OmeTiffReader
