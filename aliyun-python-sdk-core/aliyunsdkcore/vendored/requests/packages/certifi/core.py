#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.

Vendored from certifi 2026.07.22. The where() implementation keeps using
__file__ so the CA bundle resolves correctly under the nested
aliyunsdkcore.vendored.requests.packages.certifi package path
(importlib.resources with package name "certifi" would not work here).
"""
import os
import warnings


class DeprecatedBundleWarning(DeprecationWarning):
    """
    The weak security bundle is being deprecated. Please bother your service
    provider to get them to stop using cross-signed roots.
    """


def where():
    f = os.path.dirname(__file__)

    return os.path.join(f, 'cacert.pem')


def old_where():
    warnings.warn(
        "The weak security bundle has been removed. certifi.old_where() is now an alias "
        "of certifi.where(). Please update your code to use certifi.where() instead. "
        "certifi.old_where() will be removed in 2018.",
        DeprecatedBundleWarning
    )
    return where()
