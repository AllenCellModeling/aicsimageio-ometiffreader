#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aicsimageio_ometiffreader import ReaderMetadata


def test_load() -> None:
    ReaderMetadata.get_supported_extensions()
    ReaderMetadata.get_reader()


def test_str_len() -> None:
    assert True
