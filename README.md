# weatherApp
Live weather updates

A webapp that gets the weather of over 200,000 cities around the world. To know the weather of any city, simply enter name of the city in the search field.

This project was first built fetching the API from the backend using the request library.
But it has been updated to use XMLHttpRequest from the frontend while still maintaining Django for the backend

Follow these commands to run the project on your local machine :

Open your terminal

Clone the project 
```
git clone https://github.com/Judekennywise/weatherproject.git
```

Enter the project directory 

```
cd weatherproject
```

Create a virtual env

```
python -m venv env 
```

Activate your env(for windows)

```
env\Scripts\activate 
```
(for linux or mac)

```
source env/bin/activate 
``` 

Install Project Dependencies

```
pip install -r requirements.txt
```
Run the project, make sure you are the same directory where "manage.py" is located

```
python manage.py runserver
```


