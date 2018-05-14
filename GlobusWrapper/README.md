# Configure Server and Client for Globus GridFTP

## Following Setup Tutorial from JASMIN @ https://bit.ly/2jTSk2A
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
