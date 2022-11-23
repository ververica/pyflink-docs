import os
import sys

extensions = [
    'nbsphinx',
    'sphinxcontrib.rsvgconverter',  # for SVG->PDF conversion in LaTeX output
    'sphinx_gallery.load_style',  # load CSS for gallery (needs SG >= 0.6)
    'sphinx_last_updated_by_git',  # get "last updated" from Git
    'sphinx_codeautolink',  # automatic links from code to documentation
    'sphinx.ext.intersphinx',  # links to other Sphinx projects (e.g. NumPy)
]

# These projects are also used for the sphinx_codeautolink extension:
intersphinx_mapping = {
    'IPython': ('https://ipython.readthedocs.io/en/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'python': ('https://docs.python.org/3/', None),
}

html_sourcelink_suffix = ''

mathjax3_config = {
    'tex': {'tags': 'ams', 'useLabelIds': True},
}

master_doc = 'index'

project = 'pyflink-docs'
author = 'PyFlink'
copyright = ''
flink_doc_version = "release-1.15"
release = 'release-1.15'
html_show_copyright = False

html_title = project + ' version ' + flink_doc_version

# Links used globally in the RST files.
# These are defined here to allow link substitutions dynamically.
rst_epilog = """
.. |binder| replace:: Live Notebook
.. _binder: https://mybinder.org/v2/gh/ververica/pyflink-docs/{0}?filepath=docs%2Fgetting_started%2Fquickstart%2Ftable_api.ipynb
.. |binder_table| replace:: Live Notebook: Table
.. _binder_table: https://mybinder.org/v2/gh/ververica/pyflink-docs/{0}?filepath=docs%2Fgetting_started%2Fquickstart%2Ftable_api.ipynb
.. |binder_datastream| replace:: Live Notebook: DataStream
.. _binder_datastream: https://mybinder.org/v2/gh/ververica/pyflink-docs/{0}?filepath=docs%2Fgetting_started%2Fquickstart%2Fdatastream_api.ipynb
.. |examples| replace:: Examples
.. _examples: https://github.com/apache/flink/tree/{1}/flink-python/pyflink/examples
.. role:: raw-html(raw)
   :format: html

.. |api_reference| replace:: :raw-html:`<meta http-equiv="refresh" content="0;URL='https://nightlies.apache.org/flink/flink-docs-{1}/api/python/index.html' " />`
""".format(
    os.environ.get("GIT_HASH", release),
    flink_doc_version)

html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']

html_theme_options = {
    "switcher": {
        "json_url": "https://pyflink.readthedocs.io/en/main/_static/switcher.json",
        "version_match": release,
    },
    "navbar_end": ["version-switcher"]
}
