# Configure Server and Client for Globus GridFTP

## Full Tutorial with most peices from JASMIN @ https://bit.ly/2jTSk2A
#### Set up Globus CLI on end-user machine
```
pip install --upgrade --user globus-cli

```
#### Authenticate local endpoint
```
globus login
```
Copy & paste resulting URL to browser, obtain Authorization code and enter this at the command line where you did “globus login”. You are now able to log in from this particular Globus CLI instance.

#### Initialize local endpoint
```
wget https://bit.ly/2Kkk9wn

tar xzf globusconnectpersonal-latest.tgz

cd globusconnectpersonal-x.y.z # Replace x.y.z to the version downloaded

globus endpoint create --personal my-linux-laptop

# Use the setup key generated from "endpoint create" above
./globusconnectpersonal -setup 224532bb-8a4b-4d32-8995-e1fb442be98e

```
If setup fails due to ERROR: /usr/bin/env: python2: No such file or directory
```
# Confirm python2.x is installed and linked to $PATH
python --version

# Create a symbolic link
ln -s /usr/bin/python /usr/local/bin/python2
```

#### Start Globus Connect Personal
```
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
#### Locate a local Endpoint
```
globus endpoint search --filter-scope my-endpoints
```
#### Transfer file from local dir to tutorial endpoint
```
localE=4c8d7b04-5783-11e8-9101-0a6d4e044368 #local Endpoint ID
globus transfer -r $localE:/test.txt $go2:/
```
Endpoints can easily be deleted
```
globus endpoint delete [OPTIONS] ENDPOINT_ID
```
