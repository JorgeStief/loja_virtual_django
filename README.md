# Django Loja Virtual


# Preparing enviroment

* Create and activate a virtualenv

	```
	$ virtualenv -p python3 env
	$ source env/bin/activate
	```

* Clone this repository


* Install requirements and migrate:

	```
	$ pip install -r requirements.txt
	$ python manage.py migrate
	```




# Working with

* To start server:
	```
	$ python manage.py runserver
	```


* To create a super user do:

	```
	$ python manage.py createsuperuser
	```


* After create your super user:
Go to http://127.0.0.1:8000/admin, access with your credentials, go to Profiles and create a profile linked to your admin account


*