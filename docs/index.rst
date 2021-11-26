Sphinx-Data-Viewer
==================
A simple data viewer for data of type json or python object, which shows the data in an interactive
list-view on HTML pages.

.. data-viewer::
   :expand:

   {
      "Peter Meister": {
         "firstname": "Peter",
         "surname": "Meister",
         "is_female": false,
         "city": "Munich",
         "age": 26,
         "height_m": 1.86,
         "nicknames": ["Peti", "Pet", "Bomber"]
      },
      "Sandra Wilson": {
         "firstname": "Sandra",
         "surname": "Wilson",
         "is_female": true,
         "city": "London",
         "age": 32,
         "height_m": 1.67,
         "nicknames": ["Sandy", "Wilma"]
      }
   }

.. dropdown:: Show source code for above example

   .. code-block:: rst

      .. data-viewer::
         :expand:

         {
            "Peter Meister": {
               "firstname": "Peter",
               "surname": "Meister",
               "city": "Munich",
               "age": 26,
               "height_m": 1.86
               "nicknames": ["Peti", "Pet", "Bomber"]
            },
            "Sandra Wilson": {
               "firstname": "Sandra",
               "surname": "Wilson",
               "city": "London",
               "age": 32,
               "height_m": 1.67
               "nicknames": ["Sandy", "Wilma"]
            }
         }

Supports data from ``data-viewer`` content, files or variables from a ``conf.py`` configuration.

**Page content**

.. contents::
   :local:

Installation
------------
Use ``pip`` to install ``Sphinx-Data-Viewer``::

   pip install sphinx-data-viewer

Then add it to the extensions of your ``conf.py`` file::

   extensions = [
       "sphinx_data_viewer",
   ]


Options
-------

title
~~~~~
Sets a title in front of the data representation.

Default: None

.. tabbed:: Code

   .. code-block:: rst

      .. data-viewer::
         :title: My first data viewer example

         ["apple", "orange", "banana"]

.. tabbed:: Result

   .. data-viewer::
      :title: My first data viewer example

      ["apple", "orange", "banana"]

expand
~~~~~~
Use ``expand`` to show the complete data.

``expand`` does not need any value, as it is a flag and its usage is enough to set it to True.

Default: False (not set)

.. tabbed:: Code

   .. code-block:: rst

      .. data-viewer::
         :expand:

         {
            "Peter Meister": {
               "firstname": "Peter",
               "surname": "Meister",
               "city": "Munich",
               "age": 26,
               "height_m": 1.86,
               "nicknames": ["Peti", "Pet", "Bomber"]
            },
            "Sandra Wilson": {
               "firstname": "Sandra",
               "surname": "Wilson",
               "city": "London",
               "age": 32,
               "height_m": 1.67,
               "nicknames": ["Sandy", "Wilma"]
            }
         }

.. tabbed:: Result

   .. data-viewer::
      :expand:

      {
         "Peter Meister": {
            "firstname": "Peter",
            "surname": "Meister",
            "city": "Munich",
            "age": 26,
            "height_m": 1.86,
            "nicknames": ["Peti", "Pet", "Bomber"]
         },
         "Sandra Wilson": {
            "firstname": "Sandra",
            "surname": "Wilson",
            "city": "London",
            "age": 32,
            "height_m": 1.67,
            "nicknames": ["Sandy", "Wilma"]
         }
      }


file
~~~~
Use ``file`` to load data from a file.Data

``file`` takes an absolute or relative path.
If it is relative, an absolut path gets calculated based on current document path.

Default: None

.. tabbed:: Code

   .. code-block:: rst

      .. data-viewer::
         :file: test.json

.. tabbed:: Data

   .. literalinclude:: test.json
      :language: json

.. tabbed:: Result

   .. data-viewer::
      :file: test.json


data
~~~~
``data`` defines a key, which is taken to look up for data in the configuration variable ``data_viewer_data``.

Default: None

.. tabbed:: Code

   .. code-block:: rst

      .. data-viewer::
         :data: my_data

.. tabbed:: Config

   .. code-block:: rst

      # Inside conf.py

      data_viewer_data = {
          "my_data": {
              "name": "Mario",
              "job": "plumber",
              "magic_tubes": [2, 7, 23, 43.5]
          }
      }

.. tabbed:: Result

   .. data-viewer::
      :data: my_data

Errors
------
The data must be always valid json-data, if it is coming from the content of ``data-viewer`` or if it gets read from
a file.

If ``data`` option is used to read data from the ``data_viewer_data`` option of your ``conf.py``, this referenced object
gets loaded via ``json.dumps()``, so that the object must be serializable.

Parsing exception can happen during Sphinx-Build and in the used JavaScript code when the browser loads the page.

If the JavaScript code detects problems, some error text gets printed on the webpage.

.. tabbed:: Result

   Problem: Missing ``,`` after ``"Peter"``

    .. data-viewer::

      {
        "name": "Peter"
        "user": "peterbomber"
      }

.. tabbed:: Code

   .. code-block:: rst

      Problem: Missing `,` after `"Peter"`

      .. data-viewer::

         {
           "name": "Peter"
           "user": "peterbomber"
         }

Works well with...
------------------
Here some ideas and examples, how ``data-viewer`` could be used together with other Sphinx extensions.


Sphinx-Needs
~~~~~~~~~~~~
Use `Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io>`_ to define process elements like requirements and
specifications. And ``Sphinx-Data-Viewer`` to explain data structures more easily.

.. tabbed:: Result

   .. spec:: /api/user return value
      :id: SPEC_001
      :tags: endpoint, user
      :status: open

      For our API endpoint ``/api/user`` the default data structure of the return value of a successful GET
      request shall look like:

      .. data-viewer::
         :expand:

         {
            "username": "peterbomber",
            "email": "peterbomber@my_company.net",
            "active": true
         }

.. tabbed:: Code

   .. code-block::

      .. spec:: /api/user return value
         :id: SPEC_001
         :tags: endpoint, user
         :status: open

         For our API endpoint ``/api/user`` the default data structure of the return value of a successful GET
         request shall look like:

         .. data-viewer::
            :expand:

            {
               "username": "peterbomber",
               "email": "peterbomber@my_company.net",
               "active": true
            }

Sphinx-Panels
~~~~~~~~~~~~~
`Sphinx-Panels <https://sphinx-panels.readthedocs.io>`_ can be used to bring cards, tabs and dropdowns into your
documentation. It can help you to show source code or the data-viewer on user requests only.

All the dropdowns and tabs on this side got realised by ``Sphinx-Panels``.

Take a look into `the current page source <_sources/index.rst.txt>`_ for a bunch of examples.

.. tabbed:: Result

   .. panels::

      Data-Viewer 1
      ^^^^^^^^^^^^^

      .. data-viewer::
         :expand:

         {
            "name": "Peter",
            "pets": ["dog", "cat"]
         }

      ---

      Data-Viewer 2
      ^^^^^^^^^^^^^

      .. data-viewer::
         :expand:

         {
            "name": "Sandra",
            "pets": ["squirrel"]
         }

.. tabbed:: Code

   .. code-block:: rst

      .. panels::

         Data-Viewer 1
         ^^^^^^^^^^^^^

         .. data-viewer::
            :expand:

            {
               "name": "Peter",
               "pets": ["dog", "cat"]
            }

         ---

         Data-Viewer 2
         ^^^^^^^^^^^^^

         .. data-viewer::
            :expand:

            {
               "name": "Sandra",
               "pets": ["squirrel"]
            }

License
-------
This software project is released under the MIT license.

See `LICENSE file <https://github.com/useblocks/sphinx-data-viewer/blob/main/LICENSE>`_ for more details.


Kudos
-----
The javascript code is based on the wonderful work of https://github.com/pgrabovets/json-view.

Changelog
---------

0.1.1
~~~~~
:released: under development

0.1.0
~~~~~
:released: 26.11.2021

* Improvement: Provides ``data-viewer`` directive
* Improvement: Options added: file, title, data, expand

.. toctree::
