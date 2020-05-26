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
import random
import pandas as pd
import itertools

cnt = int(4)
xxs = list(range(cnt))
aas = list(range(cnt))

df_complete = pd.DataFrame(list(itertools.product(xxs, aas)), columns=['X', 'A'])
df_complete['Y'] = [random.randint(-25, 26) for _ in range(len(df_complete))]
mask = np.array([random.random() < 0.5 for _ in range(len(df_complete))])
df_complete.loc[~mask, 'Y'] = 0
TableA = df_complete[mask]
# -


len(TableA), len(df_complete)

TableA

# +
choices = len(TableA['A'].unique())
def variance_with_missing(vals):
    mean_with_missing = np.sum(vals) / choices
    ss_present = np.sum((vals - mean_with_missing)**2)
    ss_missing = (choices - len(vals)) * mean_with_missing**2
    return (ss_present + ss_missing) / (choices - 1)

TableA.groupby('X').agg({'Y': variance_with_missing})
# -

df_complete.groupby('X').agg({'Y': 'var'})


# +
def test(TableA):
    for i in range(1,TableA.X.max()+1):
        for j in TableA.A.unique():
            if not (TableA[(TableA.X==i) & (TableA.A==j)]['Y']).any():
                TableA = TableA.append(pd.DataFrame({'A':[j],'X':[i],'Y':[0]}),ignore_index=True)


    return TableA.groupby('X').agg({'Y':np.var})

# %timeit test(TableA)

# +
def test2(TableA):
    choices = len(TableA['A'].unique())
    def variance_with_missing(vals):
        mean_with_missing = np.sum(vals) / choices
        ss_present = np.sum((vals - mean_with_missing)**2)
        ss_missing = (choices - len(vals)) * mean_with_missing**2
        return (ss_present + ss_missing) / (choices - 1)

    return TableA.groupby('X').agg({'Y': variance_with_missing})

# %timeit test2(TableA)

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
#  - types of binary relationships:
#    - 1 to 1 (can be stored in either entity, but NOT BOTH, or in a separate talbe)
#    - 1 to n (must be stored in the entity with cardinality "1", or in a separate table)
#    - m to n (requires a separate table)  
#  - possible to have relationships between more than two entities
#  - example:
#    - entities
#      - students (id, name, degree)
#      - courses (id, faculty, semester)
#      - professors (id, name, chair)
#    - relationships
#      - "mentor" between students (suppose 1 to 1), three possibilities
#        - have a column "mentor"
#        - have a column "mentee"
#        - having both is not ideal: more work to ensure consistency
#        - have a new table (mentor, mentee)
#      -  grades (entity student, entity course, attribute grade)
#        - m to n -> requires a table
#      - teaches (professors, courses)
#        - m to n -> requires a table
#        - only one professor per course -> store professor in course table or create separate table
#  - sql shines when "navigating" across relationships, for example:
#    - for each student, find the professor that gave them the highest grade
#    - for each professor, find courses taught last semester

# ## anatomy of a select query
#  - "select" queries are used to retrieve data from the database
#    
#     ```
# SELECT <columns and transformation>
# FROM <source table(s)>
# [WHERE <filter rows coming from source table(s)>]
# [GROUP BY <create groups of rows>
# [HAVING <filter groups>]]
#     ```
#     
#  - must have SELECT+FROM
#  - WHERE and GROUPBY optional
#  - HAVING optional, must be used with GROUP BY
#  - note on GROUP BY: eventually you must have only one row per group

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
#    - use WHERE to remove tuples that do not make sense - possible to give aliases to tables that can be used in the remainder of the query
#  - possible to give aliases to tables and use that alias in the rest of the query
#    - useful to keep query short and when the same table is used several times in the same query

# ## WHERE: tuple filter
#  - specify a boolean condition that is evaluated for each row produced by the FROM
#  - all rows where this evaluates to false are discarded
#  - handling of null values

# ## JOIN: a special case of FROM+WHERE
#  - in most cases, we are not interested in the cross-product
#  - we actually want tuples that match primary/foreign keys
#  - example `SELECT * FROM students, grades WHERE students.id = grade.student`
#    - associates to each student all its grades (one per row)
#  - this operation is so common that it has a special name to distinguish it from the general case
#  - `SELECT * FROM students JOIN grades ON student.id = grade.student`
#  - options to handle non-matches:
#    - inner join: `FROM students [INNER] JOIN grades ON student.id = grade.student`
#      - `WHERE students.id = grade.student`
#      - only keep matches
#    - left join: `FROM students LEFT JOIN grades ON student.id = grade.student`
#      - `WHERE students.id = grade.student OR grade.student IS NULL`
#      - keep matches and un-matched records from _left_ table
#    - right join: `FROM students RIGHT JOIN grades ON student.id = grade.student`
#      - `WHERE students.id = grade.student OR stude=nt.id IS NULL`
#      - keep matches and un-matched records from _right_ table
#    - outer join: `FROM students OUTER JOIN grades ON student.id = grade.student`
#      - `WHERE students.id = grade.student OR grade.student IS NULL OR student.id IS NULL`
#      - keep matches, cross-product between un-matched records
#  - other possibilities:
#     - natural join: `FROM students JOIN grades`
#       - `ON` is missing -> match all columns with the same name
#     - self join: `FROM stdudents s JOIN students t`
#       - better to use aliases

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
#  - too many CTE's can make query slower, sometimes better to create temporary table
#  - jww's usecase:
#     ```sql
# select t.id, (
#   select u.status
#   from tbl u
#   where t.id == u.id and t.timestamp >= u.timestamp
#   order by desc u.timestamp
#   limit 1
# ) as status
# from tbl t
# ```
#
#    - tbl has columns id, timestamp, status, where status can be null.
#    - goal is to fill null status with most recent non-null status (of the same id)
#    - need index on (id, timestamp) to be quick

# ## examples of complex queries
#  - TODO

# ## programmatically interfacing to a RDBMS
#  - connections
#  - cursors
#  - sql injection and proper escaping

# ## transactions and ACID
#  - heh

# ## advanced: indexing
#  - depending on your query and how you express it, it may be quite slow
#  - the DBMS tries to optimize every query, but sometimes it fails
#  - when most of the time is spent on joins and lookups, creating _indices_ can greatly speed up the query
#  - an index is just a mapping from values to rows that contain that value in one or more columns
#  - this makes it much faster to find rows that contain a given value
#    - instead of checking row by row, simply look in the index
#    - think about books!
#  - an index is always relative to a table and one or more columns
#    - `CREATE INDEX <index name> ON <table name>(<list of columns>)`
#  - a table can have many indices, but one is always created automatically for primary keys
#    - all otherunique keys must also have an index
#    - joins are much faster when there is an index on one of the columns
#  - if a query is slow and/or executed very frequently, consider adding an index on columns used in the WHERE/JOIN
#  - types of index:
#    - tree-based: O(NlogN) access, can be used to quickly answer queries like `WHERE L < column < U`
#    - hash-based: O(1) access, cannot answer range queries
#    - clustered index: table is physically sorted by the columns

# ## advanced: query plans
#  - understanding why a query is slow is not trivial
#  - the query plan is produced by the optimizer and shows exactly what and how is done to execute the query
#  - it contains an estimated cost and can be augmented with the actual cost measured when executing the query
#  - estimated cost:
#    - computed from statistics about rows/values that the DBMS maintains internally
#    - these statistics can become inaccurate after lots of operations
#    - useful to periodically recompute these statistics
#    - also useful to periodically clear the space allocated to deleted rows and defragment table data
#  - (show example of plans before/after adding an index)

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

