Run the playbook with the following incantation:
```

ansible-playbook main.yml --user root --ask-pass

# flag -i [HOST_FILE] points to "inventory"

ansible-playbook -i hosts main.yml
```
