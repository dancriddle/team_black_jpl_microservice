team_black_jpl_microservice
===========================

Contains the web services and database/stubs to store, validate and process JPL requests

#team_black_jpl_microservice

##what is it?
Contains the web services and database/stubs to store, validate and process joint proprietor letter requests.  
This service is completely faked, mocked etc.

##dependencies
Flask
 
Jinja

Resolve Python dependencies by running pip install -r requirements.txt

team_black_casework service found at: https://github.com/dancriddle/team_black_casework


##config.py
create a config.py when you run the application.  It needs a key to know where the casework service is.  e.g.

```
CASEWORK_STUB = 'http://0.0.0.0:5010'
```
or

```
CASEWORK_STUB = 'CASEWORK_STUB = 'https://team-black-casework-yourname.c9.io'
```

##how to use it

to run the app:
```
python frontend.py
```

the app runs locally at:

http://0.0.0.0:5009/

how to curl the service to remove a restriction:

```
this app $ curl -i -H "Content-Type: application/json" -X PUT -d '{"complete": true}' Https://eam-black-casework-2-srallis1-2.c9.io/todo/api/v1.0/titles/complete/2345678
```
