.. image:: _static/sphinx-data-viewer-logo.svg
   :align: center
   :width: 200px
   :height: 200px

|

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

Supports data from ``data-viewer`` content, files or variables from a ``conf.py`` configuration.

Installation
------------
Use ``pip`` to install ``Sphinx-Data-Viewer``

.. code-block:: python

   pip install sphinx-data-viewer

Then add it to the extensions of your ``conf.py`` file

.. code-block:: python


   extensions = [
       "sphinx_data_viewer",
   ]


Options
-------

title
~~~~~
Sets a title in front of the data representation.

Default: None

.. tab-set::

    .. tab-item:: Code
    
       .. code-block:: rst
    
          .. data-viewer::
             :title: My first data viewer example
    
             ["apple", "orange", "banana"]
    
    .. tab-item:: Result
    
       .. data-viewer::
          :title: My first data viewer example
    
          ["apple", "orange", "banana"]

expand
~~~~~~
Use ``expand`` to show the complete data.

``expand`` does not need any value, as it is a flag and its usage is enough to set it to True.

Default: False (not set)

.. tab-set::

    .. tab-item:: Code
    
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
    
    .. tab-item:: Result
    
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
Use ``file`` to load data from a file.

``file`` takes an absolute or relative path.
If it is relative, an absolut path gets calculated based on current document path.

Default: None

.. tab-set::

    .. tab-item:: Code
    
       .. code-block:: rst
    
          .. data-viewer::
             :file: test.json
    
    .. tab-item:: Data
    
       .. literalinclude:: test.json
          :language: json
    
    .. tab-item:: Result
    
       .. data-viewer::
          :file: test.json


data
~~~~
``data`` defines a key, which is taken to look up for data in the configuration variable ``data_viewer_data``.

Default: None

.. tab-set::

    .. tab-item:: Code
    
       .. code-block:: rst
    
          .. data-viewer::
             :data: my_data
    
    .. tab-item:: Config
    
       .. code-block:: rst
    
          # Inside conf.py
    
          data_viewer_data = {
              "my_data": {
                  "name": "Mario",
                  "job": "plumber",
                  "magic_tubes": [2, 7, 23, 43.5]
              }
          }
    
    .. tab-item:: Result
    
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

.. tab-set::

    .. tab-item:: Result
    
       Problem: Missing ``,`` after ``"Peter"``
    
        .. data-viewer::
    
          {
            "name": "Peter"
            "user": "peterbomber"
          }
    
    .. tab-item:: Code
    
       .. code-block:: rst
    
          Problem: Missing `,` after `"Peter"`
    
          .. data-viewer::
    
             {
               "name": "Peter"
               "user": "peterbomber"
             }

Works well with...
------------------
Here are some ideas and examples, how ``data-viewer`` could be used together with other Sphinx extensions.

Sphinx-Needs
~~~~~~~~~~~~
Use `Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io>`_ to define process elements like requirements and
specifications. And ``Sphinx-Data-Viewer`` to explain data structures more easily.

.. tab-set::

    .. tab-item:: Result

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

    .. tab-item:: Code
    
       .. code-block:: rst
    
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

Sphinx-Design
~~~~~~~~~~~~~
`Sphinx-Design <https://sphinx-design.readthedocs.io>`_ can be used to bring cards, tabs and dropdowns into your
documentation. It can help you to show source code or the data-viewer on user requests only.

All the dropdowns and tabs on this side got realised by ``Sphinx-Design``.

Take a look into `the current page source <_sources/index.rst.txt>`_ for a bunch of examples.

.. tab-set::

    .. tab-item:: Result

       .. grid:: 2

           .. grid-item-card::

              Data-Viewer 1
              ^^^^^^^^^^^^^

              .. data-viewer::
                 :expand:

                 {
                    "name": "Peter",
                    "pets": ["dog", "cat"]
                 }

           .. grid-item-card::

              Data-Viewer 2
              ^^^^^^^^^^^^^

              .. data-viewer::
                 :expand:

                 {
                    "name": "Sandra",
                    "pets": ["squirrel"]
                 }

    .. tab-item:: Code

       .. code-block:: rst

           .. grid:: 2

               .. grid-item-card::

                  Data-Viewer 1
                  ^^^^^^^^^^^^^

                  .. data-viewer::
                     :expand:

                     {
                        "name": "Peter",
                        "pets": ["dog", "cat"]
                     }

               .. grid-item-card::

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


API
---

.. automodule:: sphinx_data_viewer.api
   :members:

Kudos
-----
The javascript code is based on the wonderful work of https://github.com/pgrabovets/json-view.

Changelog
---------

0.1.4
~~~~~
:released: 25.1.2024

* Bugfix: Fix for builders, which do not support registration of CSS/JS files (e.g. sphinxcontrib-spelling)


0.1.3
~~~~~
:released: 25.1.2024

* Improvement: Updated project documentation to use the useblocks theme.
* Bugfix: Avoids multiple registrations of the same CSS/JS file.

0.1.2
~~~~~
:released: 07.12.2021

* Bugfix: Fixed wrong handling of windows path.
  (`#2 <https://github.com/useblocks/sphinx-data-viewer/issues/2>`_)

0.1.1
~~~~~
:released: 30.11.2021

* Improvement: Provides API
* Improvement: Restructured code

0.1.0
~~~~~
:released: 26.11.2021

* Improvement: Provides ``data-viewer`` directive
* Improvement: Options added: file, title, data, expand

.. toctree::
   :hidden:
