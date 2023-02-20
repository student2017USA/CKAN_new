"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.iauthfunctions.logic import validators


def test_iauthfunctions_reauired_with_valid_value():
    assert validators.iauthfunctions_required("value") == "value"


def test_iauthfunctions_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.iauthfunctions_required(None)
