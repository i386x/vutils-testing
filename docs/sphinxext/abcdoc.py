#
# File:    ./docs/sphinxext/abcdoc.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2024-11-03 21:57:52 +0100
# Project: abcdoc: Documentation tools
#
# SPDX-License-Identifier: MIT
#
"""``abcdoc`` Sphinx extension."""

from sphinx.writers.html5 import HTML5Translator


class HtmlTranslator(HTML5Translator):
    """Tweak Sphinx HTML translator."""

    __slots__ = ("__indent")

    def __init__(self, document, builder):
        """Initialize the HTML translator."""
        super().__init__(document, builder)
        self.__indent = 0

    def dispatch_visit(self, node):
        """Dispatch the node visit."""
        for nodecls in node.__class__.__mro__:
            method = getattr(self, f"visit_{nodecls.__name__}", None)
            if method is not None:
                indent = "  " * self.__indent
                print(f"{indent}Visiting {node}")
                method(node)
                self.__indent += 1
                break
        else:
            super().dispatch_visit(node)

    def dispatch_departure(self, node):
        """Dispatch the node departure."""
        for nodecls in node.__class__.__mro__:
            method = getattr(self, f"depart_{nodecls.__name__}", None)
            if method is not None:
                self.__indent -= 1
                indent = "  " * self.__indent
                print(f"{indent}Departing from {node}")
                method(node)
                break
        else:
            super().dispatch_departure(node)


def setup(app):
    """Setup the extension."""
    app.set_translator("html", HtmlTranslator, override=True)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": False,
    }
