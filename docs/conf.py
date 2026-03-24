import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

project = "opnsense-py"
author = "Justin Refi"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_theme = "sphinx_rtd_theme"
autodoc_member_order = "bysource"
