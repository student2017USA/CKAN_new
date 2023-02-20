"""Tests for helpers.py."""

import ckanext.iauthfunctions.helpers as helpers


def test_iauthfunctions_hello():
    assert helpers.iauthfunctions_hello() == "Hello, iauthfunctions!"
