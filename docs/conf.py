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
version_file = os.path.join("..", 'src/version.py')
try:
    exec(open(version_file).read())
except IOError:
    print("Failed to load PyFlink Docs version file for packaging. " +
          "'%s' not found!" % version_file,
          file=sys.stderr)
    sys.exit(-1)
# The short X.Y version
version = __version__  # noqa
# The full version, including alpha/beta/rc tags
release = os.environ.get('RELEASE_VERSION', version)
html_show_copyright = False

html_title = project + ' version ' + version

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
""".format(
    os.environ.get("GIT_HASH", "main"),
    os.environ.get("GIT_HASH", "master"))

if 'html_theme' not in globals():
    try:
        import insipid_sphinx_theme
    except ImportError:
        pass
    else:
        html_theme = 'insipid'
        html_copy_source = False
        html_permalinks_icon = '#'
