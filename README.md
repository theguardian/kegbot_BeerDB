kegbot_BeerDB
=============

A widget for global beer database management, which kegbot will have the ability to pull from.

Required:
* Python 2.7

Optional, but recommended:
* virtualenv, setuptools

Built in a virtualenv with the following packages, installed using pip:
* Django==1.5.1
* pillow
* django-imagekit
* django-crispy-forms==1.3.2
* djangorestframework
* django-filter
* django-selectable
* markdown
* south
* gunicorn

For production servers, the following are recommended with sudo apt-get:
* nginx
* supervisor

Instructions for use:
1. Git clone into directory of your choice
2. Modify local_settings.py for your local environment (<your_absolute_directory>/kegbot_BeerDB/*)
3. >> python manage.py collectstatic

For development:
4. >> python manage.py runserver 0.0.0.0:<PORT #>

For production:
4. Update values in /production/kegbot_BeerDB-supervisor.conf (<your_absolute_directory>/kegbot_BeerDB/*)
5. Update values in /production/kegbot_BeerDB-nginx.conf (<your_absolute_directory>/kegbot_BeerDB/*)
6. >> sudo cp production/kegbot_BeerDB-nginx.conf /etc/nginx/sites-available/
7. >> sudo ln -s /etc/nginx/sites-available/kegbot_BeerDB-nginx.conf /etc/nginx/sites-enabled/
8. >> sudo cp production/kegbot_BeerDB-supervisor.conf /etc/supervisor/conf.d/kegbot_BeerDB.conf
9. >> sudo service nginx restart
10. >> sudo service supervisorctl restart

Then the kegbot_BeerDB will be available on http://YO.UR.IP.AD:8334!

kegbot_BeerDB code is licensed under GNU v2.0.  The initial contents leverage beer data from openbeerdb.com, licensed under the Open Database License & Database Content License.

