# Ansible Roles for Sys Admin Automation
Roles allow more than just tasks to be packaged together and can include variables, handlers, or even modules and other plugins. Unlike includes and imports, roles can also be uploaded and shared via Ansible Galaxy.

### First, install Ansible to your local machine
```
sudo yum install ansible
```

#### Setup an Ansible Inventory (hostgroup)
- Run server configuration remotely
- Use Ed's example playbook perfSonar 
- Take roles out subdirectory and make it's own repo
- Push repo to ansible galaxy 
- Get the role and install at nateshep/.ansible

#### Configure a Server on EC2 remotely via ssh


### Initialize a New Role
```
$ mkdir ansible-role-NEW_ROLE
$ cd ansible-role-NEW_ROLE
$ ansible-galaxy init
```

### Ping Localhost!!!
```
ansible localhost -m ping -e 'ansible_python_interpreter="/usr/bin/env python"'
```

### Get Ansible role from galaxy.ansible.com
```
Install @ /etc/ansible/roles
$ ansible-galaxy install username.rolename

Install @ localDir
$ ansible-galaxy install --roles-path . username.rolename
```




