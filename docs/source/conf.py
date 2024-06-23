# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

import tomli

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

_PATH_HERE = os.path.abspath(os.path.dirname(__file__))
_PATH_ROOT = os.path.realpath(os.path.join(_PATH_HERE, "..", ".."))
_PATH_PYPROJECT = os.path.join(_PATH_ROOT, "pyproject.toml")

# Read all metadata from pyproject.toml, so that we don't duplicate it.

with open(_PATH_PYPROJECT, mode="rb") as fp:
    pyproject_config = tomli.load(fp)

authors = pyproject_config["project"]["authors"]
author_names = [author["name"] for author in authors]
author_name_emails = [f"{author['name']} <{author['email']}>" for author in authors]

project = pyproject_config["project"]["name"]
copyright = "2024, " + ", ".join(author_names)
author = ", ".join(author_name_emails)
release = pyproject_config["project"]["version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
    "myst_parser",  # Enables markdown support
    "sphinx_design",  # Enables side to side cards
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

autodoc_member_order = "bysource"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}

html_favicon = "icons/favicon.ico"
html_theme_options = {
    "light_logo": "logo-light-mode.png",
    "dark_logo": "logo-dark-mode.png",
    "dark_css_variables": {
        "color-problematic": "#eeeeee",  # class names
    },
    "light_css_variables": {
        "color-problematic": "#000000",  # class names
    },
    "sidebar_hide_name": True,
}
