# Network Aware iRODS API

## Local Development

### Initial Setup

Applies when there are changes made to the database and a new **models.py** file needs to be generated, otherwise skip to [Local Environment](#localenv).

###  <a name="localenv"></a>Local Environment

From the top level of the repository:

```
$ cd server/
$ virtualenv -p /usr/local/bin/python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

**ini/connexion.ini**

Set up the `ini/connexion.ini` file to match your environment. An example file named `ini/connexion.ini.example` has been provided as a template.

```
$ cp ini/connexion.ini.example ini/connexion.ini
```

- Change `/PATH_TO/` to be the actual path to the code.
- Populate `[irods]` fields with information for a reachable running instance of iRODS. The values for `client_user` and `client_zone` are not being used at this time.

	```config
	[connexion]
	server =
	debug = True
	port = 5000
	keyfile =
	certfile =
	
	[irods]
	host =
	port = 1247
	user =
	password = 
	zone =
	client_user =
	client_zone =
	
	[sys-path]
	controllers = /PATH_TO/network-aware-irods-api/server/controllers
	```

To run the server, execute the following:

```
python3 app.py
```

and open your browser to here:

```
http://localhost:5000/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:5000/v1/swagger.json
```

## Docker Development

**TODO**

## Production Deployment

**TODO**