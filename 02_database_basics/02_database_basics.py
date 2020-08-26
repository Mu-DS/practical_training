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

# + [markdown] slideshow={"slide_type": "slide"}
# ### Example: University
#  - Entities
#    - Students (ID, Name, Degree)
#    - Courses (ID, Title, Faculty, Semester)
#    - Professors (ID, Name, Chair)
#  - Relationships
#    - One student can *Mentor* another student
#    - A student *Attends* several courses and obtains a grade for each of them
#    - Professors *Teach* courses

# + [markdown] slideshow={"slide_type": "slide"}
# ### ER diagram
#  - Graphical form to represent entities and relationships
#    - Box: entity
#    - Diamond: relationship
#    - Circle: attribute
#  
#  
# ![](../img/sql_er_diagram.png)

# + [markdown] slideshow={"slide_type": "slide"}
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

# + [markdown] slideshow={"slide_type": "slide"}
# ### Final list of tables
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)
#  - Which attributes are primary and foreign keys?

# + [markdown] slideshow={"slide_type": "slide"}
# ## Purpose of SQL
#  - SQL shines when "navigating" across relationships, for example:
#    - For each student, find the professor that gave them the highest grade
#    - For each professor, find courses taught last semester
#  - Also used to modify data, tables, databases, etc.
#    - Not discussed in this course

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
# ## Example
#
# Find all courses held in the Winter semester 2019/2020:
#
# ```sql
# SELECT *
# FROM Courses
# WHERE Semester = 'WiSE 19/20';
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ## Select query untangled
#  - Confusingly, the execution order is different than the writing order:
#    1. FROM: first, gather all input rows from all tables
#    2. WHERE: next, remove all rows not matching the predicate
#    3. GROUP BY: now, if needed, create groups of rows
#    4. HAVING: then, remove all groups that do not match the predicate
#    5. ORDER BY: sort the tuples by a the value of a certain column
#    6. SELECT: finally, produce output columns

# + [markdown] slideshow={"slide_type": "slide"}
# ## Interactive SQL console
#
# An interactive SQL console with a few tables can be accessed at [w3schools.com](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)
#
#  - Go to w3schools.com
#  - Scroll until SQL, on the left side there will be a query and a button "Try it Yourself"
#  - I encourage you to fiddle around while I am explaining
#  - They also have a (superficial) command reference
#  
# ![](../img/w3trysql.png)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Interactive SQL console
#
# ![](../img/w3sqled.png)

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
#  - Example: Associate to each student all its grades (one per row)
#
# ```sql
# SELECT *
# FROM
#     Students AS s,
#     Attend AS a,
#     Course AS c
# WHERE
#     s.ID = a.Student
#     AND a.Course = c.ID;
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ## WHERE: handling of NULL values 
#  
#  - NULL is used for "undefined" values
#  - Nothing is equal to NULL (not even NULL)
#    - `x = NULL` always equals NULL (i.e. false)
#  - Use instead `x IS NULL` or `x IS NOT NULL`
#  - Nasty example: `SELECT * FROM table WHERE x = 10 OR NOT x = 10`
#    - When `x` contains NULLs this equals `WHERE x IS NOT NULL`
#    - Dumb fix: `WHERE x = 10 OR NOT x = 10 OR x IS NULL`

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
# SELECT *
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
#    - Inner join: Only keep matches
#    - Left join: keep matches and un-matched records from _left_ table
#    - Right join: keep matches and un-matched records from _right_ table
#    - Outer join: keep matches, cross-product between un-matched records
#  - Other possibilities:
#     - Natural join (`ON` is missing): match all columns with the same name
#     - Self-join: A table with itself (e.g. to find a student's mentor)

# + [markdown] slideshow={"slide_type": "slide"}
# ### INNER JOIN
#
# ```sql
# FROM Students [INNER] JOIN Attend
#     ON Student.ID = Attend.Student
# ```
#
# ![](../img/sql_join_inner.svg)

# + [markdown] slideshow={"slide_type": "slide"}
# ### LEFT JOIN
#
# ```sql
# FROM Students LEFT JOIN Attend
#     ON Student.ID = Attend.Student
# ```
#
# ![](../img/sql_join_left.svg)

# + [markdown] slideshow={"slide_type": "slide"}
# ### RIGHT JOIN
#
# ```sql
# FROM Students RIGHT JOIN Attend
#     ON Student.ID = Attend.Student
# ```
#
# ![](../img/sql_join_right.svg)

# + [markdown] slideshow={"slide_type": "slide"}
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

# + [markdown] slideshow={"slide_type": "slide"}
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

# + [markdown] slideshow={"slide_type": "slide"}
# ## GROUP BY: create groups of rows
#  - must specify one or more columns, possibly with transformation
#  - all rows that have the same values for all (transformed) column(s) end up in the same group

# + [markdown] slideshow={"slide_type": "slide"}
# ## HAVING: filter groups
#  - A boolean condition applied to each group
#  - Example: filter by group size, min/max/average of something..
#  - Common case: counting
#    - `COUNT(*)`: number of rows in the group
#    - `COUNT(expr)`: number of rows where `expr` is not NULL
#    - `COUNT(DISTINCT expr)`: number of unique values of `expr` (excluding NULLs)

# + [markdown] slideshow={"slide_type": "slide"}
# ## ORDER BY: order tuples
#
#  - Sort the tuples produced by the query
#  - Sort by the value of one or more columns, possibly transformed
#  - Possible to order by aggregations (count/min/max/sum/avg)

# + [markdown] slideshow={"slide_type": "slide"}
# ## SELECT: produce output columns
#  - All the surviving groups/rows are transformed
#  - Select only a subset of attributes, or transform values
#  - Careful: each group must be collapsed into a row

# + [markdown] slideshow={"slide_type": "slide"}
# # Examples

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example 1
#
# Find the ID of all students who failed at least one exam.
#
# ```sql
# SELECT ...
# ```
#
# Tables:
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example 1
#
# Find the ID of all students who failed at least one exam.
#
# ```sql
# SELECT Student
# FROM Attends
# WHERE Grade > 5
# ```
#
#
# Tables:
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example 2
#
# Find how many exams each student failed.
#
# ```sql
# SELECT ...
# ```
#
# Tables:
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example 2
#
# Find how many exams each student failed.
#
# ```sql
# SELECT Student, COUNT(*)
# FROM Attends
# WHERE Grade > 5
# GROUP BY Student
# ```
#
#
# Tables:
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example 3
#
# Find how many exams each student failed, only for the students who failed at least 2.
#
# ```sql
# SELECT ...
# ```
#
#
# Tables:
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example 3
#
# Find how many exams each student failed, only for the students who failed at least 2.
#
#
# ```sql
# SELECT Student, COUNT(*)
# FROM Attends
# WHERE Grade > 5
# GROUP BY Student
# HAVING COUNT(*) > 1
# ```
#
#
# Tables:
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example 4
#
# Find how many courses each student failed, only for the students who failed at least 2 exams.
#
# ```sql
# SELECT ...
# ```
#
#
# Tables:
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Example 4
#
# Find how many courses each student failed, only for the students who failed at least 2 exams.
#
# ```sql
# SELECT Student, COUNT(DISTINCT Course)
# FROM Attends
# WHERE Grade > 5
# GROUP BY Student
# HAVING COUNT(*) > 1
# ```
#
#
# Tables:
#  - Students(ID, Name, Degree, Mentor)
#  - Professors(ID, Name, Chair)
#  - Courses(ID, Title, Faculty, Semester, Professor)
#  - Attends(Student, Course, Grade)

# + [markdown] slideshow={"slide_type": "slide"}
# # Transactions and ACID properties
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

# + [markdown] slideshow={"slide_type": "slide"}
# # Interfacing to a RDBMS
#
# Three types of clients
#
#  1. Command line clients
#  2. Graphical clients
#  3. Programmatic access

# + [markdown] slideshow={"slide_type": "slide"}
# ## Command line clients
#
# Enter SQL queries and administrative commands directly from the command line:
#
# ```
# $ sqlite3
# SQLite version 3.32.3 2020-06-18 14:00:33
# Enter ".help" for usage hints.
# Connected to a transient in-memory database.
# Use ".open FILENAME" to reopen on a persistent database.
# sqlite> 
# ```
#
# ```
# $ psql -U user -h 10.0.6.12 -p 21334 -d database
# psql (11.1, server 11.0)
# Type "help" for help.
#
# postgres=# 
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ## Graphical clients
#
# Database-specific:
#  - pgAdmin (PostgreSQL)
#  - SQLite Browser (SQLite)
#  - MySQL Workbench (MySQL)
#
# General purpose:
#  - [SQuirreL](http://squirrel-sql.sourceforge.net)
#  - [SQLAdmin](http://sqladmin.sourceforge.net/)

# + [markdown] slideshow={"slide_type": "slide"}
# ### SQuirreL example: querying
# ![](http://squirrel-sql.sourceforge.net/screenshots/15_edit_result.png)

# + [markdown] slideshow={"slide_type": "slide"}
# ### SQuirreL example: visualizing tables
#
# ![](http://squirrel-sql.sourceforge.net/screenshots/7_graph.png)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Programmatic Access
#
# Two types of APIs:
#
#  1. High-level: Object-relational mapping (ORM)
#     - Each table has a corresponding class in the code
#     - Operations on objects are automatically translated on queries
#     - These libraries can work with many SQL databases
#  2. Low-level: Directly write SQL queries as strings
#     - Usually tied to a specific type of SQL database

# + [markdown] slideshow={"slide_type": "slide"}
# ### SQLAlchemy: ORM in Python
#
# Example from [pythoncentral.io](https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/).
#
# Tables:
#
# ```python
# class Department(Base):
#     __tablename__ = 'department'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     employees = relationship('Employee', secondary='department_employee')
#
# class Employee(Base):
#     __tablename__ = 'employee'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     departments = relationship('Department', secondary='department_employee')
#
# class DepartmentEmployee(Base):
#     __tablename__ = 'department_employee'
#     department_id = Column(Integer, ForeignKey('department.id'), primary_key=True)
#     employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ### Inserting data in SQLAlchemy
#
# ```python
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///')
#
# from sqlalchemy.orm import sessionmaker
# session = sessionmaker()
# session.configure(bind=engine)
# Base.metadata.create_all(engine)
#
# s = session()
# john = Employee(name='john')
# s.add(john)
# it_department = Department(name='IT')
# it_department.employees.append(john)
# s.add(it_department)
# s.commit()
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ### Querying in SQLAlchemy
#
# asd
#
# ```python
# find_marry = select([
#     Employee.id
# ]).select_from(
#     Employee.__table__.join(DepartmentEmployee)
# ).group_by(
#     Employee.id
# ).having(func.count(
#     DepartmentEmployee.department_id
# ) > 1)
#
# rs = s.execute(find_marry) 
# rs.fetchall()  # result: [(2,)]
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ### Accessing SQLite in Python
#
# Example from [python3.org](https://docs.python.org/3/library/sqlite3.html)
#
# ```python
# import sqlite3
# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
#
# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')
#
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# conn.commit()
#
# conn.close()
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ### Querying SQLite in Python
#
# ```python
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00)]
#
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
#
# for row in c.execute('SELECT * FROM stocks WHERE price<? ORDER BY price', [2000,]):
#     print(row)
#
# # ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
# # ('2006-04-06', 'SELL', 'IBM', 500, 53.0)
# # ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# ## Programmatic access to SQL databases
#
# Common concepts:
#
# | SQLite | SQLAlchemy | Purpose |
# |-|-|-|
# | Connection | Engine | The database object |
# | Cursor | Session | A transaction |
#
# General workflow:
#
#  1. Obtain a connection
#     - Use a connection pool if performance is a concern
#  2. Obtain a cursor
#  3. Execute queries
#  4. Close cursor
#  5. Possibly repeat...
#  6. Close connection

# + [markdown] slideshow={"slide_type": "slide"}
# ### SQL injection
#
#  - An once-popular cyber-attack on SQL databases
#  - Caused by improper escaping of arguments coming from external users (e.g. in a web form)
#  - Never trust user input!
#
# Example:
#
# ```python
# def find_courses(conn, semester):
#     c = conn.cursor()
#     return c.execute(
#         "SELECT * FROM Courses WHERE Semester={}".format(semester)
#     ).fetchall()
#
# # later on...
# find_courses(conn, "''; DROP TABLE Courses; --")
# ```
#
# This will execute **two** queries:
#
# ```sql
# SELECT * FROM Courses WHERE Semester='';
# DROP TABLE Courses; --
# ```
#

# + [markdown] slideshow={"slide_type": "slide"}
# ### Avoiding SQL injection
#
# Let the API handle escaping for you:
#
# ```python
# def find_courses(conn, semester):
#     c = conn.cursor()
#     return c.execute(
#         "SELECT * FROM Courses WHERE Semester=?",
#         [semester]
#     ).fetchall()
#
# # later on...
# find_courses(conn, "''; DROP TABLE Courses; --")
# ```
#
# This will execute **one** query:
#
# ```sql
# SELECT * FROM Courses WHERE Semester='''''; DROP TABLE Courses; --'
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# # Where should I start from?
#
# [SQLite](https://sqlite.org/index.html) is very simple and scales well.
#
# [PostgreSQL](https://www.postgresql.org/) for more complicated requirements / large scale data processing.
#
# Also frequently used: [MySQL](https://www.mysql.com/)

# + [markdown] slideshow={"slide_type": "slide"}
# # Advanced topics

# + [markdown] slideshow={"slide_type": "slide"}
# ## Indexing
#  - depending on your query and how you express it, it may be quite slow
#  - the DBMS tries to optimize every query, but sometimes it fails
#  - when most of the time is spent on joins and lookups, creating _indices_ can greatly speed up the query
#  - an index is just a mapping from values to rows that contain that value in one or more columns
#  - this makes it much faster to find rows that contain a given value
#    - instead of checking row by row, simply look in the index
#    - think about books!
#  - an index is always relative to a table and one or more columns
#    - `CREATE INDEX <index name> ON <table name>(<list of columns>)`
#  - a table can have many indices
#    - an index is always created automatically for primary keys
#    - all other unique keys must also have an index
#    - indices on foreign keys _might_ be useful
#    - WHERE/JOIN are much faster when there is an index on one of the columns
#  - if a query is slow and/or executed very frequently, consider adding an index on columns used in the WHERE/JOIN

# + [markdown] slideshow={"slide_type": "slide"}
# ## Main types of index
#  - Tree-based: O(log N) access, can be used to quickly answer queries like `WHERE L < column < U`
#    - Branching factor in the order of 1000s
#  - Hash-based: O(1) access, cannot answer range queries
#  - Clustered index: table is physically sorted by the columns

# + [markdown] slideshow={"slide_type": "slide"}
# ## Query plans
#  - understanding why a query is slow is not trivial
#  - the query plan is produced by the optimizer and shows exactly what and how is done to execute the query
#  - it contains an estimated cost and can be augmented with the actual cost measured when executing the query
#  - estimated cost:
#    - computed from statistics about rows/values that the DBMS maintains internally
#    - these statistics can become inaccurate after lots of operations
#    - useful to periodically recompute these statistics
#    - also useful to periodically clear the space allocated to deleted rows and defragment table data
#  - (show example of plans before/after adding an index)

# + [markdown] slideshow={"slide_type": "slide"}
# ### Example
#
# ![](../img/qplan.png)
#
# Image from [dba.stackexchange.com](https://dba.stackexchange.com/q/9234)

# + [markdown] Collapsed="false" slideshow={"slide_type": "slide"}
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

