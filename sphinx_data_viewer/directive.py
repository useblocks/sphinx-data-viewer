import json
import os

from docutils import nodes

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


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


def html_visit(self, node):
    self.body.append(f"<p>{node.attributes['title']}</p>")
    self.body.append(f"<div class='{','.join(node.attributes['classes'])}' "
                     f"data-sdv='{node.attributes['data']}'"
                     f"data-expand={node.attributes['expand']}> </div>")


def html_depart(self, node):
    pass
