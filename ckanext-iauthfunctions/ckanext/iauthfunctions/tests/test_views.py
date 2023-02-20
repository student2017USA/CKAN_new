"""Tests for views.py."""

import pytest

import ckanext.iauthfunctions.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "iauthfunctions")
@pytest.mark.usefixtures("with_plugins")
def test_iauthfunctions_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("iauthfunctions.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, iauthfunctions!"
