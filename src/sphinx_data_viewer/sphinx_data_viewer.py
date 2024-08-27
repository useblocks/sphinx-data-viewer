from pathlib import Path

from sphinx import version_info as sphinx_version
from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset
from sphinx.util.logging import getLogger

from sphinx_data_viewer.directive import (
    DataViewerDirective,
    DataViewerNode,
    html_depart,
    html_visit,
    skip_visit,
)

LOGGER = getLogger(__name__)


def setup(app: Sphinx):
    from . import __version__

    app.add_config_value("data_viewer_data", {}, "html")
    app.add_node(
        DataViewerNode,
        html=(html_visit, html_depart),
        latex=(skip_visit, None),
        text=(skip_visit, None),
        man=(skip_visit, None),
        texinfo=(skip_visit, None),
        epub=(skip_visit, None),
    )
    app.add_directive("data-viewer", DataViewerDirective)
    app.connect("env-updated", install_lib_static_files)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def install_lib_static_files(app: Sphinx, env) -> None:
    """Copies css and js files to the output directory and adds them to the builder."""

    if app.builder.format != "html":
        return

    LOGGER.info("Copying static files for sphinx-data-viewer support")

    statics_dir = Path(app.builder.outdir) / "_static"
    source_dir = Path(__file__).parent / "assets"
    destination_dir = statics_dir / "sphinx-data-viewer"
    copy_asset(str(source_dir), str(destination_dir))

    lib_path = Path("sphinx-data-viewer")
    _add_js_file(app, lib_path.joinpath("jsonview.bundle.js"))
    _add_js_file(app, lib_path.joinpath("jsonview_loader.js"))
    _add_css_file(app, lib_path.joinpath("jsonview.bundle.css"))


def _add_css_file(app: Sphinx, rel_path: Path) -> None:
    # note this deduplication is already done in Sphinx v7.2.1+
    # https://github.com/sphinx-doc/sphinx/commit/0c22d9c9ff4a0a6b3ce2f0aa6bc591b4525b4163
    rel_str = rel_path.as_posix()
    if sphinx_version < (7, 2) and f"_static/{rel_str}" in getattr(
        app.builder, "css_files", []
    ):
        return
    app.add_css_file(rel_str)


def _add_js_file(app: Sphinx, rel_path: Path) -> None:
    # note this deduplication is already done in Sphinx v7.2.1+
    # https://github.com/sphinx-doc/sphinx/commit/0c22d9c9ff4a0a6b3ce2f0aa6bc591b4525b4163
    rel_str = rel_path.as_posix()
    if sphinx_version < (7, 2) and f"_static/{rel_str}" in getattr(
        app.builder, "script_files", []
    ):
        return
    app.add_js_file(rel_str)
