Backend v 1.0
=============

Models (postgres, sqlalchemy, alembic):
---------------------------------------
* Tags [id, name_tag, description]
* Accounting [id, date, type, description, sum, tags]

Routes :
--------
* POST [date, type, description, sum, tags] return 200 if complete else 400
* GET return all data in DB