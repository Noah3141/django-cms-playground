## Virtualenv

`python --version` - currently active python
`pip list` - check that virtualenv is installed in current python
`virualenv env` - virtualenv, create an environment of the specified (here the default) python version, called "env", at the default location (here)

`source ./env/Scripts/activate` (BACKslashes for windows, no `source`)

`pip install django-stubs`

`pip install django-cms`
`django-admin startproject rootFolderName`
`python manage.py startapp subfolderAppName`

## Database Setup:

`pip install psycopg2 ` for Postgres
`pip install mysqlclient` for MySQL

If you encounter a horrid problem with getting mysqlclient to install without erroring, check that `wheel` is installed, that VS Build tools are installed, and that mysql is functioning from commandline with env variable set properly.

## Typing:

`pip install django-stubs` // https://stackoverflow.com/questions/59031982/type-annotations-for-django-models

`/repo` where your project is `/repo/RootFolder/settings.py`

```
[mypy]
mypy_path = ./RootFolderOfDjango
plugins =
    mypy_django_plugin.main

strict_optional = True

[mypy.plugins.django-stubs]
django_settings_module = RootModuleOfDjango.settings


```

## Python Importing

Great set of diagrams here: https://stackoverflow.com/questions/36311812/django-cannot-import-modules
