# Configure Server and Client for Globus GridFTP

## Following Setup Tutorial from JASMIN @ https://bit.ly/2jTSk2A
Set up Globus CLI on end-user machine @ https://docs.globus.org/cli/installation/ (essentially pip install, then set PATH)
```
wget https://s3.amazonaws.com/connect.globusonline.org/linux/stable/globusconnectpersonal-latest.tgz

tar xzf globusconnectpersonal-latest.tgz

cd globusconnectpersonal-x.y.z # Replace x.y.z to the version downloaded

globus endpoint create --personal my-linux-laptop

# Use the setup key generated from "endpoint create" above
./globusconnectpersonal -setup 224532bb-8a4b-4d32-8995-e1fb442be98e

globus login
```
Copy & paste resulting URL to browser, obtain Authorization code and enter this at the command line where you did “globus login”. You are now able to log in from this particular Globus CLI instance.

#### After configuring local endpoint, search for local endpoints
 ```
globus endpoint search --filter-scope my-endpoints
```
#### Start Globus Connect Personal
```
cd globusconnectpersonal-2.3.5
./globusconnectpersonal -start &
```
#### List directory contents on local endpoint as a test
```
globus ls 4c8d7b04-5783-11e8-9101-0a6d4e044368
```

### Transfer some data, first using Globus Tutorial Endpoints
create an alias for tutorial endpoint: 
```
go2=ddb59af0-6d04-11e5-ba46-22000b92c6ec
```
or search for them using:
```
globus endpoint search tutorial
```

#### Activate "globus tutorial endpoint"
```
globus endpoint activate $go2
```

#### Transfer file from local dir to tutorial endpoint
```
localE=4c8d7b04-5783-11e8-9101-0a6d4e044368 #local Endpoint ID
globus transfer -r $localE:/test.txt $go2:/
```
