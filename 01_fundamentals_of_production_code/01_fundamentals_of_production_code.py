# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] slideshow={"slide_type": "slide"}
# # Fundamentals of Production Code

# + [markdown] slideshow={"slide_type": "fragment"}
# This presentation is written by @the-rccg for the Practical Data Science for Researchers Course for the Helmholtz Graduate School for Data Science in Munich (MUDS), Spring 2020.

# + [markdown] slideshow={"slide_type": "slide"}
# ## Overview: Fundamentals of Production Code
#
# - Workflow Organization (Robin)
# - Environments  (Robin)
# - Code Style  (Robin)
# - Design Patterns  (Robin)
# - Thinking Functionally  (Robin)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Some Quick Questions before starting the first line in your project

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Users

# + [markdown] slideshow={"slide_type": "fragment"}
# Who is the User?
# - Just yourself?
# - One Colleague?
# - People in your office?
# - Entire research group?
# - Your department?
# - External collaborators?
# - Unconnected users?

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Lifetime

# + [markdown] slideshow={"slide_type": "fragment"}
# How long should this code last (in time)?
# - I'll delete this file at the end of the day
# - I'll delete this file at the end of the week
# - I won't need this file, but will keep it forever to look at later
# - I'll come back to this in a few weeks
# - This project should be used for the next year
# - This project should last a few years
# - The code should be taken over by another person
# - This code should last a long time and be maintained by another person
# - This code should last a long time and be maintained by volunteer developers

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Breadth

# + [markdown] slideshow={"slide_type": "fragment"}
# How broad should this code be (in terms of users)?
# - Just people who are identical copies of myself
# - Anyone doing a PhD in this exact subfield
# - Anyone doing a PhD in this general field
# - Anyone doing a PhD in this subject
# - Any Masters degree
# - Anyone with a bachelors education
# - Even people from different fields should be able to use this code

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Takeaways

# + [markdown] slideshow={"slide_type": "fragment"}
# Whatever you decide in the previous questions, go one further in each direction.
#
# After you spent the time, you will want to share it more widely. Trust me.

# + [markdown] slideshow={"slide_type": "fragment"}
# Open Science = Open Code
#
# but, open code is useless if no one can read it

# + [markdown] slideshow={"slide_type": "fragment"}
# Peer Review means that at least your peer has to be able to read and understand your code in minimal time. If they cant, you might as well have made up your results.

# + [markdown] Collapsed="true" toc-hr-collapsed=true slideshow={"slide_type": "slide"}
# ## Workflow Organization
# Thank you to Nicole Carlson and her talk at PyData Austin 2019 (https://www.youtube.com/watch?v=2v9uwedgBxU)Come up with a process that works for the team

# + [markdown] slideshow={"slide_type": "fragment"}
# Question:
# - How does your team workflow look like?

# + [markdown] slideshow={"slide_type": "fragment"}
# Come up with a process that works for the team

# + [markdown] slideshow={"slide_type": "fragment"}
# Strong opinions + respectful conversations = better results

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Overview

# + [markdown] slideshow={"slide_type": "fragment"}
# 1. Sprinting
# 2. Tracking
# 3. Sharing
# 4. Reviewing

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Sprint planning
# - each person comes up with their own tasks
# - group discusses tasks  +  estimate times
# - R&D or Literature Review tasks are timeboxed
# - Long-term project planning happens aoutside of the meeting
# - Code Reviews are assigned after the meeting

# + [markdown] slideshow={"slide_type": "fragment"}
# Keep in mind, studies across various fields come to the rough estimate that we **underestimate the time we need by 40% on average!**

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Central place to track your work: 
# - Overview: What is each person working on?
# - Ordering: What will you work on next?
# - Timeline: What is the overall outline of your project
# - Ideas: What are potential future projects/follow-ups?
# - Collaboration: What requests have you gotten from other teams?

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Full Team Trackers:
# - [Asana](https://www.asana.com/)
# - [Trello](https://www.trello.com/)
# - [Jira](https://www.atlassian.com/software/jira/)
#
#
# ##### Simple Trackers:
# - [Todoist](https://www.todoist.com)
# - [GitHub](https://www.github.com)
#
# ##### Not Trackers:
# - [Slack](https://www.slack.com)
# - E-Mail

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Common Utilities Repo
# People will face the same challenges, <u>***especially new people***</u>. Keep solutions in one place.

# + [markdown] slideshow={"slide_type": "fragment"}
# - Database
#   - common queries, instructions, etc.
#   - descriptions for each
#   - how to acces it

# + [markdown] slideshow={"slide_type": "fragment"}
# - Data Processing
#   - transformations
#   - common tools and how to use them

# + [markdown] slideshow={"slide_type": "fragment"}
# - Helpers
#   - logging
#   - unittesting
#   - visualizations

# + [markdown] slideshow={"slide_type": "fragment"}
# - Coding Standards
#   - PEP8
#   - linter configuration file

# + [markdown] slideshow={"slide_type": "fragment"}
# - Development Flow
#   - PR Checklist
#   - CI Pipeline
#   - Review process description

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Code Review Process
#
# - Git hierarchies: master -> develop -> feature
# - How should Pull Requests (PR) be prepared?
#   - Unit Tests
#   - Documentation
# - Who should review the code?
# - What are the responsibilities of reviewer?
#   - Should they check math?
#   - Should they run tests locally for dependency checks?
#   - Should they check performance?

# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "subslide"}
# ### Data Science to production
#
# - sketch stage: data -> notebook -> insight
# - production stage: data -> API -> insight


# + [markdown] slideshow={"slide_type": "subslide"}
# #### Next Level: Web-framework for open science access
#
# Frameworks:
# - Flask (recommended as it is the lightest)
# - Django
# - Bottle
# - Falcon
#
# Further features to consider
# - Locust (Load Testing)

# + [markdown] Collapsed="true" toc-hr-collapsed=true slideshow={"slide_type": "slide"}
# ## Overview: Setting Up the Environment
#
# - virtual environments
# - vscode for working on remote server
# - jupyter for working on remote server

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Virtual Environments

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Creating an Environment (env) to update to Python 3.8

# + [markdown] slideshow={"slide_type": "fragment"}
# List current environments:
# ```bash
# conda env list
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Export current env:
# ```bash
# conda list --explicit > current_env.txt
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Create new env for Python=3.8:
# ```bash
# conda create --name py38 python=3.8
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Switch environment:
# ```bash
# activate py38
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Simply install what you need:
# ```bash
# conda install matplotlib jupyter tensorflow dask numba
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Registering Environments as Kernels in Jupyter

# + [markdown] slideshow={"slide_type": "fragment"}
# ```bash
# conda activate py38
# conda install ipykernel
# python -m ipykernel install --user --name=py38
# conda activate base
# jupyter lab
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src=../img/jupyter_environments.png />

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Other Environments
#
# You might have heard or read about the Python Virtual Environments, however, the Conda version allows for a higher encapsulation of entirely independent Python installations for each environment, as well as other tools.
#
# This works similarly to how Conda provides a higher abstraction and utility with respect to modules than PIP does, as for example its dependency resolution.

# + [markdown] slideshow={"slide_type": "subslide"}
# ### IDEs

# + [markdown] slideshow={"slide_type": "subslide"}
# #### That friend

# + [markdown] slideshow={"slide_type": "fragment"}
# There is always THAT colleague who says anyone who isn't using VI/emacs isn't a proper developer - don't ever listen to them.

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://preview.redd.it/dcuj4sradth51.jpg?width=960&crop=smart&auto=webp&s=0b36f0b69c9cf127b5f632de5208278323595de9" width=480>

# + [markdown] slideshow={"slide_type": "subslide"}
# #### IDE Options

# + [markdown] slideshow={"slide_type": "fragment"}
# - [VSCode](https://code.visualstudio.com/)
#   - Multi-Language support
#   - Extensible
#   - Open Source
#   - Very light weight
#   - Great support and stability thanks to Microsoft financing

# + [markdown] slideshow={"slide_type": "fragment"}
# - [PyCharm](https://www.jetbrains.com/pycharm/)
#   - Free for students
#   - Very heavy weight
# - [Spyder](https://www.spyder-ide.org/)
#   - Great for scripting/Analysis
#   - Open Source
# - [Atom](https://www.atom.io/)
#   - Extensible
#   - Open Source

# + [markdown] slideshow={"slide_type": "subslide"}
# ### [VSCode](https://code.visualstudio.com/) for working on Remote Server

# + [markdown] slideshow={"slide_type": "fragment"}
# Why it's useful: (non comprehensive list)
#
# - Write code directly on the server you're deploying on with full IDE capability
# - All benefits of your locally installed Extensions and Settings for the remote server
# - Simply drag-and-drop for moving files

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Getting the Extension
#
# 1. `ctrl/cmd + shift + p` opens the console in run command mode indicated by `>`
# 2. run `Extensions: install Extensions`
# 3. install `Remote - SSH`
# 4. Now you have a new icon in the footer: 
#
#    <img width=300, height=15, src="../img/ssh-remote.png">
#    
# 6. `Remote-SSH: Connect to Host...`
# 7. `Add New SSH Host...`
#

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Jupyter for working on Remote Server

# + [markdown] slideshow={"slide_type": "fragment"}
# 1. Connect to remote server
# 2. Start Jupyter server on a free port
# 3. Tunnel the port to your machine to work as if it was local

# + [markdown] slideshow={"slide_type": "fragment"}
# Reverse Tunneling 
# ```bash
# ssh usernam@host.de -L remote_port:local_host:local_port
# ```
# Example:
# ```bash
# ssh rgreif@host.mu-ds.de -L 8889:localhost:8888
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Flags explained

# + [markdown] slideshow={"slide_type": "fragment"}
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
# + [markdown] Collapsed="true" toc-hr-collapsed=true slideshow={"slide_type": "slide"}
# ## Code Style

# + [markdown] slideshow={"slide_type": "fragment"}
# - The Zen of Python
# - PEP8
# - PyLint
# - Flake8
# - How to select which linting rules to use?
#     - Hierarchical structure of: Necessary, Optional, Not needed

# + [markdown] slideshow={"slide_type": "subslide"}
# ### The Zen of Python
#
# The "guiding principles" of how to write Python code, formulated in 1999 and published as **Python Enhancement Proposal (PEP)** 20.

# + slideshow={"slide_type": "fragment"}
import this

# + [markdown] slideshow={"slide_type": "subslide"}
# ### So what does this mean?

# + [markdown] slideshow={"slide_type": "subslide"}
# #### ***Explicit is better than implicit.***

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# from some_file import custom_object
#
# custom_object().run()
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# import  some_file as fncs
#
# data = fncs.load_data('data.csv')
# proc_data = fncs.process_data(data)
# print(summarize_data(proc_data))
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# #### ***Simple is better than complex.***
#

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# def make_complex(*args):
#     x, y = args
#     return dict(**locals())
# ```
#
# ```python
# def make_complex(x, y):
#     return {'x': x, 'y': y}
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# #### ***Flat is better than nested.***
#

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Original Example

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# center_slices = tuple([(slice(1, -1) if i == ax else (slice(1, -1)) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# upper_slices = tuple([(slice(2, None) if i == ax else (slice(1, -1)) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# lower_slices = tuple([(slice(-2) if i == ax else (slice(1, -1)) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Making sense of original

# + [markdown] slideshow={"slide_type": "slide"}
# ```python
# # (c)enter (u)pper (l)ower
# c_slices = tuple([(slice(1, -1)   if i == ax else slice(1, -1) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# u_slices = tuple([(slice(2, None) if i == ax else slice(1, -1) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# l_slices = tuple([(slice(-2)      if i == ax else slice(1, -1) if _contains_axis(axes, i, rank) else slice(None)) for i in dims])
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Denesting step 1

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Final denesting

# + [markdown] slideshow={"slide_type": "slide"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# #### ***Readability counts.***
#
#

# + [markdown] slideshow={"slide_type": "fragment"}
# Code is written once, but read a lot more by people with in depth less knowledge.

# + [markdown] slideshow={"slide_type": "subslide"}
# #### ***Special cases aren't special enough to break the rules.***
#
#

# + [markdown] slideshow={"slide_type": "fragment"}
# It might be tempting to do it, but breaking conventions make things harder to understand.

# + [markdown] slideshow={"slide_type": "subslide"}
# #### ***If the implementation is hard to explain, it's a bad idea.***
#

# + [markdown] slideshow={"slide_type": "fragment"}
# Your code lives on after you leave. If you struggle to explain it, the next person has no chance to understand it. Your code will be THAT code. 

# + [markdown] slideshow={"slide_type": "subslide"}
# #### ***Namespaces are one honking great idea -- let's do more of those!***

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# from phi.flow import *
# ```
# vs.
# ```python
# from phi.flow import physics, smoke
# ```

# + [markdown] slideshow={"slide_type": "slide"}
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

# + [markdown] slideshow={"slide_type": "slide"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### From Meetings
#
# "I just want to make the examples as short as possible so people can see how easy it is to use"
# -- author of a 2 line example (`import object; object.run()`)
#
#

# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
# There are very useful tools that combine these into one, namely Sphinx and the ReadTheDocs implementation you are probably familiar with.


# + [markdown] slideshow={"slide_type": "subslide"}
# ### Whats the difference between good code and bad code?

# + [markdown] slideshow={"slide_type": "fragment"}
# Good code is code ***I*** wrote.
#
# Bad code is code ***you*** wrote.

# + [markdown] slideshow={"slide_type": "fragment"}
# Well, but how do we agree on that **this** code is good code?

# + [markdown] slideshow={"slide_type": "fragment"}
# Welcome to Code Style and Style Guides! 

# + [markdown] slideshow={"slide_type": "subslide"}
# ### PEP 8

# + [markdown] slideshow={"slide_type": "fragment"}
# > “Code is more often read than written.”
#    — Guido van Rossum
#

# + [markdown] slideshow={"slide_type": "fragment"}
# You could read all books in l337 sp34k, but let's be honest, that would be a pain.

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Coworker is asking to see your code? 
#
# <img src="https://preview.redd.it/hk54ti5n6tk11.png?width=640&crop=smart&auto=webp&s=6b84e81dae311d0f055a43ee5dfda6f68d253e47" width=300>

# + [markdown] slideshow={"slide_type": "fragment"}
# So, lets look at the rules how code should look like to build trust in your code

# + [markdown] slideshow={"slide_type": "subslide"}
# #### How code should look like:
#
# 1. Only one statement per line
# 2. All imports on top
# 3. Imports grouped by global/local, ordered by depth then alphabetically
# 4. Between global and local imports: 1 blanck line
# 5. After imports: 1 blanck line
# 7. Before/After functions: 1 blanck line
# 8. Before/After classes: 2 blanck lines
# 9. End of file: 1 blanck line
# 10. Indentation: 4 spaces / level

# + [markdown] slideshow={"slide_type": "fragment"}
# For the full list, see: https://www.python.org/dev/peps/pep-0008/

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Naming Styles

# + [markdown] slideshow={"slide_type": "fragment"}
# | Name               | Example                    |
# |--------------------|----------------------------|
# | Upper Camel Case   | ThisIsCapitalCamelCase     |
# | Lower Camel Case   | thisIsLowerCamelCase       |
# | Snake Case         | this_is_snake_case         |
# | Capital Snake Case | THIS_IS_CAPITAL_SNAKE_CASE |

# + [markdown] slideshow={"slide_type": "fragment"}
# Forbidden/Reserved conventions in Python:
#
# - ```period.separated```
# - ```kebab-case```

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Which to use for what?

# + [markdown] slideshow={"slide_type": "fragment"}
# | Object    | Naming Style     |
# |-----------|------------------|
# | Variables | `snake_case`       |
# | Constants | `CAPITAL_SNAKE_CASE`       |
# | Classes   | `CapitalCamelCase`  |
# | Functions | `snake_case`       |
# | Packages  | `alllowercase`    |

# + [markdown] slideshow={"slide_type": "fragment"}
# | Object                        | Naming Style        | Resulting Behavior                                                 |
# |-------------------------------|---------------------|--------------------------------------------------------------------|
# | Private Variables/Functions   | `_snake_case`       | Not imported with `*`, linter will complain if accessed externally |
# | Private Classes               | `_CapitalCamel`     | Not imported with `*`, linter will complain if accessed externally |
# | Python Keyword Conflicts      | `trailing_`         | Nothing special |
# | Private Attributes of Classes | `__double_leading`  | invokes name mangling (inside class FooBar, `__bar` becomes `_FooBat__boo`) |
# | magic objects/attributes      | `__double_double__` | living in user-controlled namespaces e.g. __init__, __import__, __file__ |
#

# + [markdown] slideshow={"slide_type": "fragment"}
# For more on naming conventions see: https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Side Note: naming conventions for pretty code

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + slideshow={"slide_type": "fragment"}
Useful equal sized words:

``` 
first  or  begin  or  init
final  or  final  or  last

read  or  open
save  or  save

exec 
wait
```

# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
# If you have more useful examples, please let us know!


# + slideshow={"slide_type": "subslide"}
#### PEP8 is not definite

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Indentation

# + [markdown] slideshow={"slide_type": "slide"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Continuing lines

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# if flag.is_data_bound and \
#         flag.propagates(_PROPAGATOR.RESAMPLE) and \
#         flag.is_applicable(resulting_rank, data_field.component_count):
#     flags.append(flag)
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# if (flag.is_data_bound
#         and flag.propagates(_PROPAGATOR.RESAMPLE)
#         and flag.is_applicable(resulting_rank, data_field.component_count):
#     flags.append(flag)
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# if (flag.is_data_bound and flag.propagates(_PROPAGATOR.RESAMPLE)
#                        and flag.is_applicable(resulting_rank, data_field.component_count):
#     flags.append(flag)
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Real-world Example

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### List comprehension or mapping?

# + slideshow={"slide_type": "fragment"}
f2 = [_contains_axis(axes, i, rank) for i in dims]
f2 = list(map(lambda i: _contains_axis(axes, i, rank), dims))


# + [markdown] slideshow={"slide_type": "subslide"}
# ###### Explicit via else-if, or mapping with dictionaries?

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
def _pad_mode(extrapolation):
    if extrapolation == 'periodic':
        return 'wrap'
    elif extrapolation == 'boundary':
        return 'replicate'
    else:
        return extrapolation


# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
extrapolation_map = {
    'periodic': 'wrap',
    'boundary': 'replicate',
    'constant': 'constant'
} 

extrapolation_map[extrapolation]


# + [markdown] slideshow={"slide_type": "subslide"}
# #### Useful practices outside of PEP8

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Context Managers

# + [markdown] slideshow={"slide_type": "slide"}
# ```python
# # Non-Pythonic
# resource = allocate()
# try:
#     resource.use()
# finally:
#     resource.deallocate()
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ```python
# # Pythonic!
# with allocate_resource() as resource:
#     resource.use()
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Properties (Setters & Getters)
#
# (or how to spot a Java Developer)

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# class Team:
#     _members = ['Jan', 'Viliam', 'Ilya']
#
#     @property
#     def members(self):
#         return list(self._members)
#
#     @members.setter
#     def members(self, value):
#         raise AttributeError('This team is too precious to touch!')
#
# >>> team = Team()
# >>> print(team.members)
# ['Jan', 'Viliam', 'Ilya']
# >>> team.members = []
# AttributeError('This team is too precious to touch!',)
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Intrinsic Decorators

# + [markdown] slideshow={"slide_type": "fragment"}
# Speaking of decorators, Python provides a ton of useful decorators!
#
# fore example: `Least-Recently-Used Cache` to reuse previous computations automatically
# ```python
# @lru_cache
# def count_vowels(sentence):
#     sentence = sentence.casefold()
#     return sum(sentence.count(vowel) for vowel in 'aeiou')
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Duck Typing

# + [markdown] slideshow={"slide_type": "fragment"}
# If it walks like a duck, and quacks like a duck, then it must be a duck.

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# class Duck:
#     def fly(self):
#         print("Duck flying")
#
# class Sparrow:
#     def fly(self):
#         print("Sparrow flying")
#
# class Whale:
#     def swim(self):
#         print("Whale swimming")
#
# for animal in Duck(), Sparrow(), Whale():
#     animal.fly()
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Goose Typing

# + [markdown] slideshow={"slide_type": "fragment"}
# Checking types versus abstract data types. Allows inference based on member functions, as well as inheritance.

# + [markdown] slideshow={"slide_type": "slide"}
# ```python
# # Non-Pythonic
# if not isinstance(x, list):
#     raise ApplicationError('Python list type is expected')
# ```
#
# ```python
# # Pythonic!
# if not isinstance(x, collections.abc.MutableSequence):
#     raise ApplicationError('A sequence type is expected')
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### ABC PEP

# + [markdown] slideshow={"slide_type": "fragment"}
# [Abstract Base Clases PEP 3119](https://www.python.org/dev/peps/pep-3119/)

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Type Hinting

# + slideshow={"slide_type": "fragment"}
def greeting(name: str) -> str:
    return 'Hello ' + name


# + [markdown] slideshow={"slide_type": "fragment"}
# You can use aliases

# + slideshow={"slide_type": "fragment"}
Url = str

def retry(url: Url, retry_count: int) -> None: 
    return 0


# + [markdown] slideshow={"slide_type": "fragment"}
# Can be composed

# + slideshow={"slide_type": "fragment"}
from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)
Vector = Iterable[Tuple[T, T]]

def inproduct(v: Vector[T]) -> T:
    return sum(x*y for x, y in v)


# + [markdown] slideshow={"slide_type": "fragment"}
# Annotations to functions are available through the `__annotations__` dictionary

# + slideshow={"slide_type": "fragment"}
greeting.__annotations__

# + slideshow={"slide_type": "fragment"}
inproduct.__annotations__

# + [markdown] slideshow={"slide_type": "fragment"}
# See https://www.python.org/dev/peps/pep-0484/

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Futher Reading
#
# For more, see: https://access.redhat.com/blogs/766093/posts/2802001

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Thou shall comment (but, like, not unecessarily)

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://preview.redd.it/vs35fh1ruef51.jpg?width=640&crop=smart&auto=webp&s=3e1dd46e210f0499b9ac87187eefbde912bebdeb" width=320>

# + [markdown] slideshow={"slide_type": "fragment"}
# - at least 2 spaces to code
# - start with #
# - followed by a single space

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Example

# + [markdown] slideshow={"slide_type": "fragment"}
# Inline comments are unnecessary and in fact distracting if they state the obvious. Don't do this:
# ```python
# x = x + 1                 # Increment x
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# But sometimes, this is useful:
# ```python
# x = x + 1                 # Compensate for border
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Comments are important, but Documentation and schematics are even more important

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://preview.redd.it/jm8b5iwoq6p11.png?width=640&crop=smart&auto=webp&s=f4f484b59333e96555d8076b13dfbc2f8fc2b5b3" width=480>

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Docstrings

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://preview.redd.it/a5skfy5y88x11.jpg?width=640&crop=smart&auto=webp&s=edee581af2812ad4f4469d13e79e38d9b2dd3f06" width=360>

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Reading code you wrote a month ago
#
# <img src="https://preview.redd.it/htp8nd9yd1f51.jpg?width=640&crop=smart&auto=webp&s=79820471f09326c75ce6ea865d36290a7b600262" widht=480>

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### PEP8 Docstrings

# + [markdown] slideshow={"slide_type": "fragment"}
# > Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Checking for missing docstrings

# + slideshow={"slide_type": "fragment"}
from unittest import TestCase
import importlib


def get_undocumented_wildcards(modulename: str) -> (list, int):
    """lists undocumented public modules, functions, classes, and methods; and sum of all public members"""
    namespace = importlib.import_module(modulename)
    loc = namespace.__dict__
    undocumented = []
    for key, val in loc.items():
        if (key[0] != "_") and (key not in {"_", "In", "Out", "get_ipython", "exit", "quit", "join", "S"}):
            description = val.__doc__
            if not description:
                undocumented.append(key)
    return undocumented, len(loc.items())

undoc, num = get_undocumented_wildcards("phi.flow")
print(f"{len(undoc)/num:.2%}")

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Module Level Dunder Names

# + [markdown] slideshow={"slide_type": "fragment"}
# Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__, __author__, __version__, etc. should be placed after the module docstring but before any import statements except from __future__ imports. Python mandates that future-imports must appear in the module before any other code except docstrings:

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### Example

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### PEP257, The Docstring Conventions Guide

# + [markdown] slideshow={"slide_type": "fragment"}
# https://www.python.org/dev/peps/pep-0257/

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### What is a docstring?
#
# > A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__` special attribute of that object.

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### Single Line Docstring

# + [markdown] slideshow={"slide_type": "fragment"}
# > Triple quotes are used even though the string fits on one line. This makes it easy to later expand it.

# + [markdown] slideshow={"slide_type": "fragment"}
# > The closing quotes are on the same line as the opening quotes. This looks better for one-liners.

# + [markdown] slideshow={"slide_type": "fragment"}
# > There's no blank line either before or after the docstring.

# + [markdown] slideshow={"slide_type": "fragment"}
# > The docstring is a phrase ending in a period. It prescribes the function or method's effect as a command ("Do this", "Return that"), not as a description; e.g. don't write "Returns the pathname ...".

# + [markdown] slideshow={"slide_type": "fragment"}
# > The one-line docstring should NOT be a "signature" reiterating the function/method parameters (which can be obtained by introspection)

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# """Do X and return a list."""
# ``` 

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Types of Multi-Line Docstring

# + [markdown] slideshow={"slide_type": "fragment"}
# - Summary line, just like single-line docstring
# - Followed by an empty line
# - (more elaborate description)
# - Place closing quotes on a line by themselves

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### reStructured Text (RST)

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### NumPy/SciPy

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### Auto generate Docstrings!

# + [markdown] slideshow={"slide_type": "fragment"}
# VSCode: `Python Docstring Generator`

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Why conventions are important

# + [markdown] slideshow={"slide_type": "fragment"}
# Uniform convention allows automated documentation creation via `autodoc` and `apidoc` for `sphinx`

# + [markdown] slideshow={"slide_type": "fragment"}
# https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html

# + [markdown] slideshow={"slide_type": "subslide"}
# #### PEP8 + people = a lot of different opinions

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### flake8

# + [markdown] slideshow={"slide_type": "fragment"}
# Flake8 is one implementation of the PEP8 format.
# It also catches some errors like undefined variables. It also supports addign in plugins.
#
# Under the hood it combines pycodestyl and pyflakes together.

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python -m pip install flake8```

# + [markdown] slideshow={"slide_type": "fragment"}
# See: https://flake8.pycqa.org/en/latest/

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### black

# + [markdown] slideshow={"slide_type": "fragment"}
# Black is the "opinionated" python formatter. You either love it, or you hate it.
#
# Improtant differences are:
# - Only one argument per line
# - 88 character line limit
#

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### Example

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# def very_important_function(template: str, *variables, file: os.PathLike, engine: str, header: bool = True, debug: bool = False):
#     """Applies `variables` to the `template` and writes to `file`."""
#     with open(file, 'w') as f:
#         ...
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ```python
# # out:
# def very_important_function(
#     template: str,
#     *variables,
#     file: os.PathLike,
#     engine: str,
#     header: bool = True,
#     debug: bool = False,
# ):
#     """Applies `variables` to the `template` and writes to `file`."""
#     with open(file, "w") as f:
#         ...
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ###### In VSCode

# + [markdown] slideshow={"slide_type": "fragment"}
# Running in VSCode
#
# Edit settings.json by adding
# ```json
#     "python.formatting.blackArgs": ["--line-length", "160"],
#     "python.formatting.provider": "black",
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# ```pip install black```

# + [markdown] slideshow={"slide_type": "fragment"}
# For more see: https://black.readthedocs.io/en/stable/the_black_code_style.html

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### There are a lot of plugins, variations, etc.

# + [markdown] slideshow={"slide_type": "fragment"}
# - pylint
# - vulture (find dead code)
# - pydiatra
# - inspectortiger
# - flake8-bugbear
# - redbaron-missing-comma-string-collection
# - etc.
#
# for more see: https://github.com/vintasoftware/python-linters-and-code-analysis

# + [markdown] slideshow={"slide_type": "subslide"}
# ### KISS, goodbye to worrying about formatting

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Automatically format to PEP8:
#
# Autoformatting in VSCode: `alt`+`shift`+`f`
#
# In the settings you can select your autoformater, default is `autopep8` or `pylint`

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### autopep8
#
#

# + [markdown] slideshow={"slide_type": "fragment"}
#
# ```json
# "python.formatting.autopep8Args": [
#         "--max-line-length",
#         "160"
#     ],
# "python.formatting.provider": "autopep8",
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Or simply create your formatter settings file for your project!
#
# For example: `.flake8`
# ``` 
# [flake8]
# ignore = F401,F403,F405,E231,E501
# ``` 
#

# + [markdown] slideshow={"slide_type": "fragment"}
# ```cmd
# pip install pre-commit
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Create `pyproject.toml`
#
# ```
# [tool.black]
# py36 = true
# include = '\.pyi?$'
# exclude = '''
# /(
#     \.git
#   | \.hg
#   | \.mypy_cache
#   | \.tox
#   | \.venv
#   | _build
#   | buck-out
#   | build
#   | dist
#
#   # The following are specific to Black, you probably don't want those.
#   | blib2to3
#   | tests/data
# )/
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# Create `.pre-commit-config.yaml`
#
# ```
# # See https://pre-commit.com for more information
# # See https://pre-commit.com/hooks.html for more hooks
# repos:
# -   repo: https://github.com/pre-commit/pre-commit-hooks
#     rev: v2.3.0
#     hooks:
#     -   id: check-yaml
#     -   id: end-of-file-fixer
#     -   id: trailing-whitespace
# -   repo: https://github.com/psf/black
#     rev: 19.3b0
#     hooks:
#     -   id: black
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Install the hook via terminal `pre-commit install` in the directoy

# + [markdown] slideshow={"slide_type": "fragment"}
# Now pre-commit will run automatically on each `git commit`

# + [markdown] slideshow={"slide_type": "fragment"}
# Run the hooks manually via `pre-commit run --all-files`

# + [markdown] slideshow={"slide_type": "fragment"}
# For more see: https://dev.to/m1yag1/how-to-setup-your-project-with-pre-commit-black-and-flake8-183k
#
# Or the official site: https://pre-commit.com/

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Automatic sort imports

# + [markdown] slideshow={"slide_type": "fragment"}
# ```pip install isort```

# + [markdown] slideshow={"slide_type": "fragment"}
# `crtl`+`shift`+`p` $\rightarrow$ `Python Refactor: Sort Imports`
#
# In the settings you can define your import sorter, default is `isort`

# + [markdown] slideshow={"slide_type": "fragment"}
# For more information, see: https://github.com/timothycrosley/isort

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Pre-Commit Hooks

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Side note: There are rules for *everything*

# + [markdown] slideshow={"slide_type": "fragment"}
# Understanding they exist helps understanding why some representations look so weird

# + [markdown] slideshow={"slide_type": "subslide"}
# #### ISO 8601: Data elements and interchange formats - information interchange - Representation of dates and times

# + [markdown] slideshow={"slide_type": "fragment"}
# There is an official way to write dates and datetimes, this is it, everything else is not according to international standards.
# ```
# 2020-01-28
# 2020-01-28T13:44:24+00.00
# ```

# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
# Similarly unix timetsamps or epoch time are seconds since since 01.01.1970.


# + [markdown] slideshow={"slide_type": "slide"}
# ## Design Patterns

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Why are they important

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src=https://i.redd.it/rskneik2r4h41.jpg width=480>

# + [markdown] slideshow={"slide_type": "fragment"}
# They are widely used, therefore widely read, meaning you will read them, and have an easier time if you know them.

# + [markdown] slideshow={"slide_type": "subslide"}
# #### What is a Design Pattern?

# + [markdown] slideshow={"slide_type": "fragment"}
# > "Each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice"

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://preview.redd.it/2h7wdn8p70e51.jpg?width=640&crop=smart&auto=webp&s=e3b1e993244961540150a48ca00b424664bd00f0" width=320>

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Rule of Thumb

# + [markdown] slideshow={"slide_type": "fragment"}
# If you use ```ctrl+c```& ```ctrl+v```, you're not thinking enough about design

# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "subslide"}
# ### Brief Overview


# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
# Information from: https://sourcemaking.com/design_patterns


# + [markdown] slideshow={"slide_type": "fragment"}
# Three Types of Design Patterns:
# - Creational
# - Structural
# - Behavioral

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Creational Design Patterns

# + [markdown] slideshow={"slide_type": "fragment"}
# Focused on: class **instantiation** (creation)
#
# Subclasses:
# - creational **class**-creation patterns use inheritance effectively in the instantiation process
# - creational **object**-creation patterns use delegation effectively to get the job done

# + [markdown] slideshow={"slide_type": "fragment"}
# Prominent Patterns:
# - Abstract Factory
# - Builder
# - Factory Method
# - Object Pool
# - Prototype
# - Singleton

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Structural Design Patterns

# + [markdown] slideshow={"slide_type": "fragment"}
# Focused on: Class and Object **composition**
#
# Subclasses:
# - Structural class-creation patterns use inheritance to compose interfaces
# - Structural object-patterns define ways to compose objects to obtain new functionality

# + [markdown] slideshow={"slide_type": "fragment"}
# Prominent Patterns:
# - Adapter
# - Bridge
# - Composite
# - Decorator
# - Facade
# - Flyweight
# - Private Class Data
# - Proxy

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Behavioral design patterns

# + [markdown] slideshow={"slide_type": "fragment"}
# Focused on: Class's objects **communication**
#
# Behavioral patterns are those patterns that are most specifically concerned with communication between objects.

# + [markdown] slideshow={"slide_type": "fragment"}
# Prominent Patterns:
# - Chain of responsibility
# - Command
# - Interpreter
# - Iterator
# - Mediator
# - Memento
# - Null Object
# - Observer
# - State
# - Strategy
# - Template method
# - Visitor

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Criticism

# + [markdown] slideshow={"slide_type": "fragment"}
# - If these problem are so common, they should be fixed in the language
# - They are often overused when they are no longer needed
# - It can lead to rigid programming

# + [markdown] slideshow={"slide_type": "slide"}
# ## Code Analyzer
#
# Or what to do when you inherit 50,000 lines of a Java developers code...

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Static Code Analysis with `pyan3`
# https://github.com/Technologicat/pyan
#
#

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src=https://raw.githubusercontent.com/Technologicat/pyan/master/graph0.png width=640>

# + [markdown] slideshow={"slide_type": "fragment"}
# ```bash
# pip install pyan3
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# ```bash
# pyan3 *.py --uses --no-defines --colored --grouped --annotated --dot >myuses.dot
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Dependency analysis with `pydeps`
# https://github.com/thebjorn/pydeps

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://raw.githubusercontent.com/thebjorn/pydeps/master/docs/_static/pydeps-18-bacon4-cluster-max1000.svg?sanitize=true" width=640>

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Call Graph Creation with `pycallgraph2`
# https://github.com/daneads/pycallgraph2

# + [markdown] slideshow={"slide_type": "slide"}
# ## Functional Programming

# + [markdown] slideshow={"slide_type": "fragment"}
# - Object-Oriented Programming (OOP) shortcomings
# - Composition
# - Immutability
# - Pure functions (no side-effects)
# - Functional Programming in Python
#   - Lambda functions
#   - Maps

# + [markdown] slideshow={"slide_type": "subslide"}
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

# + [markdown] slideshow={"slide_type": "fragment"}
# Procedural Pogramming languages are very close to hardware as they describe the list of instructions in order, like C or Fortran and were mostly developed in the late 50s until early 1970s.
#
# The major declarative language still used today is SQL which we will cover in a future session on Databases (developed in the 70s-80s). 
#
# Object-oriented programming focus on deconstructing the program into objects, instances, and performing actions on these using member functions such as Java.
#
# Functional programming decomposes the problem into functions with inputs and outputs that get composed to process information.

# + [markdown] slideshow={"slide_type": "fragment"}
# Most modern programming languages like Python and C++ are multi-paradigm, and most big projects use multiple programming styles for different parts: GUIs are often simpler to describe as objects such as a slider that has methods that can be performed on it, while data processing is often easier to be described as various functions that are applied to the data.

# + [markdown] slideshow={"slide_type": "fragment"}
# That is why functional programming is important to data science - it is the preferred paradigm for processing data!

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Pure Functions in Python

# + [markdown] slideshow={"slide_type": "fragment"}
# > Pure functions have no side effects. 
#
# This means, functions map inputs to outputs and access nothing outside of the inputs. 

# + [markdown] slideshow={"slide_type": "fragment"}
# One common problem in Python is the global name lookup:

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
a = 1
b = 2
def impure(a0, b0):
    return a+b

print(impure(a,b))
a = 2
print(impure(a,b))
print(impure(5,5))

# + [markdown] slideshow={"slide_type": "fragment"}
# This bug in code is caused from the global name lookup that you **cannot** deactivate in Python easily.

# + [markdown] slideshow={"slide_type": "fragment"}
# Luckily, we're not the first one encountering this issue.
#
# Instead of prohibiting global lookups, we can patch the global namespace within each function with an empty namespace.
#
# Or even better, with just the namespace of imported modules, thereby allowing execution of code without needing to re-import modules.

# + [markdown] slideshow={"slide_type": "subslide"}
# #### One such solution is:

# + slideshow={"slide_type": "fragment"}
import types

def copyglobals(f):
    return types.FunctionType(f.__code__, globals().copy(), f.__name__, f.__defaults__, f.__closure__)


# + slideshow={"slide_type": "fragment"}
a = 10
b = 5
@copyglobals
def print_a(b):
    return a+1
print_a(b), a

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Force pure functions

# + slideshow={"slide_type": "slide"}
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

def noglobal(f):
    return types.FunctionType(f.__code__, dict(imports()))


# + slideshow={"slide_type": "fragment"}
a = 1
b = 1
@noglobal
def impure(a0,b0):
    return a+b

impure(1,2)

# + [markdown] slideshow={"slide_type": "fragment"}
# While it does not cause an error upon definition, it does cause an error upon calling it, instead of letting it pass with a wrong value.

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Functional Programming in Python

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Lambda

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
double = lambda x: x*2
double(5)

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Map

# + [markdown] slideshow={"slide_type": "fragment"}
# `map(function, iterable)` applies a function to every element in an iterable and returns an iterable

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
map(lambda x: x*x, [1,2,3,4,5])

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
list(map(lambda x: x*x, [1,2,3,4,5]))

# + [markdown] slideshow={"slide_type": "fragment"}
# map() on Pandas DataFrame

# + [markdown] slideshow={"slide_type": "fragment"}
# Benefits of Maps: Runtime knows they are independent and can use all parallelization methods

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Filter

# + [markdown] slideshow={"slide_type": "fragment"}
# `filter(function, iterable)` applies a True/False function to every element in an iterable and returns an iterable

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
filter(lambda x: x%2, [1,2,3,4,5])

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
list(filter(lambda x: x%2, [1,2,3,4,5]))

# + [markdown] slideshow={"slide_type": "subslide"}
# #### List & Dictionary Comprehension

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
[i*2 for i in range(0,5)]

# + jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
{i:i*2 for i in range(0,5)}

# + [markdown] slideshow={"slide_type": "fragment"}
# Benefits: Fast

# + [markdown] slideshow={"slide_type": "fragment"}
# Drawbacks: High-Memory usage from parallel execution

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Best Practices

# + [markdown] slideshow={"slide_type": "fragment"}
# > While you can assign lambda functions a name, this is not considered good Python form.

# + [markdown] slideshow={"slide_type": "fragment"}
# Use lambda functions for single uses when assigning a name in the namespace is not necessary.
#
# Lambdas have a (tiny) overhead that has to be considered.

# + [markdown] slideshow={"slide_type": "slide"}
# ## Module Architecture

# + [markdown] slideshow={"slide_type": "fragment"}
# - `__init__` files
# - src/ folder
# - bin/ folder
# - main() and `__main__`
# - README.md
# - Changelog.md
# - requirements
# - License files (and Licensing cheatsheet)
# - Python Module Structure

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Name your Project!!

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://preview.redd.it/31i8o3bvl3h51.png?width=640&crop=smart&auto=webp&s=6d15fbca5bc1ee97935da9396d815bd1bbb93e8a" width=480>

# + [markdown] slideshow={"slide_type": "subslide"}
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
# |-> .gitattributes
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

# + [markdown] slideshow={"slide_type": "fragment"}
# - Each folder is a `(sub)package`
# - Each package has an `__init__.py`
# - `tests` mirrors the main package 1:1
# - `docs` mirrors the main package closely too

# + [markdown] slideshow={"slide_type": "subslide"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# ### `__init__` files

# + [markdown] slideshow={"slide_type": "fragment"}
# Import the functions that should be used by other modules that import this module

# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
# `data/database.py`
# ```python
# def load_data_from_db(dataname, **kwargs):
#     return True
# ```
#
# `data/__init__.py`
# ```python
# from .database import load_data_from_db
# ```
#
# `some_code.py`
# ```python
# from data import load_data_from_db
# ```


# + [markdown] slideshow={"slide_type": "slide"}
# ## Documentation

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://preview.redd.it/08sz26e91k841.jpg?width=640&crop=smart&auto=webp&s=4cbb04afe0b73ad80c6d8b74b509024f3201405e" width=400>

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Audience:

# + [markdown] slideshow={"slide_type": "fragment"}
# Users want to know:
# - When to use it
# - How to use it
# - What it does

# + [markdown] slideshow={"slide_type": "fragment"}
# Developers want to know:
# - Why it is done this way
# - What it depends on
# - What depends on it
# - What options are available
# - What errors might be raised
# - What types are needed and returned

# + [markdown] slideshow={"slide_type": "fragment"}
# > “It doesn’t matter how good your software is, because if the documentation is not good enough, people will not use it.“
#     — Daniele Procida
#

# + [markdown] slideshow={"slide_type": "fragment"}
# > “Code tells you how; Comments tell you why.”
#    — Jeff Atwood (aka Coding Horror)

# + [markdown] slideshow={"slide_type": "fragment"}
# Since you already commented your code, writing documentation seems repetitive. That's where Spinx comes in!

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Sphinx
#
# Automatically generates documentations for you modules from the docstrings you write anyways!

# + [markdown] slideshow={"slide_type": "fragment"}
# It also allows for creating further documentation using the RST format. For example a Table of Contents:

# + [markdown] slideshow={"slide_type": "fragment"}
# ```
# .. toctree::
#    :maxdepth: 2
#
#    usage/installation
#    usage/quickstart
#    ...
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# ```bash
# pip install sphinx
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Creating an automatic API documentation

# + [markdown] slideshow={"slide_type": "fragment"}
# ```
# sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN …]
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# ```bash
# sphinx-apidoc -o source/build/ ../module_name/
# make html
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# For the full documentation, see: https://www.sphinx-doc.org/en/master/usage/quickstart.html
#
# For the hosted version, see: https://readthedocs.org/

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Sphinx

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://i.redd.it/d5x18rtcfof31.png" width=400 />

# + [markdown] slideshow={"slide_type": "fragment"}
# Don't worry, Sphinx is here to help!

# + [markdown] slideshow={"slide_type": "fragment"}
# Installation:
# ```bash
# conda install sphinx
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "fragment"}
# in GitHub under Hooks, you can define ReadTheDocs as a hook upon commit, meaning it will update your documentation automatically when committing to your repository

# + [markdown] slideshow={"slide_type": "slide"}
# ## How to get listed on PIP / PyPI (Python Package Index)
#
# Summarized from https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
# 1. First things first, you need an account on [PyPi](https://pypi.org/)


# + [markdown] slideshow={"slide_type": "fragment"}
# 2. Create a project using the steps of the previous chapters

# + [markdown] slideshow={"slide_type": "fragment"}
# 3. Pypi requires the presence of 4 files in the top level:
#    - setup.py
#    - setup.cfg
#    - LICENSE.txt
#    - README.md

# + [markdown] slideshow={"slide_type": "fragment"}
# Example Structure:
# ```
# |-> MyLib
# |-> setup.py
# |-> setup.cfg
# |-> LICENSE.txt
# |-> README.md
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# `setup.py`
#
# ```python
# from distutils.core import setup
# setup(
#     name = 'YOURPACKAGENAME',
#     packages = ['YOURPACKAGENAME'], 
#     version = '0.1',
#     license='MIT',
#     description = 'TYPE YOUR DESCRIPTION HERE',
#     author = 'YOUR NAME',
#     author_email = 'your.email@domain.com',
#     url = 'https://github.com/user/reponame',
#     download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',  # tar.gz to GitHub release
#     keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
#     install_requires=[
#         # List of dependencies
#         'validators',
#         'beautifulsoup4',
#     ],
#     classifiers=[
#         'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
#         'Intended Audience :: Developers',      # Define that your audience are developers
#         'Topic :: Software Development :: Build Tools',
#         'License :: OSI Approved :: MIT License',   # Again, pick a license
#         'Programming Language :: Python :: 3',      # Specify which pyhton versions that you want to support
#         'Programming Language :: Python :: 3.6',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',
#     ],
# )
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# `setup.cfg` 
# ```
# [metadata]
# description-file = README.md
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# 4. Upload your Project to a public GitHub

# + [markdown] slideshow={"slide_type": "fragment"}
# 5. Create a release version
# - GitHub -> Project -> "releases" tab -> "Create a new release"
# - Tag version == setup.py version-field.
# - Click "publish release"
# - Under Assets a new release is visible with a link to Source Code (tar.gz)
# - Copy Link Address
# - In the stup.py: paste the link-address into the download_url field
# - Repeat the steps for each new release

# + [markdown] slideshow={"slide_type": "fragment"}
# 6. Create source distribution: `python setup.py sdist`

# + [markdown] slideshow={"slide_type": "fragment"}
# 7. Upload to PyPi:
# - `pip install twine`
# - `twine upload dist/*`

# + [markdown] slideshow={"slide_type": "fragment"}
# 8. Congratulations, you are done! Check it out at: https://pypi.org/project/YOURPACKAGENAME/

# + [markdown] slideshow={"slide_type": "fragment"}
# For more, see: https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

# + [markdown] slideshow={"slide_type": "slide"}
# ## Code Maintenance

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Support

# + [markdown] slideshow={"slide_type": "fragment"}
# 1. Make simple rules for support.
# 2. Don't support unsupported packages! (looking at you Python 2)
# 3. Only support the last X versions
# 4. Update regularly

# + [markdown] slideshow={"slide_type": "fragment"}
# Example:
#
# You create an API and publish it as v1.0
#
# You want to change something to the API in v1.1, you should build backwards compatibility for v1.0

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Preventing code abandonment

# + [markdown] slideshow={"slide_type": "subslide"}
# #### 3 Causes for code abandonment

# + [markdown] slideshow={"slide_type": "fragment"}
# 1. Code is illegible
#    - Comments
#    - Documentation
#    - Tests

# + [markdown] slideshow={"slide_type": "fragment"}
# 2. Code is outdated
#    - Update dependencies regularly (e.g. 1st of every month)

# + [markdown] slideshow={"slide_type": "fragment"}
# 3. Code is cumbersomly written
#    - Take advantage of new features (only support new versions)
#    - Define code styling
#    - Define code design pattern
#    - Keep things shallow (at most 5 levels deep)

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Regularly update your Python

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Performance Improvements

# + [markdown] slideshow={"slide_type": "fragment"}
# Python version                      |   3.7 |     3.8  | Speedup |
# --------------                      |   --- |     ---  |-------- |
# *Variable and attribute read access:* |       |          |         |
# read_local                      |   5.1 |     3.9  | 1.3x |
# read_nonlocal                   |   5.4 |     4.4  | 1.2x |
# read_global                     |  13.6 |     7.6  | 1.8x |
# read_builtin                    |  19.0 |     7.5  | **2.5x** |
# read_classvar_from_class        |  19.5 |    18.4  | 1.1x |
# read_classvar_from_instance     |  17.1 |    16.4  | 1.0x |
# read_instancevar                |  26.3 |    25.4  | 1.0x |
# read_instancevar_slots          |  20.8 |    20.2  | 1.0x |
# read_namedtuple                 |  46.8 |    18.4  | **2.5x** |
# read_boundmethod                |  26.9 |    27.7  | 1.0x |
# *Variable and attribute write access:* |       |          | |
# write_local                     |   5.3 |     4.3  | 1.2x |
# write_nonlocal                  |   5.5 |     4.7  | 1.2x |
# write_global                    |  18.0 |    15.8  | 1.1x |
# write_classvar                  | 102.1 |    39.2  | **2.6x** |
# write_instancevar               |  38.9 |    35.5  | 1.1x |
# write_instancevar_slots         |  26.6 |    25.7  | 1.0x |
# *Data structure read access:*         |       |          | |
# read_list                       |  20.8 |    19.0  | 1.1x |
# read_deque                      |  20.6 |    19.8  | 1.0x |
# read_dict                       |  23.0 |    21.0  | 1.1x |
# read_strdict                    |  21.2 |    18.9  | 1.1x |
# *Data structure write access:*        |       |          | |
# write_list                      |  21.6 |    20.0  | 1.1x |
# write_deque                     |  21.8 |    23.5  | 0.9x |
# write_dict                      |  29.2 |    24.7  | 1.2x |
# write_strdict                   |  25.2 |    23.1  | 1.1x |
# *Stack (or queue) operations:*        |       |          | |
# list_append_pop                 |  74.2 |    50.8  | 1.5x |
# deque_append_pop                |  49.2 |    42.5  | 1.2x |
# deque_append_popleft            |  49.7 |    42.8  | 1.2x |
# *Timing loop:*                        |       |          | |
# loop_overhead                   |   0.3 |     0.3  | 1.0x |

# + [markdown] slideshow={"slide_type": "subslide"}
# ##### Keep your Code maintainable

# + [markdown] slideshow={"slide_type": "fragment"}
# Implementing backwards compatibility restricts your ability.

# + [markdown] slideshow={"slide_type": "fragment"}
# Like running a marathon withou shoes.

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Update your dependencies regularly

# + [markdown] slideshow={"slide_type": "fragment"}
# Yes, something will break. Yes, you will spend time fixing it.

# + [markdown] slideshow={"slide_type": "fragment"}
# This will:
# - when pushed off, updating becomes this big wall everyone avoids
# - this leads to code abandonment
# - and a new poor grad student has to redo all the work
# - the small annoyances will lead to reducing dependencies
# - iteratively makes the code more maintainable, as you want to have it as easy as possible!

# + [markdown] slideshow={"slide_type": "slide"}
# ## Command Line Interfaces

# + [markdown] slideshow={"slide_type": "fragment"}
# Most popular tool these days: <a href="https://github.com/pallets/click">**Click**</a>
#
# ```bash
# conda install click
# pip install click
# ```
#

# + [markdown] slideshow={"slide_type": "fragment"}
# Click is developed as parts of <a href="palletsprojects.com/">pallets</a>, who also develop <a href="https://github.com/pallets/flask">Flask</a>

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Minimal Example

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "fragment"}
# ```bash
# > python test.py
# Hello World
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# ```bash
# > python test.py --help
# Usage: click_test.py [OPTIONS]
#
# Options:
#   --help  Show this message and exit.
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# `click.echo` is used to ensure:
# - works for `Python 2` and `Python 3`
# - prevents `UnicodeError`
# - supports ANSI Colors
# If you do not want these features, you can use `print()`

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Adding Commands

# + [markdown] slideshow={"slide_type": "fragment"}
# `click.group`s wrap commands as one, allowing arbitrarily nesting.

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Example

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Or in short:

# + [markdown] slideshow={"slide_type": "slide"}
# ```python
# @click.group()
# def cli():
#     pass
#
# # note 'cli' (name of the group) instead of 'click'
# @cli.command()
# def initdb():
#     pass
#
#
# @cli.command()
# def dropdb():
#     pass
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Usage

# + [markdown] slideshow={"slide_type": "fragment"}
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

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Pass commands via context

# + [markdown] slideshow={"slide_type": "fragment"}
# Groups can perform common computations and pass the results to the children commands via the context. From the doc:

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# @click.group()
# @click.option('--debug/--no-debug', default=False)
# @click.pass_context
# def cli(ctx, debug):
#     # ensure that ctx.obj exists and is a dict (in case `cli()` is called
#     # by means other than the `if` block below)
#     ctx.ensure_object(dict)
#
#     ctx.obj['DEBUG'] = debug
#
#     
# @cli.command()
# @click.pass_context
# def sync(ctx):
#     click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
#
#     
# if __name__ == '__main__':
#     cli(obj={})
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Adding Parameters

# + [markdown] slideshow={"slide_type": "fragment"}
# Commands can have two types of parameters:
# - `argument`s: positional arguments of python fucntions 
# - `option`s: key-value arguments of python functions

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Example

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# import click
#
#
# @click.command()
# @click.option('--count', default=1, help='number of greetings')
# @click.argument('name')
# def hello(count, name):
#     '''
#     Greets somebody a given number of times.
#     '''
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
# if __name__ == "__main__":
#     hello()
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Running examples

# + [markdown] slideshow={"slide_type": "fragment"}
# ```bash
# > python test.py --help
# Usage: test.py [OPTIONS] NAME
#
#   Greets somebody a given number of times.
#
# Options:
#   --count INTEGER  number of greetings
#   --help           Show this message and exit.
# ```
#
# ```bash
# > python test.py Robin
# Hello Robin!
# ```
#
# ```bash
# > python test.py Robin --count 3
# Hello Robin!
# Hello Robin!
# Hello Robin!
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ### More complex Options

# + [markdown] slideshow={"slide_type": "fragment"}
# https://click.palletsprojects.com/en/7.x/options/

# + [markdown] slideshow={"slide_type": "fragment"}
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
# - file argument (`type=click.File('w')`)
#   - bonus: specifying `-` will automatically use stdin/stdout as appropriate
# - path argument (`type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True)`)
#   - bonus: performs some checks (above: must exists, not a file, can be written to)
# - and more...

# + [markdown] slideshow={"slide_type": "fragment"}
# ```python
# @click.option("--c1", default=1, type=click.FloatRange(0, None), show_default=True,
#               help="Scale between: hydrodynamic: 0.1, transition: 1, adiabatic: 5")
# ```

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Real world example

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Code

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="../img/click_example_code.jpg" />

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Help page

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="../img/click_example_help.jpg" />

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Setuptools Integration

# + [markdown] slideshow={"slide_type": "fragment"}
# Benefits:
# - Executable wrapping with necessary requirements into a virtual environment
# - Windows and Unix executables

# + [markdown] slideshow={"slide_type": "slide"}
# ## That's it

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Thank you for not falling asleep

# + [markdown] slideshow={"slide_type": "subslide"}
# ### If there are any question, now is the time!
