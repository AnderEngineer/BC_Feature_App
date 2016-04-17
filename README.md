Feature Request App for IWS and BriteCore

Use virtualenv with Python2.7
To install virtualenv:
  - sudo apt-get install python-virtualenv

If virtualenv is installed, run the following commands:
-# mkdir WebApp
-# virtualenv WebApp
-# cd WebApp
-# git clone https://github.com/mrandersondev/BC_Feature_App.git
-# source bin/activate
-# cd BC_Feature_App
-# pip install -r requirements.txt
-# cd FeatureRequestProject
-# python manage.py makemigrations
-# python manage.py migrate
-# python manage.py runserver

Go to: http://127.0.0.1:8000/

When finished:
  Use CONTROL-C to stop the server.
  Run "deactivate" to stop the virtualenv environment.

Thanks!
