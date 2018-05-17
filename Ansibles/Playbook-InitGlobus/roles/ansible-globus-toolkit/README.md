# Install/Authenticate/Deploy Globus Endpoint
Following Admin Install Guide @ toolkit.globus.org/toolkit/docs/latest-stable/admin/install/`

## Prerequisites
```
sudo wget http://www.globus.org/ftppub/gt6/installers/repo/globus-toolkit-repo-latest.noarch.rpm
sudo rpm -hUv globus-toolkit-repo-latest.noarch.rpm
```
For operating systems based on RHEL (such as Red Hat Enterprise Linux, CentOS, and Scientific Linux), the compatible EPEL repository must be enabled before installing myproxy. 
```
http://fedoraproject.org/wiki/EPEL/FAQ#How%5fcan%5fI%5finstall%5fthe%5fpackages%5ffrom%5fthe%5fEPEL%5fsoftware%5frepository.3F

```

## Install Globus Toolkit on Linux
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
```
http://toolkit.globus.org/toolkit/docs/latest-stable/gsic/admin/index.html#gsic-configuring
```
#### 2. SimpleCA
This wrapper around OpenSSL CA should come installed with GlobusToolkit. Otherwise, (install SimpleCA)[http://toolkit.globus.org/toolkit/docs/latest-stable/admin/install/appendix.html#gtadmin-simpleca]

Install SimpleCA
```
sudo yum install globus-simple-ca globus-gsi-cert-utils-progs
```
(Setup Host Credentials)[from http://grid.ncsa.illinois.edu/myproxy/fromscratch.html#simpleca_setup]

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
```
(grid-ca-package)[http://toolkit.globus.org/toolkit/docs/latest-stable/simpleca/admin/index.html#grid-ca-package]
```

Sign the certificate
```
grid-ca-sign -in /home/nateshep/.globus/usercert_request.pem -out hostsigned.pem
```

### Add Authorization
Installing Globus services on your resources doesn’t automatically authorize users to use these services. Each user must have their own user certificate, and each user certificate must be mapped to a local account.

To add authorizations for users, you’ll need to update the grid-mapfile database to include the mapping between the credentials and the local user accounts database to include the mapping between the credentials and the local user accounts.

You’ll need two pieces of information:
- the subject name of a user’s certificate
- the local account name that the certificate holder can access.

To start with, if you have created a user certificate, you can run the grid-cert-info command to get the certificate’s subject name, and id -un to get the account name:

















