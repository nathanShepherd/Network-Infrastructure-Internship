GridFTP
=======
Note: this CentOS port was built @ https://github.com/luisico/ansible-simpleca.git

Install GridFTP servers and clients. The role will:
- Install globus software and dependencies as needed
- Configure gridftp servers
- Main config in /etc/gridftp.conf
- Directory access restrictions in /etc/gridftp.d
- Host cert/key in /etc/grid-security
- CA certificates in /etc/grid-security/certificates
- Complete management of mappings in /etc/grid-security/grid-mapfile
- Start the service and enable it at boot
- Open firewall ports if firewalld is detected
- Install fetch-crl and cronjobs on servers to maintain revocation lists
- Install UberFTP of clients

Choose the mode to work by setting `gridftp_mode` to `server` (default) or `client`.

By default no anonymous users are allowed, set `gridftp_allow_anonymous: no` and change the `gridftp_anonymous_user` of your choice (defaults to `nobody`).

In order to make GridFTP usable you will need to deploy several certificates in both server and client.

For the server you will need:
- CA certificates used to create the host certificate,
- CA certificates used to create the user certificates presented by the clients.
- Other CA certificates you trust.
- Valid host certificate and private key.

For the client you will need:
- CA certificates used to create the server's host certificate.
- CA certificates used to create the user certificate.
- Other CA certificates you trust.
- User certificates.

CA certificates can be deployed in two ways to both servers and clients: using certificate repositories from known CA sources or installing locally trusted CA certificates.

You probably want to install packages repositories from known CA sources, ie EGI, IGTF, EUGridPMA, APGridPMA or TAGPMA. Each repository should be listed in `gridftp_ca_cert_repos` along with a list of packages to install. For example:
```
gridftp_ca_cert_repos:
  - name: EGI-trustanchors
    baseurl: http://repository.egi.eu/sw/production/cas/1/current/
    gpgkey: http://repository.egi.eu/sw/production/cas/1/GPG-KEY-EUGridPMA-RPM-3
    packages:
      - ca-policy-egi-core
```

Local trusted CA certificates can also be installing by listing them in `gridftp_ca_local_certs` along with their subject and signing policy. For example:
```
gridftp_ca_local_certs:
  - name: my_certificate
    subject: '/O=Grid/OU=GlobusTest/CN=Globus Simple CA'
    policy: '/O=Grid/OU=GlobusTest/*'
    cert_file: path/to/certificate
```

Alternatively you can also specify the certificate's content instead of pointing to a file:

```
    cert: |
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
```
If both `cert_file` and `cert` are specified, `cert_file` will take overwrite `cert`. Leaving both options undefined will try to just change the signing policy using an already existant certificate with the filename equal to the name specified.

You should ask your local CA representative for host (for server) and user (for client) certificates. Once you have a valid host (trusted by your CA) and its accompanying private key install with variables `gridftp_host_cert` and `gridftp_host_key` (possible holding the host key in the vault).

This role manages globus' `grid-mapfile` directly without the use of grid-mapfile- tools. Only mappings defined in `gridftp_mapping` will get globus authorization. For example:
```
gridftp_mappings:
  - ln: vagrant
    dn: '/O=Grid/OU=GlobusTest/CN=vagrant'
```

Installation of fetch-crl (on the server) and UberFTP (on the client) are managed by `gridftp_fetchcrl` and `gridftp_uberftp`.

Requirements
------------
See `meta/main.yml`.

Role Variables
--------------
See `defaults/main.yml`.

Dependencies
------------
None.

Example Playbook
----------------
Example:
```
- hosts: gridftp-servers
  roles:
  - gridftp

- hosts: gridftp-clients
  roles:
  - gridftp
```

TODO
----
- Threading on clients
- xinetd conf or gfork
- Set gridftp_instances in xinetd/gfork conf or command line
- Tune host: http://fasterdata.es.net/host-tuning/
- Use udt instead of tcp?
- strped and cluster-to-cluster setup
- chroot
- Enable confidential communication (encryption)?
- Get all certs in igtf or terana?
- Make elixir CA the default
- Create host cert/key from custom CA
- Cron job for revocation list
- Firewall
- Manage grid-mapfile with grid-mapfile-add-entry and grid-mapfile-delete-entry tools
- Document default variables

Licence
-------
Licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Author Information
------------------
Luis Gracia <luis.gracia@ebi.ac.uk>
