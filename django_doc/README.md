# Build a Django app
## Using Python

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
- You'll need to go to http://127.0.0.1:8000/ (or whatever URL is shown in the terminal) in your browser
- You should see an animated rocket ship

7. Connect to your database in settings.py
> In the DATABASES section:
```
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'django-example',
    }
}
```

8. Transfer our migrations to the database
```
CTRL + C >> shuts down server first
python manage.py migrate
```

9. Connect our project (PROJECT_NAME) to the django app (main_app)
```
touch main_app/urls.py
```
- Import paths to APP_NAME/urls.py file
```Python
# add 'include' to import statement

from django.urls import path, include

# add to urlpatterns section:

path('', include('main_app.urls')),

# if you add authentication or other features, you might need to also add:

path('accounts/', include('django.contrib.auth.urls'))
```
- Import paths and url patterns to main_app/urls.py file
- Use views or Class Based Views
```Python
from django.urls import path
# You'll also import views
from . import views

# urls will follow a similar format
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('things/', views.ThingList.as_view(), name='things_index'),
    path('things/create', views.ThingCreate.as_view(), name='things_create'),
]
```
10. Set up view functions
- views.py is where you'll be adding all the functions and Python to make your app work
```Python
# in main_app/views.py
from django.http import HttpResponse
# this is starter code - once you add more refined HTML templates you won't need HttpResponse

# Create views
def home(request):
    return HttpResponse('Hello World')

```
