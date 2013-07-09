kegbot_BeerDB
=============

A widget for global beer database management, which kegbot will have the ability to pull from.

Required:
* Python 2.7

Optional, but recommended:
* virtualenv, setuptools

Built in a virtualenv with the following packages, installed using pip:
* django 1.5
* pillow
* django-imagekit
* django-crispy-forms
* djangorestframework
* django-filter
* django-selectable
* markdown
* south

For production servers, the following are recommended:
* gunicorn
* nginx
* supervisor

kegbot_BeerDB code is licensed under GNU v2.0.  The initial contents leverage beer data from openbeerdb.com, licensed under the Open Database License & Database Content License.

