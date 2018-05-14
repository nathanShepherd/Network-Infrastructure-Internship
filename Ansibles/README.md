# Ansible Roles for Sys Admin Automation
Roles allow more than just tasks to be packaged together and can include variables, handlers, or even modules and other plugins. Unlike includes and imports, roles can also be uploaded and shared via Ansible Galaxy.

### First, install Ansible to your local machine
```
sudo yum install ansible
```

### Initialize a New Role
```
$ mkdir ansible-role-NEW_ROLE
$ cd ansible-role-NEW_ROLE
$ ansible-galaxy init
```

### Get Ansible role from galaxy.ansible.com
```
Install @ /etc/ansible/roles
$ ansible-galaxy install username.rolename

Install @ localDir
$ ansible-galaxy install --roles-path . username.rolename
```




