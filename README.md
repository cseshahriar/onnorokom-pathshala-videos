# shosen-tube-videos
Shosen tube videos modules

# __Usage:__
> _This document will be using the following
>
> _Please make sure `git`, `python`, `postgresql` and is installed in the system._
>
> _NOTE for Windows users: Please use `Git Bash` for the following steps_


1. ### Configure the project
    - git clone https://github.com/cseshahriar/onnorokom-pathshala-videos.git
    - cd dir_name
    - Create folders for `logs`, and `media`.
    - Copy `local_settings.example` to `local_settings.py`.
    - Update `local_settings.py` with proper `settings`, including `database`.
    ```shell script
    mkdir -p logs && mkdir -p media/uploads
    cp examples/local_settings.example app/local_settings.py
    
    nano app/local_settings.py
    # edit local_settings.py
    DB_NAME = 'db_name'
    DB_USER = 'db username'
    DB_PASS = 'db password'
    ```

2. ### Run the project
    - cd project root dir
    - python3 -m venv venv
    - source venv/bin/active
    - pip3 install -r requirements.txt
    - Run `python manage.py makemigrations` and `python manage.py makemigrations migrate`.
    - Run `python manage.py tests`
    - Create superuser to access the admin panel `python manage.py createsuperuser`.
    - Run django `python manage.py runserver 127.0.0.1:8001` to view the project or application.
    
   > _NOTE: Browse to [http://127.0.0.1:8001/](http://127.0.0.1:8001/) to view the site. Admin site is at url [/manage](http://127.0.0.1:8001/admin) changed from default to keep the project secure. Admin url can be changed in `settings.py` --> `ADMIN_URL`_
