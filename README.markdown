**Django Starter**

My simple Django project template.

- Uses Twitter Bootstrap CSS library

**Usage**

1. Setup Virtual Environment
    - mkdir app
    - cd app
    - virtualenv --no-site-packages root
    - source root/bin/activate
2. Clone the repository and rename to cms
   - git clone git@github.com:ronbeltran/DjangoStarter.git
   - mv DjangoStarter cms
3. Change into cms and install dependencies
   - pip install -r requirements.txt
4. Setup db and run.
    - python manage.py syncdb
    - python manage.py runserver 
5. Grab some coffee, or should I put this at #1 ?
