# Install/Authenticate/Deploy Globus Endpoint
[Following Admin Install Guide](toolkit.globus.org/toolkit/docs/latest-stable/admin/install/)

## Prerequisites
```
sudo wget http://www.globus.org/ftppub/gt6/installers/repo/globus-toolkit-repo-latest.noarch.rpm
sudo rpm -hUv globus-toolkit-repo-latest.noarch.rpm
```

Install Auxilary packages
```
sudo yum install globus-data-management-client
```

## Basic Security Configuration
Host credentials must:

- consist of the following two files: hostcert.pem and and hostkey.pem
- be in the appropriate directory for secure services: /etc/grid-security/
- match the hostname for a the machine. If the machine is going to be accessed remotely, the name on the certificate must match the network-visible hostname.

### There are 2 options
#### 1. Request a certificate from an existing CA
[how-to](http://toolkit.globus.org/toolkit/docs/latest-stable/gsic/admin/index.html#gsic-configuring)

#### 2. SimpleCA
This wrapper around OpenSSL CA should come installed with GlobusToolkit. Otherwise, [install SimpleCA](http://toolkit.globus.org/toolkit/docs/latest-stable/admin/install/appendix.html#gtadmin-simpleca)

[Install SimpleCA](http://toolkit.globus.org/toolkit/docs/latest-stable/admin/install/appendix.html#simpleca-admin-installing)
```
sudo yum install globus-simple-ca globus-gsi-cert-utils-progs
```
[Setup Host Credentials](http://grid.ncsa.illinois.edu/myproxy/fromscratch.html#simpleca_setup)

Request a certificate for localhost
```
sudo grid-cert-request 
```

Create a certificate
```
grid-ca-create
--> Do you want to keep this as the CA subject (y/n) [y]: y
--> Enter the email of the CA (this is the email where certificate
requests will be sent to be signed by the CA)
---> Set the CA certificate expiration date [default: 5 years 1825 days]
```

The grid-ca-package command can be used to generate RPM, debian, or legacy GPT packages for a SimpleCA, or for any other CA which is installed on a host. These packages can make it easy to distribute the CA certificate and policy to other hosts with which you want to establish Grid trust relationships.
[More info on this step](http://toolkit.globus.org/toolkit/docs/latest-stable/simpleca/admin/index.html#grid-ca-package)
```
grid-ca-package
```

Before signing, it might be good to examine the Certificate Request
```
# Execute @ ./home/USERNAME/.globus
openssl req -noout -text -in usercert_request.pem 

```

Sign the certificate
```
# Execute @ ./home/USERNAME/.globus
grid-ca-sign -in usercert_request.pem -out hostsigned.pem
```

### Add Authorization
Installing Globus services on your resources doesn’t automatically authorize users to use these services. Each user must have their own user certificate, and each user certificate must be mapped to a local account.

To add authorizations for users, you’ll need to update the grid-mapfile database to include the mapping between the credentials and the local user accounts database to include the mapping between the credentials and the local user accounts.

You’ll need two pieces of information:
- the subject name of a user’s certificate
- the local account name that the certificate holder can access.

To start with, if you have created a user certificate, you can run the grid-cert-info command to get the certificate’s subject name, and id -un to get the account name:
```
# Execute @ ./home/USERNAME/.globus
$ grid-cert-info -subject
```
STDOUT:
/O=Grid/OU=GlobusTest/OU=simpleCA-elephant.globus.org/CN=Globus User

```
$ id -un
```
STDOUT:
globus



# Alternative Install: [Globus Connect Server](https://docs.globus.org/globus-connect-server-installation-guide/)
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

```

Send data to and from endpoint using [Web Interface](https://www.globus.org/app/transfer)
