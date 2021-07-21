.. _started:

Quick Start Guide
____________________________________________
============================================

.. figure:: ./_templates/resources/THREE.gif
   :alt: The Good Old Classic Percolation Question
   :align: center
   :scale: 65%

It is required that you have in system the following:

- `python` or `python3`.
- `pip` or `pip3`.


Installation
--------------------------------------------

Set Up repo and installs first. e.g. Unix like systems:

* $ `git clone https://github.com/alexisraelmtz/algoViewer.git`



* Within any venv install `pipenv` if not present:

    $ `pip install --user pipenv`



* Run $ `pipenv install --dev`



* Then run the `windows.py` file:

    $ `pipenv run python windows.py`

TIP: Activate the Pipenv Environment with `pipenv shell` and just run the command `python windows.py`.


Usage
---------------------------------------------

On mouse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Right Click:
  - Adds a single Node.
  - First 2 Nodes Default to START and TARGET node; Yellow and Orange colors correspondingly.
  - After 2 right clicks, it defaults to Wall Nodes.

2. Left Click:
  - Removes the selected Node which ever type it corresponds.

On Press Keyboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3. `C`: Clear Entire Graph.


Testing
---------------------------------------------

Verify that you are able to run the Coverage Test.
e.g. Unix like systems:

- $ `pipenv run pytest`


Repository
____________________________________________
--------------------------------------------

Feel Free to surf the Repository any time: `AlgoViewer - Official Repo
<https://github.com/alexisraelmtz/algoViewer/>`_.

