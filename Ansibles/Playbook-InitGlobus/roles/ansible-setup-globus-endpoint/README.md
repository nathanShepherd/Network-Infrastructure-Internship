# Install/Authenticate and Deploy a Globus Endpoint
This role allow the user rapid deployment of Globus Connect Server. Globus is popular implimentation of GridFTP that already has many clusters around the world.

**Globus self endorsment:**
Globus allows you, as a resource provider, to easily offer reliable, secure, high-performance research data management capabilities to your users and their collaborators, directly from your own storage. Globus is software-as-a-service (SaaS), enabled by the cloud and designed to let users manage their research files, regardless of number and size, as effortlessly as they manage their photos with popular cloud-based services. Globus lets you provide authorized users with web, command line, and REST interfaces for listing, transferring, replicating, and sharing directories and files on your Globus-connected storage resources. 

# How to setup a [Globus Connect Server](https://docs.globus.org/globus-connect-server-installation-guide/)
TODO: [Configure Globus Connect Server](https://docs.globus.org/globus-connect-server-installation-guide/#globus_connect_server_configuration)

## TODO [Open TCP Ports](https://docs.globus.org/globus-connect-server-installation-guide/#test_basic_endpoint_functionality)

## Install Globus Connect Server

#### Request latest version of software via HTTP
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
