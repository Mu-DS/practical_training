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

# + [markdown] Collapsed="false" slideshow={"slide_type": "slide"}
# # SQL

# + [markdown] slideshow={"slide_type": "slide"}
# ## Introduction
#  - SQL is a declarative programming language to manipulate tables
#    - no functions or loops, just _declare_ what you need and the runtime will figure out how to compute it
#  - SQL queries can be used to
#    - Insert new rows into a table
#    - Delete rows from a table
#    - Ipdate one or more attributes of one or more rows in a table
#    - Retrieve and possibly transform rows combing from one or more tables
#  - Relational Database Management System (RDBMS)
#    - Manages data in the tables
#    - Executes queries, returns results
#  - This section will mostly focus on reading data (last point)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Main abstraction: Tables
#  - A table is a _set_ of tuples (rows)
#    - No two rows are the same
#  - Rows are distinguished by _primary keys_
#    - Primary key: smallest set of attributes that uniquely identifies a row
#    - Cannot have two rows with the same primary key
#    - Examples:
#      - Student ID (one attribute)
#      - First name, last name, birth date, place of birth (four attributes)
#    - The primary key is a property of each table
#      - All rows in a table use the same attributes as primary key
#      - But different tables can have different primary keys

# + [markdown] slideshow={"slide_type": "slide"}
# ## Domain
#  - Good database design has
#    - One table for each entity in the domain
#    - Relationships between two or more entities
#  - _Foreign keys_ are used to refer to rows of other tables
#    - e.g. a table with grades will have foreign keys that point to the student and the course

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Example: University
#  - Entities
#    - Students (ID, Name, Degree)
#    - Courses (ID, Title, Faculty, Semester)
#    - Professors (ID, Name, Chair)
#  - Relationships
#    - One student can *Mentor* another student
#    - A student *Attends* several courses and obtains a grade for each of them
#    - Professors *Teach* courses

# + [markdown] slideshow={"slide_type": "subslide"}
# ### ER diagram
#  - Graphical form to represent entities and relationships
#    - Box: entity
#    - Diamond: relationship
#    - Circle: attribute
#  
#  
# ![](../img/sql_er_diagram.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Which tables to create?
#  - Until now, we separated entities from relationships
#  - But in practice everything must be stored into tables
#  - How to do this?
#    - One table per entity (students, courses, professors)
#    - What about the relationships?
#      - Mentor: 1 to 1, three possibilities
#        1. Have a column "mentor"
#        2. Have a column "mentee"
#           - Having both is not ideal: more work to ensure consistency
#        3. Have a new table (mentor, mentee)
#      - Attends: M to N
#        - Requires a table (student, course)
#      - Teaches: 1 to N
#        - Store professor in course table or create separate table
#    - General rule:
#      - Using a separate table is always possible, or
#      - 1 to 1: can store in either entity
#      - 1 to N: store in entity with cardinality N
#      - M to N: must use separate table

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Final list of tables
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course)
#  - Which attributes are primary and foreign keys?

# + [markdown] slideshow={"slide_type": "slide"}
# ## Purpose of SQL
#  - SQL shines when "navigating" across relationships, for example:
#    - For each student, find the professor that gave them the highest grade
#    - For each professor, find courses taught last semester
#  - Also used to modify data

# + [markdown] slideshow={"slide_type": "slide"}
# ## Anatomy of a SELECT query
#  - SELECT queries are used to retrieve data from the database
#  - The result is itself a table (not saved unless specified)
#
# ```
# SELECT <columns and transformation>
# FROM <source table(s)>
# [WHERE <filter rows coming from the source table(s)>]
# [GROUP BY <create groups of rows>
# [HAVING <filter groups>]]
# [ORDER BY <columns> [ASC|DESC]];
# ```
#
#  - Must have SELECT and FROM
#  - WHERE and GROUPBY are optional
#  - HAVING is optional, and must be used with GROUP BY
#  - GROUP BY: eventually you must have only one row per group

# + [markdown] slideshow={"slide_type": "slide"}
# ## Select query untangled
#  - Confusingly, the execution order is different than the writing order:
#    1. FROM: first, gather all input rows from all tables
#    2. WHERE: next, remove all rows not matching the predicate
#    3. GROUP BY: now, if needed, create groups of rows
#    4. HAVING: then, remove all groups that do not match the predicate
#    5. ORDER BY: sort the tuples by a the value of a certain column
#    6. SELECT: finally, produce output columns
# -

# ## Example
#
# Find all courses held in the Winter semester 2019/2020:
#
# ```sql
# SELECT *
# FROM Courses
# WHERE Semester = 'WiSE 19/20;
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ## FROM: source tables
#  - You can specify one or more tables in the from clause
#  - FROM will do a cross-product of all tuples of all tables
#  - In almost all cases, you only want a small subset of the cross-product
#    - Use WHERE to remove tuples that do not make sense
#  - Possible to give aliases to tables and use that alias in the rest of the query
#    - Useful to keep query short and to disambiguate when the same table is used several times in the same query

# + [markdown] slideshow={"slide_type": "slide"}
# ## WHERE: tuple filter
#  - Specify a boolean condition that is evaluated for each row produced by the FROM
#  - All rows where this evaluates to false are discarded
#  - Handling of null values:
#    - Nothing is equal to `NULL` (not even `NULL`)
#      - `x = NULL` is _always_ false
#    - Use `x IS NULL` or `x IS NOT NULL`
#    - Nasty example:
#      - `SELECT * FROM stuff WHERE x = 10 OR NOT x = 10;`
#      - Result differs from `SELECT * FROM stuff;` when `x` contains `NULL` values!
#      - Query is actually equivalent to `SELET * FROM stuff WHERE x IS NOT NULL`

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example
#
#  - Associate to each student all its grades (one per row)
#  - Each row has three columns: name of the student, title of the course, grade
#
# ```sql
# SELECT
#     s.Name AS student_name,
#     c.Title AS course_title,
#     a.Grade AS grade
# FROM
#     Students AS s,
#     Attend AS a,
#     Course AS c
# WHERE
#     s.ID = a.Student
#     AND a.Course = c.ID;
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ## JOIN: a special case of FROM+WHERE
#  - In most cases, we are not interested in the cross-product
#  - We actually want tuples that match primary/foreign keys
#  - This operation is so common that it has a special name to distinguish it from the general case
#  - Other than the name, the two are completely equivalent
#  - Join makes your intentions clearer
#  - The previous query becomes:
#
# ```sql
# SELECT
#     s.Name AS student_name,
#     c.Title AS course_title,
#     a.Grade AS grade
# FROM
#     Students AS s
#     JOIN Attend AS a
#         ON s.ID = a.Student
#     JOIN Course AS c
#         ON c.ID = a.Course;
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ## Non-matching rows in JOINs
#  - Options to handle non-matches:
#    - Inner join: `FROM Students [INNER] JOIN Attend ON Student.ID = Attend.Student`
#      - `WHERE Students.ID = Grade.student`
#      - Only keep matches
#    - Left join: `FROM Students LEFT JOIN Attend ON Student.ID = Attend.Student`
#      - Keep matches and un-matched records from _left_ table
#    - Right join: `FROM students RIGHT JOIN Attend ON Student.ID = Attend.Student`
#      - Keep matches and un-matched records from _right_ table
#    - Outer join: `FROM students OUTER JOIN Attend ON Student.ID = Attend.Student`
#      - Keep matches, cross-product between un-matched records
#  - Other possibilities:
#     - Natural join: `FROM Students JOIN Grades`
#       - `ON` is missing -> match all columns with the same name
#     - Self-join: `FROM Students AS s JOIN Students AS t`
#       - Use table aliases in this case

# + [markdown] slideshow={"slide_type": "subslide"}
# ### INNER JOIN
#
# ```sql
# FROM Students [INNER] JOIN Attend
#     ON Student.ID = Attend.Student
# ```
#
# ![](../img/sql_join_inner.svg)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### LEFT JOIN
#
# ```sql
# FROM Students LEFT JOIN Attend
#     ON Student.ID = Attend.Student
# ```
#
# ![](../img/sql_join_left.svg)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### RIGHT JOIN
#
# ```sql
# FROM Students RIGHT JOIN Attend
#     ON Student.ID = Attend.Student
# ```
#
# ![](../img/sql_join_right.svg)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### OUTER JOIN
#
# ```sql
# FROM Students OUTER JOIN Attend
#     ON Student.ID = Attend.Student
# ```
#
# ![](../img/sql_join_outer.svg)
#
#
# Warning: cross-product between unmatched rows!

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Retrieving un-matched rows only
#
#  - Example: find all students who have not attended any course
#
# ```sql
# SELECT Students.ID
# FROM Students LEFT JOIN Attend
#     ON Students.ID = Attends.Student
# WHERE
#     Attends.Student IS NULL
# ```
#
# ![](../img/sql_join_unmatched_only.svg)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Multi-way JOINs
#
#  - Cyan
#    - Courses that nobody attended
#    - Professors that taught one or more courses nobody attended
#  - Orange:
#    - Students who attended one or more courses
#    - Courses that were attended by one or more students
#  - Gray areas: not realizable in our domain
#
#
# ![](../img/sql_join_multi.svg)
# -

#
# ```sql
# SELECT *
# FROM Professors AS p
#     JOIN Course AS c ON p.ID = c.Professor
#     LEFT JOIN Attend AS a ON a.Course = c.ID
# WHERE a.Student IS NULL
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ## GROUP BY: create groups of rows
#  - must specify one or more columns, possibly with transformation
#  - all rows that have the same values for all (transformed) column(s) end up in the same group

# + [markdown] slideshow={"slide_type": "slide"}
# ## HAVING: filter groups
#  - another boolean condition applied to each group
#  - example: filter by group size, min/max/mean of something..
# -

# # ORDER BY: order tuples
#
#  - Sort the tuples produced by the query
#  - Sort by the value of one or more columns, possibly transformed

# + [markdown] slideshow={"slide_type": "slide"}
# ## SELECT: produce output columns
#  - all the surviving groups/rows are transformed
#  - select only a subset of attributes, or transform values
#  - careful: each group must be collapsed into a row
# -

# ## Example:
#
# Find all students who failed at least two exams and, for each of them, find how many separate courses the failed exams belong to. Sort the result by number of courses and student ID.
#
# ```sql
# SELECT Student, COUNT(Course)
# FROM Attends
# WHERE Grade > 5
# GROUP BY Student
# HAVING COUNT(*) > 1
# ORDER BY COUNT(Course) DESC, Student ASC
# ```
#
# Q: What happens when the grade is NULL?

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

# ## Transactions and ACID properties
#
#  - When the data is read and modified by several clients at the same time, care must be taken
#  - Read/modify/write workflows especially vulnerable
#  - Transaction: a set of queries (reads and/or writes)
#    - Atomicity: sequence of operations appears as as a single operation on the data
#      - Either all operations succeed, or the all modifications are undone
#    - Consistency: database invariants are always satisfied regardless of the outcome
#       - Invariants: uniqueness, non-empty values, primary/foreign keys, etc.
#    - Isolation: different transactions cannot "see" each other
#       - Order of transactions does not matter
#    - Durability: once completed, the modifications are permanent
#       - Useful in case of crashes
#   - All of this is handled automatically by the DBMS
#     - Users only need to declare start/end and outcome of the transaction

# ## programmatically interfacing to a RDBMS
#  - connections
#  - cursors
#  - sql injection and proper escaping

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

