# Network Aware iRODS API

Specification in [swaggerhub](https://app.swaggerhub.com/apis/mjstealey/network-aware-irods-api/1.0.0)

## Development

###  Local Environment

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

From the `docker/` directory.

Create a file named **network-aware-irods.env** based on the provided example:

```
CONNEXION_SERVER=gevent
CONNEXION_DEBUG=False
API_SERVER_HOST=localhost
API_SERVER_PORT=5000
API_SERVER_KEYFILE=
API_SERVER_CERTFILE=
IRODS_HOST=
IRODS_PORT=1247
IRODS_USER=
IRODS_PASSWORD=
IRODS_ZONE=
IRODS_CLIENT_USER=
IRODS_CLIENT_ZONE=
SWAGGER_HOST=localhost:8080
```

Update the **network-aware-irods-local.sh** script to reflect the settings of the **network-aware-irods.env** file.

Generally this means updating the port number of `LOCAL_PORT` to match that of the port declared by `SWAGGER_HOST`

Run the **network-aware-irods-local.sh** script.

```
$ ./run-network-aware-irods-local.sh
Sending build context to Docker daemon  30.18MB
Step 1/22 : FROM python:3
 ---> be512ebcbac9
 ...
Step 22/22 : CMD app.py
 ---> Running in 0ed57335c7f3
 ---> 0d14c2cd70e5
Removing intermediate container 0ed57335c7f3
Successfully built 0d14c2cd70e5
Successfully tagged network-irods:latest
/Users/stealey/Github/scidas/network-aware-irods-api/docker
network-irods
network-irods
7d32c077494573d89ce2cb8c101faaa93afb59808a0730ec11fa86d37197e517
Network Aware iRODS API running at http://localhost:8080/v1/ui/#/default
```

Validate the the server is running at the URL defined by `SWAGGER_HOST`

## Production Deployment

**TODO**