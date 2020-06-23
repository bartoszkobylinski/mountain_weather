# WEATHER FORECAST FOR TATRAS FOR THE NEXT FEW DAYS

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is an web based app to aggregate weather information, current conditions, avalanche warnings and so on.
Application run one time per day few scraper to gather information about condition. Additionally user can sign in and 
add a picture with current condition where app will make a pin on map based on geotag of picture to show place where 
picture were taken
	
## Technologies
Project is created with:
* Python
* JavaScript
* HTML5, CSS3
* Django
* Selenium
* AWS EC2, R53, RDS

To run this project, install it locally using pip:

Create a virtual environment

```
$ python3 -m venv /path/to/new/virtual/env
```
Activate virtual environment
```
source ~/env_catalog_name/bin/activate
```
install depencies 

```
$ cd ../mountain_weather
$ pip install -r requirements.txt
```
install virtual environment
```
export DB_NAME='name of your database'
export DB_USER='name of user'
export DB_PASS='password'
export ACCU_API_KEY='your api key on accu weather services'
export DB_HOST='localhost'
export PATH_SCRAPER='path to chromedriver file on your computer'
```
To run server locally

```
$ python manage.py runserver
```
