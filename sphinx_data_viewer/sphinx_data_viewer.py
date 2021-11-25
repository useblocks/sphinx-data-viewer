import os

from docutils import nodes

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

from sphinx.util.osutil import copyfile

from sphinx_data_viewer.version import VERSION


class DataViewerDirective(Directive):
    has_content = True

    option_spec = {
        "file": directives.unchanged,
        "data": directives.unchanged
    }

    def run(self):
        container = nodes.container(classes=['sphinx-data-viewer'])
        title = nodes.paragraph("", "Cool title")

        container.append(title)
        return [container]


def setup(app):
    app.add_directive("data-viewer", DataViewerDirective)
    app.connect("env-updated", install_lib_static_files)

    return {
        "version": VERSION,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def install_lib_static_files(app, env):
    # Add js / css files to the final project
    extra_files = ['assets/jsonview.bundle.js', 'assets/jsonview_loader.js', 'assets/jsonview.bundle.css']
    this_path = os.path.abspath(os.path.dirname(__file__))

    static_path = os.path.join(app.builder.outdir, '_static')
    try:
        os.mkdir(static_path)
    except FileExistsError:
        pass

    for extra_file in extra_files:
        extra_path = os.path.join(this_path, extra_file)
        extra_dir = os.path.dirname(extra_path).replace(this_path, '')
        if extra_dir.startswith('/'):
            extra_dir = extra_dir[1:]
        if not os.path.exists(extra_path):
            raise FileNotFoundError(f'Not found: {extra_path}')

        static_file_dir = os.path.join(static_path, extra_dir)
        try:
            os.mkdir(static_file_dir)
        except FileExistsError:
            pass

        dest_path = os.path.join(static_path, extra_file)
        copyfile(extra_path, dest_path)

        if extra_path.endswith('js'):
            app.add_js_file(str(extra_path))
        elif extra_path.endswith('css'):
            app.add_css_file(str(extra_path))
