import json
import os

from docutils import nodes

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

from sphinx.util.osutil import copyfile

from sphinx_data_viewer.version import VERSION


class DataViewerNode(nodes.General, nodes.Element):
    pass


class DataViewerDirective(Directive):
    has_content = True
    optional_arguments = 1
    final_argument_whitespace = True

    option_spec = {
        "file": directives.unchanged,
        "data": directives.unchanged,
        "title": directives.unchanged,
        "expand": directives.flag
    }

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def run(self):
        env = self.state.document.settings.env
        data_string = "\n".join(self.content)

        data_expand = True if self.options.get('expand', False) is None else False

        data_option = self.options.get('data', None)
        if data_option:
            if data_option in env.config['data_viewer_data']:
                data_string = json.dumps(env.config['data_viewer_data'][data_option])

        file_option = self.options.get('file', None)
        if file_option:
            if not os.path.isabs(file_option):
                file_dir = os.path.dirname(self.state.document.current_source)
                file_option = os.path.join(file_dir, file_option)
            with open(file_option) as file_obj:
                # we load the data as json to be sure that it is really json data.
                data_string = json.dumps(json.load(file_obj))


        container = nodes.container(classes=['sphinx-data-viewer'])
        data_container = DataViewerNode(classes=['sdv-data'])
        data_container["data"] = data_string
        data_container["expand"] = data_expand
        data_container["title"] = self.options.get('title', '')

        container.append(data_container)

        return [container]


def setup(app):
    app.add_config_value('data_viewer_data', {}, 'html')
    app.add_node(DataViewerNode, html=(html_visit, html_depart))
    app.add_directive("data-viewer", DataViewerDirective)


    app.connect("env-updated", install_lib_static_files)

    return {
        "version": VERSION,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def html_visit(self, node):
    self.body.append(f"<p>{node.attributes['title']}</p>")
    self.body.append(f"<div class='{','.join(node.attributes['classes'])}' "
                     f"data-sdv='{node.attributes['data']}'"
                     f"data-expand={node.attributes['expand']}> </div>")


def html_depart(self, node):
    pass

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

        builder_static_path = os.path.join(app.builder.outdir, '_static')
        web_path = dest_path.replace(builder_static_path, '')
        if web_path.startswith('/'):
            web_path = web_path[1:]
        if extra_path.endswith('js'):
            app.add_js_file(str(web_path))
        elif extra_path.endswith('css'):
            app.add_css_file(str(web_path))
