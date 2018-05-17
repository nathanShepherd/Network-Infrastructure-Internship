# Install/Authenticate/Deploy Globus Endpoint: [Globus Connect Server](https://docs.globus.org/globus-connect-server-installation-guide/)

## [Open TCP Ports](https://docs.globus.org/globus-connect-server-installation-guide/#test_basic_endpoint_functionality)

## Install Globus Connect Server
```
sudo curl -LOs https://downloads.globus.org/toolkit/globus-connect-server/globus-connect-server-repo-latest.noarch.rpm
sudo rpm --import https://downloads.globus.org/toolkit/gt6/stable/repo/rpm/RPM-GPG-KEY-Globus
sudo yum install globus-connect-server-repo-latest.noarch.rpm
```

#### Install EPEL repository and Prerequisite packages
```
sudo curl -LOs https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum install epel-release-latest-7.noarch.rpm
sudo yum install yum-plugin-priorities
```

#### Install Globus Connect Server
```
sudo yum install globus-connect-server
```

## Create Globus Endpoint
Before creating your Globus server endpoint, choose a suitable second part for your endpoint name. Then, edit the Globus Connect Server configuration file, */etc/globus-connect-server.conf*, and set *Name* to your choice (umich_network_infrastructure in the example shown), and *Public to True*. These two changes in the *[Endpoint]* section of the file will allow authorized users to find and access your endpoint.
```
[Endpoint]
Name = umich_network_infrastructure
Public = True
```
After editing config file, run
```
sudo globus-connect-server-setup
```
When prompted, enter the Globus username and password for your [Globus organization account](https://docs.globus.org/globus-connect-server-installation-guide/#organization-account-anchor). When the globus-connect-server-setup command completes, your Globus endpoint is ready to be accessed by users with logins on your system.

## [Verify globus-gridftp-server Service](https://docs.globus.org/globus-connect-server-installation-guide/#test_basic_endpoint_functionality)
```
ps aux | grep globus-gridftp-server
```
If you do not see an instance of globus-gridftp-server running, then the service has not started. 

You can also verify myproxy-server Service
```
ps aux | grep myproxy-server
```

Send data to and from endpoint using [Web Interface](https://www.globus.org/app/transfer)
