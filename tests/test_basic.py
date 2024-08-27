from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import pytest
from sphinx import version_info
from sphinx.testing.util import SphinxTestApp


@pytest.mark.parametrize(
    "builder", ["html", "singlehtml", "dirhtml", "latex", "text", "man", "epub"]
)
def test_build(builder: str, tmp_path: Path, make_app: type[SphinxTestApp]):
    """
    Tests a build via the Sphinx Build API.
    It looks like that there are scenarios where this specific build makes trouble but no others.
    """
    tmp_path.joinpath("conf.py").write_text(
        dedent("""\
        extensions = ["sphinx_data_viewer"]
        """),
        encoding="utf-8",
    )
    tmp_path.joinpath("test.json").write_text('{"a": [1, 2, 3]}', encoding="utf-8")
    tmp_path.joinpath("index.rst").write_text(
        dedent("""\
        Title
        =====
               
        .. data-viewer::
            :expand:
               
            {"a": 1, "b": 2}
               
        .. data-viewer::
            :file: test.json
        """),
        encoding="utf-8",
    )

    if version_info >= (7, 2):
        src_dir = tmp_path
        builddir = tmp_path / "_build"
    else:
        from sphinx.testing.path import path

        src_dir = path(str(tmp_path))
        builddir = path(str(tmp_path / "_build"))

    sphinx_app = make_app(
        srcdir=src_dir,
        builddir=builddir,
        buildername=builder,
    )
    sphinx_app.build()
    assert sphinx_app.statuscode == 0
    if builder in ("html", "singlehtml", "dirhtml"):
        assert sphinx_app._warning.getvalue() == ""
    else:
        # print(sphinx_app._warning.getvalue())
        assert (
            "index.rst:4: WARNING: sphinx-data-viewer does not support this builder"
            in sphinx_app._warning.getvalue()
        )
