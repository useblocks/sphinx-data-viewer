"""
Small API to create Data-Viewer nodes from other Sphinx extensions
"""

import json

from sphinx_data_viewer.directive import DataViewerNode


def get_data_viewer_node(title, data, expand=True):
    """
    Returns a docutils node, which represents a configured data-viewer.

    :param title: Title for the viewer as string
    :param data:  Data as python objects, which must be serializable by json.dumps()
    :param expand: True or False as boolean. If True all data will be shown.
    :return: Configured DataViewerNode instance
    """
    viewer_node = DataViewerNode()

    viewer_node['title'] = str(title)
    viewer_node['data'] = json.dumps(data)
    viewer_node['expand'] = str(expand)
    viewer_node['classes'] = ['sdv-data']

    return viewer_node

