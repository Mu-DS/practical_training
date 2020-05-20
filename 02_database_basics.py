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
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] Collapsed="false"
# # Data Management and Database Basics

# + [markdown] Collapsed="false"
# ## Motivation

# + [markdown] Collapsed="false"
# <img src="https://preview.redd.it/gph4rp6drvo41.jpg?width=640&crop=smart&auto=webp&s=a407a7be1da73ba010f0295a6351ab9d14471b2a" width=400 />

# + [markdown] Collapsed="false"
# ## Overview

# + [markdown] Collapsed="false"
# 1. Pre-SQL  (Robin)
# 2. SQL databases  (Ali/Emilio)
# 3. Non-SQL databases  (Ali)
# 4. Simple graph database introduction  (Robin?)

# + [markdown] Collapsed="false"
# # Pre-SQL

# + [markdown] Collapsed="false"
# - You kind of have data, but not really that much.
# - You want to organize it better,  but keep things lightweight to share.

# + [markdown] Collapsed="false"
# ## Working with CSV files

# + Collapsed="false"



# + [markdown] Collapsed="false"
# ### Efficiently reading last lines

# + Collapsed="false"



# + [markdown] Collapsed="false"
# # SQL
# -

# ## intro
#  - sql is a declarative programming language to manipulate tables
#  - declarative: no functions or loops, just _declare_ what you need and the runtime will figure out how to compute it
#  - sql queries can be used to
#    - insert new rows into a table
#    - delete rows from a table
#    - update one or more attributes of one or more rows in a table
#    - retrieve and possibly transform rows combing from one or more tables
#  - this section will mostly focus on reading data (last point)

#
# ## main abstraction: tables
#  - a table is a _set_ of tuples (rows)
#    - no two rows are the same
#  - rows are distinguished by _primary keys_
#    - primary key: smallest set of attributes that uniquely identifies a row, examples:
#      - student ID (one attribute)
#      - first name, last name, birth date, place of birth (four attributes)
#    - the primary key is a property of each table
#      - all rows in a table use the same attributes as primary key
#      - but different tables can have different primary keys
#    - cannot have two rows with the same primary key
#  - _foreign keys_ are used to refer to rows of other tables
#    - e.g. a table with grades will have foreign keys that point to the student and the course

# ## domain
#  - good database design has
#    - one table for each "entity" in the domain
#    - relationships between entities
#  - types of relationships:
#    - 1 to 1 (can be stored in either entity, but NOT BOTH, or in a separate talbe)
#    - 1 to n (must be stored in the entity with cardinality "1", or in a separate table)
#    - m to n (requires a separate table)  
#  - example:
#    - entity students
#      - relationship mentor (suppose 1 to 1), three possibilities
#        - have a column "mentor"
#        - have a column "mentee"
#        - have a new table (mentor, mentee)
#    - entity courses
#    - entity professors
#    - relationship grades (m to n -> requires a table)
#      - student, course, grade
#    - relationship teaches (m to n -> requires a table)
#      - professors, courses
#  - sql shines when "navigating" across relationships
#    - example: for each student, find the professor that gave them the highest grade

# ## anatomy of a select query
#  - "select" queries are used to retrieve data from the database
#  - must have SELECT+FROM
#  - WHERE and GROUPBY optional
#  - HAVING optional, must be used with GROUP BY
#  - note on GROUP BY: eventually you must have only one row per group
#
# ```
# SELECT <columns and transformation>
# FROM <source table(s)>
# [WHERE <filter rows coming from source table(s)>]
# [GROUP BY <create groups of rows>
# [HAVING <filter groups>]]
# ```

# ## select query untangled
#  - confusingly, order of execution is different than order of writing:
#    1. FROM: first, gather all input rows from all tables
#    2. WHERE: next, remove all rows not matching the predicate
#    3. GROUP BY: now, if needed, create groups of rows
#    4. HAVING: then, remove all groups that do not match the predicate
#    5. SELECT: finally, produce output rows

# ## FROM: source tables
#  - you can specify one or more tables in the from clause
#  - FROM will do a cross-product of all tuples of all tables
#  - in almost all cases, you only want a small subset of the cross-product
#    - use WHERE to remove tuples that do not make sense
#  - special case: JOIN
#    - inner/left/right/outer
#  - possible to give aliases to tables that can be used in the remainder of the query

# ## WHERE: tuple filter
#  - specify a boolean condition that is evaluated for each row produced by the FROM
#  - all rows where this evaluates to false are discarded

# ## GROUP BY: create groups of rows
#  - must specify one or more columns, possibly with transformation
#  - all rows that have the same values for all (transformed) column(s) end up in the same group

# ## HAVING: filter groups
#  - another boolean condition applied to each group
#  - example: filter by group size, min/max/mean of something..

# ## SELECT: produce output columns
#  - all the surviving groups/rows are transformed
#  - select only a subset of attributes, or transform values
#  - careful: each group must be collapsed into a row

# ## subqueries and CTE
#  - to make things messy

# ## examples of complex queries
#  - TODO

# ## programmatically interfacing to a RDBMS
#  - connections
#  - cursors
#  - sql injection and proper escaping

# ## transactions and ACID
#  - heh

# ## advanced: query plans and indexing
#  - why

# + [markdown] Collapsed="false"
# # Non-SQL

# + Collapsed="false"



# + [markdown] Collapsed="false"
# # Graph Databases

# + [markdown] Collapsed="false"
# ## Graph Theory

# + Collapsed="false"



# + [markdown] Collapsed="false"
# ## Neo4j

# + Collapsed="false"

