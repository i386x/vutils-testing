#
# File:    ./docs/conf.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2024-11-03 12:20:12 +0100
# Project: vutils-testing: Auxiliary library for writing tests
#
# SPDX-License-Identifier: MIT
#
"""Configuration for Sphinx documentation builder."""

import sys

sys.path.insert(0, "../src")


project = "vutils-testing"
author = "Jiří Kučera"
copyright = "2021-%Y, Jiří Kučera"
version = "2.0"
release = "2.0.3"

needs_sphinx = "8.1"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxext.abcdoc",
]
manpages_url = (
    "https://man7.org/linux/man-pages/"
    "man{section}/{page}.{section}.html"
)
today = ""
today_fmt = "%Y-%m-%d"

numfig = True
numfig_format = {
    "code-block": "Listing %s",
    "figure": "Figure %s",
    "section": "Section",
    "table": "Table %s",
}
numfig_secnum_depth = 0

highlight_language = "python"
highlight_options = {}
pygments_style = "sphinx"

language = "en"

default_role = None
keep_warnings = False
option_emphasize_placeholders = True
primary_domain = "py"
rst_epilog = ""
rst_prolog = ""
show_authors = False
trim_footnote_reference_space = False

math_eqref_format = "({number})"
math_number_all = False
math_numfig = True
math_numsep = "."

nitpicky = True
nitpick_ignore = ()
nitpick_ignore_regex = ()

add_function_parentheses = True
maximum_signature_line_length = 79
strip_signature_backslash = True
toc_object_entries = True
toc_object_entries_show_parents = "domain"

exclude_patterns = ["build"]
include_patterns = ["**"]
root_doc = "index"
source_encoding = "utf-8-sig"
source_suffix = {".rst": "restructuredtext"}

smartquotes = True
smartquotes_action = "qBDew"
smartquotes_excludes = {
    "languages": ["ja"],
    "builders": ["man", "text"],
}

template_bridge = ""
templates_path = []

show_warning_types = True
suppress_warnings = []

html_theme = "renku"
# html_theme_options = {}
# html_theme_path = []
# html_style = ["classic.css"]
html_title = f"{project} {release} Documentation"
html_short_title = f"{project} {release} documentation"
html_baseurl = ""
html_codeblock_linenos_style = "inline"
html_context = {}
html_logo = ""
html_favicon = ""
html_css_files = []
html_js_files = []
html_static_path = []
html_extra_path = []
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S %z"
html_last_updated_use_utc = False
html_permalinks = True
html_permalinks_icon = "¶"
# html_sidebars = {}
html_additional_pages = {}
html_domain_indices = True
html_use_index = True
html_split_index = False
html_copy_source = True
html_show_sourcelink = True
html_sourcelink_suffix = ".txt"
html_use_opensearch = ""
html_file_suffix = ".html"
html_link_suffix = html_file_suffix
html_show_copyright = True
html_show_search_summary = True
html_show_sphinx = True
html_output_encoding = "utf-8"
html_compact_lists = True
html_secnumber_suffix = " "
html_search_language = language
html_search_options = {}
html_search_scorer = ""
html_scaled_image_link = True
html_math_renderer = "mathjax"

text_add_secnumbers = True
text_newlines = "unix"
text_secnumber_suffix = " "
text_sectionchars = '*=-~"+`'

man_pages = [
    (root_doc, project, "Auxiliary library for writing tests", author, "3"),
]
man_show_urls = False
man_make_section_directory = True

linkcheck_allowed_redirects = {}
linkcheck_anchors = True
linkcheck_anchors_ignore = ["^!"]
linkcheck_anchors_ignore_for_url = ()
linkcheck_exclude_documents = []
linkcheck_ignore = []

linkcheck_auth = []
linkcheck_allow_unauthorized = False
linkcheck_rate_limit_timeout = 300
linkcheck_report_timeouts_as_broken = True
linkcheck_request_headers = {}
linkcheck_retries = 1
linkcheck_timeout = 30
linkcheck_workers = 5

c_extra_keywords = [
    "alignas",
    "alignof",
    "bool",
    "complex",
    "imaginary",
    "noreturn",
    "static_assert",
    "thread_local",
]
c_id_attributes = ()
c_maximum_signature_line_length = maximum_signature_line_length
c_paren_attributes = ()

cpp_id_attributes = ()
cpp_index_common_prefix = []
cpp_maximum_signature_line_length = maximum_signature_line_length
cpp_paren_attributes = ()

javascript_maximum_signature_line_length = maximum_signature_line_length

add_module_names = True
modindex_common_prefix = []
python_display_short_literal_types = True
python_maximum_signature_line_length = maximum_signature_line_length
python_use_unqualified_type_names = False
trim_doctest_flags = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
