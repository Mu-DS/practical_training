# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: py38
#     language: python
#     name: py38
# ---

# + [markdown] Collapsed="false"
# # Fundamentals of Production Code

# + [markdown] Collapsed="false"
# This presentation is written by @the-rccg for the Practical Data Science for Researchers Course for the Helmholtz Graduate School for Data Science in Munich (MUDS), Spring 2020.

# + [markdown] Collapsed="true" toc-hr-collapsed=true
# ## Data Science Teams

# + [markdown] Collapsed="false"
# Strong opinions + respectful conversations = better results

# + [markdown] Collapsed="true"
# ### Agile mindset vs process
# Thank you to Nicole Carlson and her talk at PyData Austin 2019 (https://www.youtube.com/watch?v=2v9uwedgBxU)
#
# Come up with a process that works for the team
#
# #### Sprint planning
# - each person comes up with their own tasks
# - group discusses tasks  +  estimate times
# - R&D or Literature Review tasks are timeboxed
# - Long-term project planning happens aoutside of the meeting
# - Code Reviews are assigned after the meeting
#
# #### Central place to track your work: 
# - Overview: What is each person working on?
# - Ordering: What will you work on next?
# - Timeline: What is the overall outline of your project
# - Ideas: What are potential future projects/follow-ups?
# - Collaboration: What requests have you gotten from other teams?
#
# ##### Full Team Trackers:
# - [Asana](https://www.asana.com/)
# - [Trello](https://www.trello.com/)
# - [Jira](https://www.atlassian.com/software/jira/)
#
# ##### Simple Trackers:
# - [Todoist](https://www.todoist.com)
# - [GitHub](https://www.github.com)
#
# ##### Not Trackers:
# - [Slack](https://www.slack.com)
# - E-Mail
#

# + [markdown] Collapsed="false"
# ### Common Utilities Repo
# People will face the same challenges, <u>***especially new people***</u>. Keep solutions in one place.
#
# - Database
#   - common queries, instructions, etc.
#   - descriptions for each
#   - how to acces it
# - Data Processing
#   - transformations
#   - common tools and how to use them
# - Helpers
#   - logging
#   - unittesting
#   - visualizations
# - Coding Standards
#   - PEP8
#   - linter configuration file

# + Collapsed="false"


# + [markdown] Collapsed="false"
# ## Overview: Fundamentals of Production Code
#
# - Environments  (Robin)
# - Code Style  (Robin)
# - Design Patterns  (Robin?)
# - Thinking Functionally  (Robin)

# + [markdown] Collapsed="true" toc-hr-collapsed=true endofcell="--"
# ## Overview: Setting Up the Environment
#
# - virtual environments
# - vscode for working on remote server
# - jupyter for working on remote server
# - 
# --

# + [markdown] Collapsed="false"
# ### Virtual Environments

# + [markdown] Collapsed="true"
# #### Creating an Environment (env) to update to Python 3.8
#
# List current environments:
# ```bash
# conda env list
# ```
#
# Export current env:
# ```bash
# conda list --explicit > current_env.txt
# ```
#
# Create new env for Python=3.8:
# ```bash
# conda create --name py38 python=3.8
# ```
#
# Switch environment:
# ```bash
# activate py38
# ```
#
# Simply install what you need:
# ```bash
# conda install matplotlib jupyter tensorflow dask numba
# ```
#

# + [markdown] Collapsed="true"
# #### Registering Environments as Kernels in Jupyter

# + [markdown] Collapsed="false"
# ```bash
# conda activate py38
# conda install ipykernel
# python -m ipykernel install --user --name=py38
# conda activate base
# jupyter lab
# ```

# + [markdown] Collapsed="false"
# <img src=img/jupyter_environments.png />

# + [markdown] Collapsed="true"
# #### Other Environments
#
# You might have heard or read about the Python Virtual Environments, however, the Conda version allows for a higher encapsulation of entirely independent Python installations for each environment, as well as other tools.
#
# This works similarly to how Conda provides a higher abstraction and utility with respect to modules than PIP does, as for example its dependency resolution.

# + [markdown] Collapsed="true"
# ### IDEs

# + [markdown] Collapsed="false"
# - [VSCode](https://code.visualstudio.com/)
#   - Multi-Language support
#   - Extensible
#   - Open Source
#   - Very light weight
#   - Great support and stability thanks to Microsoft financing
# - [PyCharm](https://www.jetbrains.com/pycharm/)
#   - Free for students
#   - Very heavy weight
# - [Spyder](https://www.spyder-ide.org/)
#   - Great for scripting/Analysis
#   - Open Source
# - [Atom](https://www.atom.io/)
#   - Extensible
#   - Open Source

# + [markdown] Collapsed="true"
# ### [VSCode](https://code.visualstudio.com/) for working on Remote Server

# + [markdown] Collapsed="false"
# Why it's useful: (non comprehensive list)
#
# - Write code directly on the server you're deploying on with full IDE capability
# - All benefits of your locally installed Extensions and Settings for the remote server
# - Simply drag-and-drop for moving files

# + [markdown] Collapsed="false"
# #### Getting the Extension
#
# 1. `ctrl/cmd + shift + p` opens the console in run command mode indicated by `>`
# 2. run `Extensions: install Extensions`
# 3. install `Remote - SSH`
# 4. Now you have a new icon in the footer: 
#
#    <img width=300, height=15, src="img/ssh-remote.png">
#    
# 6. `Remote-SSH: Connect to Host...`
# 7. `Add New SSH Host...`
#

# + [markdown] Collapsed="false"
#

# + [markdown] Collapsed="false"
# ### Jupyter for working on Remote Server

# + [markdown] Collapsed="false"
# 1. Connect to remote server
# 2. Start Jupyter server on a free port
# 3. Tunnel the port to your machine to work as if it was local

# + [markdown] Collapsed="false" slideshow={"slide_type": "slide"}
# Reverse Tunneling 
# ```bash
# ssh usernam@host.de -NL remote_port:local_host:local_port
# ```
# Example:
# ```bash
# ssh rgreif@host.mu-ds.de -NL 8889:localhost:8888
# ```

# + [markdown] Collapsed="false" slideshow={"slide_type": "slide"}
# ```bash
# ssh usernam@host.de -NL remote_port:local_host:local_port
# ```
#
# -N 
#
#     "Nothing else": tells the ssh client that no command executionafterwards is needed
#     
# -L [protocol/][listening_host:] listening_port:host:hostport
#     
#     "Listen": redirects data from the port following, through the secure tunnel to the destination address and port following, e.g. localhost:8888. 

# + Collapsed="false"


# + [markdown] Collapsed="true" toc-hr-collapsed=true
# ## Code Style

# + [markdown] Collapsed="false"
# - The Zen of Python
# - PEP8
# - PyLint
# - Flake8
# - How to select which linting rules to use?
#     - Hierarchical structure of: Necessary, Optional, Not needed

# + [markdown] Collapsed="false"
# ### The Zen of Python
#
# The "guiding principles" of how to write Python code, formulated in 1999 and published as **Python Enhancement Proposal (PEP)** 20.

# + Collapsed="false"
import this

# + [markdown] Collapsed="false"
# ### So what does this mean?

# + [markdown] Collapsed="true"
# #### ***Explicit is better than implicit.***

# + [markdown] Collapsed="false"
# ```python
# from some_file import custom_object
#
# custom_object().run()
# ```

# + [markdown] Collapsed="false"
# ```python
# import  some_file as fncs
#
# data = fncs.load_data('data.csv')
# proc_data = fncs.process_data(data)
# print(summarize_data(proc_data))
# ```

# + [markdown] Collapsed="true"
# #### ***Simple is better than complex.***
#

# + [markdown] Collapsed="true"
# #### ***Flat is better than nested.***
#

# + [markdown] Collapsed="false"
# ```python
# center_slices = tuple([(slice(1, -1) if i == ax else (slice(1, -1)) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# upper_slices = tuple([(slice(2, None) if i == ax else (slice(1, -1)) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# lower_slices = tuple([(slice(-2) if i == ax else (slice(1, -1)) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# ```

# + [markdown] Collapsed="false"
# ```python
# # (c)enter (u)pper (l)ower
# c_slices = tuple([(slice(1, -1)   if i == ax else slice(1, -1) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# u_slices = tuple([(slice(2, None) if i == ax else slice(1, -1) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# l_slices = tuple([(slice(-2)      if i == ax else slice(1, -1) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# ```

# + [markdown] Collapsed="false"
# ```python
# c_slices = []
# u_slices = []
# l_slices = []
# for i in dims:
#     if i == ax:
#         c_slices.append(slice(1, -1))
#         u_slices.append(slice(2,None))
#         l_slices.append(slice(-2))
#     elif _contains_axis(axes, i, rank):
#         c_slices.append(slice(1, -1))
#         u_slices.append(slice(1, -1))
#         l_slices.append(slice(1, -1))
#     else:
#         c_slices.append(slice(None))
#         u_slices.append(slice(None))
#         l_slices.append(slice(None))
# c_slices = tuple(c_slices)
# u_slices = tuple(u_slices)
# l_slices = tuple(l_slices)
# ```

# + [markdown] Collapsed="false"
# ```python
# c_slices = [slice(None)]*len(dims)
# u_slices = [slice(None)]*len(dims)
# l_slices = [slice(None)]*len(dims)
# # i == ax
# c_slices[ax] = slice(1, -1)
# u_slices[ax] = slice(2, None)
# l_slices[ax] = slice(-2)
# # if contained
# f2 = [_contains_axis(axes, i, rank) for i in dims]
# c_slices[f2] = slice(1, -1)
# u_slices[f2] = slice(1, -1)
# l_slices[f2] = slice(1, -1)
# # make tuple
# c_slices = tuple(c_slices)
# u_slices = tuple(u_slices)
# l_slices = tuple(l_slices)
# ```

# + [markdown] Collapsed="false"
#

# + [markdown] Collapsed="false"
# #### ***Readability counts.***
#
#

# + [markdown] Collapsed="true"
# #### ***Special cases aren't special enough to break the rules.***
#
#

# + [markdown] Collapsed="true"
# #### ***If the implementation is hard to explain, it's a bad idea.***
#

# + [markdown] Collapsed="true"
# #### ***Namespaces are one honking great idea -- let's do more of those!***

# + [markdown] Collapsed="false"
# ```python
# from phi.flow import *
# ```
# vs.
# ```python
# from phi.flow import physics, smoke
# ```

# + [markdown] Collapsed="false"
# `math.py`
# ```python
# from .base import backend
# abs = backend.abs
# all = backend.all
# ```
# `run.py`
# ```python
# from .math import *
# ```
# vs.
# `run.py`
# ```python
# from .base import backend
# # use: backend.abs(), backend.all()
# ```

# + [markdown] Collapsed="false"
# `math.py`
# ```python
# from .base import backend
# abs = backend.abs  # redefines built-in keyword
# all = backend.all  # redefines built-in keyword
# ```
# `run.py`
# ```python
# from .math import *  # ambiguity with math core module, wildcard import, REDEFINING BUILT-IN KEYWORDS
# ```
# vs.
# `run.py`
# ```python
# from .base import backend  # explicit import
# # use: backend.abs(), backend.all()  explicit use
# ```

# + [markdown] Collapsed="false"
# ##### From Meetings
#
# "I just want to make the examples as short as possible so people can see how easy it is to use"
# -- author of a 2 line example (`import object; object.run()`)
#
#

# + Collapsed="false"


# + [markdown] Collapsed="true"
# #### Comments are important, but Documentation and schematics are even more important
#
# <img src="https://preview.redd.it/jm8b5iwoq6p11.png?width=640&crop=smart&auto=webp&s=f4f484b59333e96555d8076b13dfbc2f8fc2b5b3" width=400>

# + Collapsed="false"


# + [markdown] Collapsed="false"
# ### Whats the difference between good code and bad code?

# + [markdown] Collapsed="false"
# Good code is code ***I*** wrote.
#
# Bad code is code ***you*** wrote.

# + [markdown] Collapsed="false"
# Well, but how do we agree on that **this** code is good code?

# + [markdown] Collapsed="false"
# Welcome to Code Style and Style Guides! 

# + [markdown] Collapsed="false"
#

# + [markdown] Collapsed="true"
# ### PEP 8

# + [markdown] Collapsed="true"
# #### Coworker is asking to see your code? 
#
# <img src="https://preview.redd.it/hk54ti5n6tk11.png?width=640&crop=smart&auto=webp&s=6b84e81dae311d0f055a43ee5dfda6f68d253e47" width=300>

# + [markdown] Collapsed="false"
# #### How code should look like:
#
# - Only one statement per line
# - All imports on top
# - Imports grouped by global/local, ordered by depth then alphabetically
# - Between global and local imports: 1 blanck line
# - After imports: 1 blanck line
# - Before/After functions: 1 blanck line
# - Before/After classes: 2 blanck lines
# - End of file: 1 blanck line
# - ...
#
# https://www.python.org/dev/peps/pep-0008/

# + [markdown] Collapsed="true"
# #### Naming Styles
#
# | Name               | Example                    |
# |--------------------|----------------------------|
# | Upper Camel Case   | ThisIsCapitalCamelCase     |
# | Lower Camel Case   | thisIsLowerCamelCase       |
# | Snake Case         | this_is_snake_case         |
# | Capital Snake Case | THIS_IS_CAPITAL_SNAKE_CASE |

# + [markdown] Collapsed="true"
# #### Which to use for what?
#
# | Object    | Naming Style     |
# |-----------|------------------|
# | Variables | `snake_case`       |
# | Constants | `CAPITAL_SNAKE_CASE`       |
# | Classes   | `CapitalCamelCase`  |
# | Functions | `snake_case`       |
# | Packages  | `alllowercase`    |
#
# https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
#
# | Object                        | Naming Style        | Resulting Behavior                                                 |
# |-------------------------------|---------------------|--------------------------------------------------------------------|
# | Private Variables/Functions   | `_snake_case`       | Not imported with `*`, linter will complain if accessed externally |
# | Private Classes               | `_CapitalCamel`     | Not imported with `*`, linter will complain if accessed externally |
# | Python Keyword Conflicts      | `trailing_`         | Nothing special |
# | Private Attributes of Classes | `__double_leading`  | invokes name mangling (inside class FooBar, `__bar` becomes `_FooBat__boo`) |
# | magic objects/attributes      | `__double_double__` | living in user-controlled namespaces e.g. __init__, __import__, __file__ |
#

# + [markdown] Collapsed="false"
#

# + [markdown] Collapsed="false"
# Problem: antonyms are often not equally sized
# ```
# open   or  first  or  read   or  initial  or  begin  
# close  or  last   or  write  or  final    or  end    
# ```
#
# Some properties already have common abbreviations that fit
# ```
# avg  
# std  
# len  
# ```

# + [markdown] Collapsed="false"
# Useful equal sized words:
#
# ``` 
# first  or  begin  or  init
# final  or  final  or  last
#
# read  or  open
# save  or  save
#
# exec 
# wait
# ```

# + Collapsed="false"


# + [markdown] Collapsed="true"
# #### PEP8 is not definite

# + [markdown] Collapsed="false"
# ```python
# # No extra indentation.
# if (this_is_one_thing and
#     that_is_another_thing):
#     do_something()
#
# # Add a comment, which will provide some distinction in editors
# # supporting syntax highlighting.
# if (this_is_one_thing and
#     that_is_another_thing):
#     # Since both conditions are true, we can frobnicate.
#     do_something()
#
# # Add some extra indentation on the conditional continuation line.
# if (this_is_one_thing
#         and that_is_another_thing):
#     do_something()
# ```

# + [markdown] Collapsed="false"
# ```python
# if flag.is_data_bound and \
#         flag.propagates(_PROPAGATOR.RESAMPLE) and \
#         flag.is_applicable(resulting_rank, data_field.component_count):
#     flags.append(flag)
# ```

# + [markdown] Collapsed="false"
# ```python
# if (flag.is_data_bound
#         and flag.propagates(_PROPAGATOR.RESAMPLE)
#         and flag.is_applicable(resulting_rank, data_field.component_count):
#     flags.append(flag)
# ```

# + [markdown] Collapsed="false"
# ```python
# if (flag.is_data_bound and flag.propagates(_PROPAGATOR.RESAMPLE)
#                        and flag.is_applicable(resulting_rank, data_field.component_count):
#     flags.append(flag)
# ```

# + [markdown] Collapsed="false"
# ##### Real-world Example

# + Collapsed="false"
f2 = [_contains_axis(axes, i, rank) for i in dims]
f2 = list(map(lambda i: _contains_axis(axes, i, rank), dims))

# + [markdown] Collapsed="false"
#

# + Collapsed="false"
[slice(None)]*5

# + Collapsed="false"


# + Collapsed="false"


# + [markdown] Collapsed="false"
#

# + Collapsed="false"
def _pad_mode(extrapolation):
    if extrapolation == 'periodic':
        return 'wrap'
    elif extrapolation == 'boundary':
        return 'replicate'
    else:
        return extrapolation


# + Collapsed="false"
extrapolation_map = {
    'periodic': 'wrap',
    'boundary': 'replicate',
    'constant': 'constant'
} 

extrapolation_map[extrapolation]

# + Collapsed="false"


# + [markdown] Collapsed="false"
# https://access.redhat.com/blogs/766093/posts/2802001

# + Collapsed="false"


# + [markdown] Collapsed="true"
# #### Comment, but not unecessarily

# + [markdown] Collapsed="false"
# - at least 2 spaces to code
# - start with #
# - followed by a single space

# + [markdown] Collapsed="false"
# Inline comments are unnecessary and in fact distracting if they state the obvious. Don't do this:
# ```python
# x = x + 1                 # Increment x
# ```
#
# But sometimes, this is useful:
# ```python
# x = x + 1                 # Compensate for border
# ```

# + Collapsed="false"


# + [markdown] Collapsed="true"
# #### Docstrings
#
# <img src="https://preview.redd.it/a5skfy5y88x11.jpg?width=640&crop=smart&auto=webp&s=edee581af2812ad4f4469d13e79e38d9b2dd3f06" width=300>

# + [markdown] Collapsed="false"
# ##### PEP8 Docstrings

# + [markdown] Collapsed="false"
# > Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.

# + [markdown] Collapsed="false"
# >  most importantly, the """ that ends a multiline docstring should be on a line by itself:
#
# ```python
# """Return a foobang
#
# Optional plotz says to frobnicate the bizbaz first.
# """
# ```
# > For one liner docstrings, please keep the closing """ on the same line.
#

# + [markdown] Collapsed="false"
#
# Module Level Dunder Names
#
# Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__, __author__, __version__, etc. should be placed after the module docstring but before any import statements except from __future__ imports. Python mandates that future-imports must appear in the module before any other code except docstrings:
#
# ```python
# """This is the example module.
#
# This module does stuff.
# """
#
# from __future__ import barry_as_FLUFL
#
# __all__ = ['a', 'b', 'c']
# __version__ = '0.1'
# __author__ = 'Cardinal Biggles'
#
# import os
# import sys
# ```
#

# + [markdown] Collapsed="false"
# ##### PEP257, The Docstring Conventions Guide

# + [markdown] Collapsed="false"
# https://www.python.org/dev/peps/pep-0257/

# + [markdown] Collapsed="false"
# ###### What is a docstring?
#
# > A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__` special attribute of that object.

# + [markdown] Collapsed="false"
# ###### Single Line Docstring

# + [markdown] Collapsed="false"
# > Triple quotes are used even though the string fits on one line. This makes it easy to later expand it.
#
# > The closing quotes are on the same line as the opening quotes. This looks better for one-liners.
#
# > There's no blank line either before or after the docstring.
#
# > The docstring is a phrase ending in a period. It prescribes the function or method's effect as a command ("Do this", "Return that"), not as a description; e.g. don't write "Returns the pathname ...".
#
# > The one-line docstring should NOT be a "signature" reiterating the function/method parameters (which can be obtained by introspection)
#
# ```python
# """Do X and return a list."""
# ``` 

# + [markdown] Collapsed="false"
# ##### Multi-Line Docstring

# + [markdown] Collapsed="false"
# - Summary line, just like single-line docstring
# - Followed by an empty line
# - (more elaborate description)
# - Place closing quotes on a line by themselves

# + [markdown] Collapsed="false"
# ###### reStructured Text (RST)

# + [markdown] Collapsed="false"
# ```
# """Gets and prints the spreadsheet's header columns
#
# :param file_loc: The file location of the spreadsheet
# :type file_loc: str
# :param print_cols: A flag used to print the columns to the console
#     (default is False)
# :type print_cols: bool
# :returns: a list of strings representing the header columns
# :rtype: list
#
# .. note:: blabla
# .. seealso:: blabla
# .. warnings also:: blabla
# .. todo:: blabla
#
# :Example:
#
# here is an example!
# >>> import this
# >>> print(this)
# The Zen of Python
# """
# ```

# + [markdown] Collapsed="false"
# ###### NumPy/SciPy

# + [markdown] Collapsed="false"
# ```
# """Gets and prints the spreadsheet's header columns
#
# Parameters
# ----------
# file_loc : str
#     The file location of the spreadsheet
# print_cols : bool, optional
#     A flag used to print the columns to the console (default is False)
#
# Returns
# -------
# list
#     a list of strings representing the header columns
# """
# ```

# + [markdown] Collapsed="false"
# ##### Why conventions are important

# + [markdown] Collapsed="false"
# Uniform convention allows automated documentation creation via `autodoc` and `apidoc` for `sphinx`

# + [markdown] Collapsed="false"
# https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html

# + [markdown] Collapsed="true"
# #### Documentation

# + [markdown] Collapsed="false"
# > “Code is more often read than written.”
#    — Guido van Rossum
#

# + [markdown] Collapsed="false" endofcell="--"
# ##### Audience:
#
# Users want to know:
# - When to use it
# - How to use it
# - What it does
#
# Developers want to know:
# - Why it is done this way
# - What it depends on
# - What depends on it
# - 
# --

# + [markdown] Collapsed="false"
# > “It doesn’t matter how good your software is, because if the documentation is not good enough, people will not use it.“
#     — Daniele Procida
#

# + [markdown] Collapsed="false"
# > “Code tells you how; Comments tell you why.”
#    — Jeff Atwood (aka Coding Horror)

# + Collapsed="false"


# + [markdown] Collapsed="false"
# ##### Sphinx

# + [markdown] Collapsed="false"
# ```bash
# pip install sphinx
# ```

# + [markdown] Collapsed="false"
# ```
# sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN …]
# ```

# + [markdown] Collapsed="false"
# ```bash
# sphinx-apidoc -o source/build/ ../module_name/
# make html
# ```

# + Collapsed="false"


# + [markdown] Collapsed="true"
# #### PEP8 + people = a lot of different opinions

# + [markdown] Collapsed="false"
# ##### flake8

# + [markdown] Collapsed="false"
# ##### pylint

# + [markdown] Collapsed="false"
# ##### black

# + [markdown] Collapsed="false"
# Runnin in VSCode
#
# Edit settings.json by adding
# ```json
#     "python.formatting.blackArgs": ["--line-length", "160"],
#     "python.formatting.provider": "black",
# ```

# + [markdown] Collapsed="true"
# ### KISS, goodbye to worrying about formatting

# + [markdown] Collapsed="false"
# #### Automatically format to PEP8:
#
# Autoformatting in VSCode: `alt`+`shift`+`f`
#
# In the settings you can select your autoformater, default is `autopep8`

# + [markdown] Collapsed="false"
# ##### autopep8
#
#

# + [markdown] Collapsed="false"
#
# ```json
# "python.formatting.autopep8Args": [
#         "--max-line-length",
#         "160"
#     ],
# "python.formatting.provider": "autopep8",
# ```

# + [markdown] Collapsed="false"
# #### Automatic sort imports
#
# `crtl`+`shift`+`p` $\rightarrow$ `Python Refactor: Sort Imports`
#
# In the settings you can define your import sorter, default is `isort`

# + Collapsed="false"


# + [markdown] Collapsed="true"
# ### What to 

# + Collapsed="false"


# + [markdown] Collapsed="true"
# ### Side note: There are rules for *everything*

# + [markdown] Collapsed="true"
# #### ISO 8601: Data elements and interchange formats - information interchange - Representation of dates and times
#
# There is an official way to write dates and datetimes, this is it, everything else is not according to international standards.
# ```
# 2020-01-28
# 2020-01-28T13:44:24+00.00
# ```

# + Collapsed="false"


# + [markdown] Collapsed="true"
# ## Design Patterns

# + [markdown] Collapsed="true"
# ### Why are they important

# + [markdown] Collapsed="false"
# <img src=https://i.redd.it/rskneik2r4h41.jpg width=480>

# + [markdown] Collapsed="false"
# They are widely used, therefore widely read, meaning you should know them.

# + [markdown] Collapsed="false"
# #### What is a Design Pattern?

# + [markdown] Collapsed="false"
# > "Each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice"

# + Collapsed="false"


# + Collapsed="false"


# + [markdown] Collapsed="true"
# ## Code Analyzer

# + [markdown] Collapsed="false"
# ### Static Code Analysis with `pyan3`
# https://github.com/Technologicat/pyan
#
#

# + [markdown] Collapsed="false"
# <img src=https://raw.githubusercontent.com/Technologicat/pyan/master/graph0.png width=640>

# + [markdown] Collapsed="false"
# ```bash
# pip install pyan3
# ```

# + [markdown] Collapsed="false"
# ```bash
# pyan3 *.py --uses --no-defines --colored --grouped --annotated --dot >myuses.dot
# ```

# + [markdown] Collapsed="false"
# ### Dependency analysis with `pydeps`
# https://github.com/thebjorn/pydeps

# + [markdown] Collapsed="false"
# <img src="https://raw.githubusercontent.com/thebjorn/pydeps/master/docs/_static/pydeps-18-bacon4-cluster-max1000.svg?sanitize=true" width=640>

# + Collapsed="false"


# + [markdown] Collapsed="false"
# ### Call Graph Creation with `pycallgraph2`
# https://github.com/daneads/pycallgraph2

# + Collapsed="false"


# + [markdown] Collapsed="true"
# ## Functional Programming

# + [markdown] Collapsed="false"
# - Object-Oriented Programming (OOP) shortcomings
# - Composition
# - Immutability
# - Pure functions (no side-effects)
# - Functional Programming in Python
#   - Lambda functions
#   - Maps

# + Collapsed="false"


# + [markdown] Collapsed="false"
# ### Introduction to Programming Styles
#
# "Most programming languages are ***procedural***: programs are lists of instructions that tell the computer what to do with the program’s input. C, Pascal, and even Unix shells are procedural languages."
#
# "In ***declarative*** languages, you write a specification that describes the problem to be solved, and the language implementation figures out how to perform the computation efficiently. SQL is the declarative language you’re most likely to be familiar with; a SQL query describes the data set you want to retrieve, and the SQL engine decides whether to scan tables or use indexes, which subclauses should be performed first, etc."
#
# "***Object-oriented*** programs manipulate collections of objects. Objects have internal state and support methods that query or modify this internal state in some way. Smalltalk and Java are object-oriented languages. C++ and Python are languages that support object-oriented programming, but don’t force the use of object-oriented features."
#
# "***Functional*** programming decomposes a problem into a set of functions. Ideally, functions only take inputs and produce outputs, and don’t have any internal state that affects the output produced for a given input. Well-known functional languages include the ML family (Standard ML, OCaml, and other variants) and Haskell."
#
# (https://docs.python.org/3/howto/functional.html)

# + [markdown] Collapsed="false"
# Procedural Pogramming languages are very close to hardware as they describe the list of instructions in order, like C or Fortran and were mostly developed in the late 50s until early 1970s.
#
# The major declarative language still used today is SQL which we will cover in a future session on Databases (developed in the 70s-80s). 
#
# Object-oriented programming focus on deconstructing the program into objects, instances, and performing actions on these using member functions such as Java.
#
# Functional programming decomposes the problem into functions with inputs and outputs that get composed to process information.

# + [markdown] Collapsed="false"
# Most modern programming languages like Python and C++ are multi-paradigm, and most big projects use multiple programming styles for different parts: GUIs are often simpler to describe as objects such as a slider that has methods that can be performed on it, while data processing is often easier to be described as various functions that are applied to the data.

# + [markdown] Collapsed="false"
# That is why functional programming is important to data science - it is the preferred paradigm for processing data!

# + Collapsed="false"


# + [markdown] Collapsed="false"
# ### Pure Functions in Python

# + [markdown] Collapsed="false"
# > Pure functions have no side effects. 
#
# This means, functions map inputs to outputs and access nothing outside of the inputs. 

# + [markdown] Collapsed="false"
# One common problem in Python is the global name lookup:

# + Collapsed="false"
a = 1
b = 2
def impure(a0, b0):
    return a+b

print(impure(a,b))
a = 2
print(impure(a,b))
print(impure(5,5))

# + [markdown] Collapsed="false"
# This bug in code is caused from the global name lookup that you **cannot** deactivate in Python easily.

# + [markdown] Collapsed="false"
# Luckily, we're not the first one encountering this issue.
#
# Instead of prohibiting global lookups, we can patch the global namespace within each function with an empty namespace.
#
# Or even better, with just the namespace of imported modules, thereby allowing execution of code without needing to re-import modules.

# + [markdown] Collapsed="false"
# One such solution is:

# + Collapsed="false"
# https://gist.github.com/ax3l/59d92c6e1edefcef85ac2540eb056da3
import types
def imports():
    for name, val in globals().items():
        # module imports
        if isinstance(val, types.ModuleType):
            yield name, val
        # functions / callables
        if hasattr(val, '__call__'):
            yield name, val

noglobal = lambda fn: types.FunctionType(fn.__code__, dict(imports()))

# + Collapsed="false"
a = 1
b = 1
@noglobal
def impure(a0,b0):
    return a+b

impure(1,2)

# + [markdown] Collapsed="false"
# While it does not cause an error upon definition, it does cause an error upon calling it, instead of letting it pass with a wrong value.

# + [markdown] Collapsed="false"
# ### Functional Programming in Python

# + [markdown] Collapsed="false"
# #### Lambda

# + Collapsed="false"
double = lambda x: x*2
double(5)

# + [markdown] Collapsed="false"
# #### Map

# + [markdown] Collapsed="false"
# `map(function, iterable)` applies a function to every element in an iterable and returns an iterable

# + Collapsed="false"
map(lambda x: x*x, [1,2,3,4,5])

# + Collapsed="false"
list(map(lambda x: x*x, [1,2,3,4,5]))

# + [markdown] Collapsed="false"
# #### Filter

# + [markdown] Collapsed="false"
# `filter(function, iterable)` applies a True/False function to every element in an iterable and returns an iterable

# + Collapsed="false"
filter(lambda x: x%2, [1,2,3,4,5])

# + Collapsed="false"
list(filter(lambda x: x%2, [1,2,3,4,5]))

# + [markdown] Collapsed="false"
# #### List & Dictionary Comprehension

# + Collapsed="false"
[i*2 for i in range(0,5)]

# + Collapsed="false"
{i:i*2 for i in range(0,5)}

# + [markdown] Collapsed="true"
# ## Module Architecture

# + [markdown] Collapsed="false"
# - `__init__` files
# - src/ folder
# - bin/ folder
# - main() and `__main__`
# - README.md
# - Changelog.md
# - requirements
# - License files (and Licensing cheatsheet)
# - Python Module Structure

# + [markdown] Collapsed="true"
# ### Package Structure
#
# ```
# package-git
# |-> LICENSE.md
# |-> README.md
# |-> requirements.txt
# |-> setup.py
# |-> setup.cfg
# |-> .pylintrc
# |-> .gitignore
# |-> package_name
# |   |-> __init__.py
# |   |-> core_code.py
# |   |-> io
# |   |   |- __init__.py
# |   |   |-> data_loader.py
# |   |   |-> data_saver.py
# |   |-> processing
# |   |   |-> __init__.py
# |   |   |-> core.py
# |   |-> data
# |   |   |-> initial_data_set.csv
# |-> docs
# |   |-> package_name.md
# |   |-> io.md
# |   |-> processing.md
# |   |-> data.md
# |-> tests
# |   |-> core_code.py
# |   |-> io
# |   |   |-> data_loader.py
# |   |   |-> data_saver.py
# |   |-> processing
# |   |   |-> core.py
# ```

# + [markdown] Collapsed="false"
# - Each folder is a `(sub)package`
# - Each package has an `__init__.py`
# - `tests` mirrors the main package 1:1
# - `docs` mirrors the main package closely too

# + [markdown] Collapsed="true"
# ### PEP8 conform module level dunder names
#
# "Module level "dunders" (i.e. names with two leading and two trailing underscores) such as `__all__`, `__author__`, `__version__`, etc. should be placed after the module docstring but before any import statements except `from __future__` imports. Python mandates that future-imports must appear in the module before any other code except docstrings:" -- PEP8
#
# ```python
# """This is the example module.
#
# This module does stuff.
# """
#
# from __future__ import barry_as_FLUFL
#
# __all__ = ['a', 'b', 'c']
# __version__ = '0.1'
# __author__ = 'Cardinal Biggles'
#
# import os
# import sys
# ```

# + [markdown] Collapsed="false"
# ### `__init__` files

# + [markdown] Collapsed="false"
# Import the functions that should be used by other modules that import this module

# + Collapsed="false"


# + Collapsed="false"


# + Collapsed="false"


# + Collapsed="false"


# + [markdown] Collapsed="false"
# ## Documentation

# + [markdown] Collapsed="false"
# <img src="https://preview.redd.it/08sz26e91k841.jpg?width=640&crop=smart&auto=webp&s=4cbb04afe0b73ad80c6d8b74b509024f3201405e" width=400>

# + [markdown] Collapsed="false"
# ### Sphinx

# + [markdown] Collapsed="false"
# <img src="https://i.redd.it/d5x18rtcfof31.png" width=400 />

# + [markdown] Collapsed="false"
# Installation:
# ```bash
# conda install sphinx
# ```

# + [markdown] Collapsed="false"
# Sample Practice
# ```bash
# # # mkdir docs
# # # cd docs 
# ```
# ```bash
# sphinx-quickstart
# ```
# ```bash
# make html
# ```

# + [markdown] Collapsed="false"
# in GitHub under Hooks, you can definte ReadTheDocs as a hook upon commit, meaning it will update your documentation automatically when committing to your repository

# + [markdown] Collapsed="false"
#

# + Collapsed="false"


# + [markdown] Collapsed="false"
# ### How to get listed on PIP / PyPI (Python Package Index)

# + Collapsed="false"


# + [markdown] Collapsed="false"
# ### How to get listed on Conda

# + Collapsed="false"


# + [markdown] Collapsed="false"
# Why do you have to make it so complicated?
#
# https://www.youtube.com/watch?v=PcJeHNWOoWk

# + Collapsed="false"


# + Collapsed="false"


# + Collapsed="false"


# + [markdown] Collapsed="true"
# ## Code Maintenance

# + [markdown] Collapsed="false"
# ### Support

# + [markdown] Collapsed="false"
# 1. Make simple rules for support.
# 2. Don't support unsupported packages! (looking at you Python 2)
# 3. Only support the last X versions
# 4. Update regularly

# + [markdown] Collapsed="false"
# ### Preventing code abandonment

# + [markdown] Collapsed="false"
# #### Cause for code abandonment

# + [markdown] Collapsed="false"
# 1. Code is illegible
#    - Comments
#    - Documentation
#    - Tests
# 2. Code is outdated
#    - Update dependencies regularly (e.g. 1st of every month)
# 3. Code is cumbersomly written
#    - Take advantage of new features (only support new versions)
#    - Define code styling
#    - Define code design pattern
#    - Keep things shallow (at most 5 levels deep)
#

# + [markdown] Collapsed="true"
# ## Command Line Interfaces

# + [markdown] Collapsed="false"
# Most popular tool these days: <a href="https://github.com/pallets/click">**Click**</a>
#
# ```bash
# conda install click
# pip install click
# ```
#

# + [markdown] Collapsed="false"
# Click is developed as parts of <a href="palletsprojects.com/">pallets</a>, who also develop <a href="https://github.com/pallets/flask">Flask</a>

# + [markdown] Collapsed="true"
# ### Minimal Example

# + [markdown] Collapsed="false"
# ```python
# import click
#
#
# @click.command()
# def hello():
#     click.echo('Hello World')
#
# if __name__ == "__main__":
#     hello()
# ```

# + [markdown] Collapsed="false"
# ```bash
# > python test.py
# Hello World
# ```

# + [markdown] Collapsed="false"
# ```bash
# > python test.py --help
# Usage: click_test.py [OPTIONS]
#
# Options:
#   --help  Show this message and exit.
# ```

# + [markdown] Collapsed="false"
# `click.echo` is used to ensure:
# - works for `Python 2` and `Python 3`
# - prevents `UnicodeError`
# - supports ANSI Colors
# If you do not want these features, you can use `print()`

# + [markdown] Collapsed="true"
# ### Adding Commands

# + [markdown] Collapsed="false"
# `click.group`s wrap commands as one, allowing arbitrarily nesting.

# + [markdown] Collapsed="false"
# ```python
# @click.group()
# def cli():
#     pass
#
# @click.command()
# def initdb():
#     click.echo('Initialized the database')
#
# @click.command()
# def dropdb():
#     click.echo('Dropped the database')
#
# cli.add_command(initdb)
# cli.add_command(dropdb)
#
# if __name__ == "__main__":
#     cli()
# ```

# + [markdown] Collapsed="false"
# Commandas are activated using:
# ```bash
# > python test.py initdb
# Initialized the database
# ```
#
# ```bash
# > python test.py --help
# Usage: click_test.py [OPTIONS] COMMAND [ARGS]...
#
#   --help  Show this message and exit.
#
# Commands:
#   dropdb
#   initdb
# ```

# + [markdown] Collapsed="true"
# ### Adding Parameters

# + [markdown] Collapsed="false"
# Commands can have two types of parameters:
# - `argument`s: positional arguments of python fucntions 
# - `option`s: key-value arguments of python functions

# + [markdown] Collapsed="false"
# ```python
# import click
#
#
# @click.command()
# @click.option('--count', default=1, help='number of greetings')
# @click.argument('name')
# def hello(count, name):
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
# if __name__ == "__main__":
#     hello()
# ```

# + [markdown] Collapsed="false"
# ```bash
# > python test.py --help
# Usage: click_test.py [OPTIONS] NAME
#
# Options:
#   --count INTEGER  number of greetings
#   --help           Show this message and exit.
# ```
#
# ```bash
# python test.py Robin
# Hello Robin!
# ```
#
# ```bash
# python test.py Robin --count 3
# Hello Robin!
# Hello Robin!
# Hello Robin!
# ```

# + [markdown] Collapsed="true"
# ### More complex Options

# + [markdown] Collapsed="false"
# https://click.palletsprojects.com/en/7.x/options/

# + [markdown] Collapsed="false"
# Options allow for:
# - specify variable name (`"--n", "N"` for fixing case in-sensitivity)
# - define aliast (`"--n", "-n"`)
# - required flag (`required=True`)
# - default values (`default=1`)
# - type limiting and conversion (`type=int` or even `type=(int, int)`)
# - multi-value arguments (`nargs=2` or `multiple=True` for unspecified number of args)
# - binary flag (`is_flag=True, flag_value=True` or `--shout/--no-shout` with `true/false`)
# - choice input (`type=click.Choice(['MD5', 'SHA1'], case_sensitive=False)`)
# - allow promted input (`prompt="Enter Name"` and for confirmation `confirmation_prompt=True`)
# - range limitations (`type=click.IntRange(0, 100)`)
# - iteration counting (`count=True` counts multiple invokations e.g. `-vvv` for `v=3`)
# - password prompts (`hinde_input=True`)
# - callbacks for validation or other (`callback=print_version`)
# - displaying defaults (`show_defaults=True`)
# - hide from help function (`hidden=True`)
# - and more...

# + [markdown] Collapsed="false"
# ```python
# @click.option("--c1", default=1, type=click.FloatRange(0, None), show_default=True,
#               help="Scale between: hydrodynamic: 0.1, transition: 1, adiabatic: 5")
# ```

# + [markdown] Collapsed="true"
# ### Real world example

# + [markdown] Collapsed="false"
# <img src="img/click_example_code.jpg" />

# + [markdown] Collapsed="false"
# <img src="img/click_example_help.jpg" />

# + [markdown] Collapsed="false"
# ### Setuptools Integration

# + [markdown] Collapsed="false"
# Benefits:
# - Executable wrapping with necessary requirements into a virtual environment
# - Windows and Unix executables

# + [markdown] Collapsed="false"
#

# + [markdown] Collapsed="false"
#

# + Collapsed="false"


# + Collapsed="false"


# + [markdown] Collapsed="false"
# ```python
# import click
#
# @click.command()
# @click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name",
#               help="The person to greet.")
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for _ in range(count):
#         click.echo("Hello, %s!" % name)
#
# if __name__ == '__main__':
#     hello()
# ```

# + Collapsed="false"


# + Collapsed="false"

