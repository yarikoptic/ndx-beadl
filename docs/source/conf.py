# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ndx-beadl'
copyright = '2021, Ryan Ly'
author = 'Ryan Ly'

# The short X.Y version
version = '0.1.0'

# The full version, including alpha/beta/rc tags
release = 'alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

############################################################################
#  CUSTOM CONFIGURATIONS ADDED BY THE NWB TOOL FOR GENERATING FORMAT DOCS
###########################################################################

import sphinx_rtd_theme  # noqa: E402
import textwrap  # noqa: E402

# -- Options for intersphinx  ---------------------------------------------
intersphinx_mapping.update({
    'core': ('https://nwb-schema.readthedocs.io/en/latest/', None),
    'hdmf-common': ('https://hdmf-common-schema.readthedocs.io/en/latest/', None),
})

# -- Generate sources from YAML---------------------------------------------------
# Always rebuild the source docs from YAML even if the folder with the source files already exists
spec_doc_rebuild_always = True


def run_doc_autogen(_):
    # Execute the autogeneration of Sphinx format docs from the YAML sources
    import sys
    import os
    conf_file_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(conf_file_dir)  # Need so that generate format docs can find the conf_doc_autogen file
    from conf_doc_autogen import spec_output_dir

    if spec_doc_rebuild_always or not os.path.exists(spec_output_dir):
        sys.path.append('./docs')  # needed to enable import of generate_format docs
        from hdmf_docutils.generate_format_docs import main as generate_docs
        generate_docs()


def setup(app):
    app.connect('builder-inited', run_doc_autogen)
    # overrides for wide tables in RTD theme
    try:
        app.add_css_file("theme_overrides.css")  # Used by newer Sphinx versions
    except AttributeError:
        app.add_stylesheet("theme_overrides.css")  # Used by older version of Sphinx

# -- Customize sphinx settings
numfig = True
autoclass_content = 'both'
autodoc_docstring_signature = True
autodoc_member_order = 'bysource'
add_function_parentheses = False


# -- HTML sphinx options
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# LaTeX Sphinx options
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': textwrap.dedent(
        '''
        \\setcounter{tocdepth}{3}
        \\setcounter{secnumdepth}{6}
        \\usepackage{enumitem}
        \\setlistdepth{100}
        '''),
}
