# AlgoViewer -- by Alex Martinez

## Path Finding Algorithm Propagation Visualizer

[![Build Status](https://travis-ci.com/alexisraelmtz/algoViewer.svg?branch=main)](https://travis-ci.com/alexisraelmtz/algoViewer) [![Maintainability](https://api.codeclimate.com/v1/badges/e691cab9705bcfb3b7cf/maintainability)](https://codeclimate.com/github/alexisraelmtz/algoViewer/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/e691cab9705bcfb3b7cf/test_coverage)](https://codeclimate.com/github/alexisraelmtz/algoViewer/test_coverage)

Feel Free to Read our documentation at: [AlgoViewer - Official Doc](https://algoviewer.readthedocs.io/en/latest/)

---

<img src="/algoDocs/_templates/resources/4.gif" alt="The good Old Classic Percolation Question -" width="600"/>

## Preface

This project corresponds to my personal interests, given the chance to explore and create whatever API I wished. I chose to dive into the realm of two subjects I have a great passion for -

- Path Finding Algorithms and,
- Data Structures

## Problem

I have been very visual throughout all my life, and writing down simple data structures with pen on paper has always helped me understand the subject better. For this occasion, and after many dedicated hours into getting a basic understanding of Sorting and Path Finding algorithms, I think it is an excellent practice to create an API that traverses visually any generated graph structure. In addition to that, create a small Data Base of different types of Algorithms to choose from and learn about the inner workings visually.

## Solution

<div><img src="/algoDocs/_templates/resources/THREE.gif" alt="The good Old Classic Percolation Question -" width="400"/> <img src="/algoDocs/_templates/resources/5.gif" alt="The good Old Classic Percolation Question -" width="400"/></div>

The API is capable of traversing any path-finding algorithm through a graph-like data structure in a visual fashion, with the following -

### Featured Algorithms

- DFS,
- BFS,
- A Star,
- Cownway's Game Of Life

---

## Getting Started

### Install Requirements

It is required that you have in system the following:

- `python` or `python3`.
- `pip` or `pip3`.

### Installation

Set Up repo and installs first. e.g. Unix like systems:

- `git clone https://github.com/alexisraelmtz/algoViewer.git`.
  - Within any venv if not present install `pipenv`: $`pip install --user pipenv`.
- Run $`pipenv install --dev`
- Then run the `windows.py` file:
  - $ `pipenv run python windows.py`

TIP: Activate the Pipenv Environment with `pipenv shell` and just run the command `python windows.py`.

### Windows Users:

Run the following command:

- $`git clone https://github.com/alexisraelmtz/algoViewer.git`
- $`pip install pygame`
- $`cd algoViewer/algoViewer/`
- $`python windows.py`

---

### Usage

#### On mouse:

- Right Click:
  - Adds a single Node.
  - First 2 Nodes Default to START and TARGET node; Yellow and Orange colors correspondingly.
  - After 2 right clicks, it defaults to Wall Nodes.
- Left Click:
  - Removes the selected Node which ever type it corresponds.

#### On Press Keyboard:

- `C`: Clear Entire Graph.

---

### Testing

Verify that you are able to run the Coverage Test.
e.g. Unix like systems:

- $ `pipenv run pytest`

---

Feel Free to Read our documentation at: [AlgoViewer - Official Doc](https://algoviewer.readthedocs.io/en/latest/)

---

<div><img src="/algoDocs/_templates/resources/FIRST.gif" alt="The good Old Classic Percolation Question -" width="400"/><img src="/algoDocs/_templates/resources/B.PNG" alt="The good Old Classic Percolation Question -" width="400"/><img src="/algoDocs/_templates/resources/A.PNG" alt="The good Old Classic Percolation Question -" width="400"/><img src="/algoDocs/_templates/resources/SEC.gif" alt="The good Old Classic Percolation Question -" width="400"/></div>
