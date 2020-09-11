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
# # Best Practices in Machine Learning and Code Organization

# + [markdown] slideshow={"slide_type": "slide"}
# ## Motivation

# + [markdown] slideshow={"slide_type": "fragment"}
# - What does best-practice even mean?
# - How do I know something is a bad practice?

# + [markdown] jupyter={"outputs_hidden": true} slideshow={"slide_type": "fragment"}
# > It's not wrong, but it feels wrong.


# + [markdown] slideshow={"slide_type": "slide"}
# ## Overview

# + [markdown] slideshow={"slide_type": "fragment"}
# Best Pratices in:
# - Machine Learning Code Bases and Versioning
# - Code and Module organization and philosophies

# + [markdown] slideshow={"slide_type": "slide"}
# ## Bad vs. Best Practices in Python

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Repetition

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Python is not C - so do ***not*** copy-and-paste!

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://www.gogagah.com/wp-content/uploads/2019/04/Find-the-Difference-1024x576.jpg" width=380>

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Instead of copy & pasting:

# + [markdown] slideshow={"slide_type": "fragment"}
# - write functions!
# - compose functions!
# - create partial function!

# + slideshow={"slide_type": "fragment"}
def add(a, b):
    return a + b


# +
from functools import partial

add2 = partial(add, 2)  # Create a copy of add() with a=2

add2(3)

# + slideshow={"slide_type": "fragment"}
add2 = lambda x: add(2, x)

add2(3)


# +
def add2(x):
    return add(2, x)

add2(3)


# + [markdown] slideshow={"slide_type": "subslide"}
# ### Switch Behavior

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Python has no switch statements, but don't go around stacking if's:

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://i.redd.it/6rbq35occu441.jpg" width=300px>

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Instead of stacking if-else:

# + [markdown] slideshow={"slide_type": "fragment"}
# - map things with a dictionary!

# + [markdown] slideshow={"slide_type": "fragment"}
# Dictionaries are hashmaps, meaning the map a hash to an object.

# + [markdown] slideshow={"slide_type": "fragment"}
# Since Functions are first order objects in Python, they can be pointed to!

# + slideshow={"slide_type": "fragment"}
def add(a, b):
    return a + b

def add_sum(a, b):
    return sum([a, b])

math_functions = {'add': add_sum}

math_functions['add'](2, 2)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Depth

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Making too many layers - inheritance, nesting, etc.

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://preview.redd.it/3kz7f2k1psx41.jpg?width=640&crop=smart&auto=webp&s=0c026807888b4c611089b31c740947bf78b5a3c5" width=400 />

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Instead keep things shallow

# + [markdown] slideshow={"slide_type": "fragment"}
# Ask yourself:
# - Do I need this class?
#   - Will it be instantiated often?
#   - Are there many objects inheriting from it?
#   - Does it carry state? Otherwise its a namespace!
# - Does this need to be submodul or a file?
#   - Are there many long functions?
#   - Are there a large number of private functions?

# + [markdown] slideshow={"slide_type": "fragment"}
# Singleton Pattern (Single global instance for an Object)
# - If it does not carry state, it is a namespace
#   - In Python, any file is a namespace! No need for the Object or Instance!
# - If it just carries state, you want a database
#   - Atomicity of operation can be guaranteed with a database
#   - Database outside of Global Interpreter Lock (GIL)
#   - Databases scale better!

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Readability

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Write code - but write it to be read!

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://i.redd.it/yl1lu031day41.png" width=400 />

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Code is written to be read

# + [markdown] slideshow={"slide_type": "fragment"}
# - Documentation
# - Type Hinting
# - Naming

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Dependencies

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Sometimes they're too tempting

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://i.redd.it/mapjfjami3y41.jpg" width=400 />

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Why?

# + [markdown] slideshow={"slide_type": "fragment"}
# - Projects get abandoned
#   - Lack of security patches
#   - Forced to stay with old versions
#   - => Your project becomes ancient
# -

# Update regularly!
# - Small bugs on a regular basis prevent abandonment
# - Improved performances
# - Additional functionality!

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Keep things short

# + [markdown] slideshow={"slide_type": "subslide"}
# #### The first law of Software Quality

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://i.redd.it/tozimpm65gy41.jpg" widht=350 />

# + [markdown] slideshow={"slide_type": "subslide"}
# #### Sometimes less functionality is more maintainability

# + [markdown] slideshow={"slide_type": "fragment"}
# > Each line of code is a credit you take on and interest is paid in time to maintain the base. Don't default on your code debt.

# + [markdown] slideshow={"slide_type": "fragment"}
# Finding non-critical code:
# - Is this functionality used by many?
# - Is this code still used or abandoned?
# - Is it relevant to the larger goal?

# + [markdown] slideshow={"slide_type": "fragment"}
# Solving too much code:
# - Spin out functionality into a different module
# - Simplify the code
# - Delete code
# - No really, you should delete code

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Use version control

# + [markdown] slideshow={"slide_type": "fragment"}
# <img src="https://external-preview.redd.it/u1_S5Vu4FztMR72c9pfl086wbmdlZYVjK77i1IEvTjg.jpg?width=640&crop=smart&auto=webp&s=310af21a5b237f4b53a982afc2077fcdb4b1839c" width="400">
