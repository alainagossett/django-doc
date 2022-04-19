# Build a Django app
## Using Python

### Starting a Project:
1. Create a database for the project (using Postgresql)
```
createdb <DATABASE_NAME>
```
2. Create the project
- in the root directory of your computer:
```
cd django_env
pipenv shell
```
- then navigate to a folder where you want to create your project
```
django-admin startproject <PROJECT_NAME>
cd <PROJECT_NAME>
code-insiders .
```

3. Once open in text editor, confirm the Python interpreter is being used  
  a. CMD + Shift + P >> Python: Select Interpreter >> select the one with '*django_env*' in it  
  b. You might need to trash your existing terminal and open a new one to activate it  
  c. Success when you see the '*(django_env) username$*' in the terminal  


4. Create a main_app for your project
```
django-admin startapp main_app
```
- you should see a main_app directory get created with a bunch of python files and a migrations folder

5. In the project folder (_not_ main_app) add your main_app to settings.py
> In the INSTALLED_APPS section:
```
INSTALLED APPS = [
    'main_app',
    etc.
]
```

6. Run your server to test what you've got so far
```
python manage.py runserver
```