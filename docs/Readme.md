# bootstrap a node

## move a keypair

* in node_setup.yml:

---
- hosts: all
  become: true
  vars: 

  tasks:
    - name: Set authorized key taken from file
      ansible.posix.authorized_key:
        user: root
        state: present
        exclusive: True
        key: "{{ lookup('file', lookup('env','HOME') + '/.ssh/tlef_summer.pub') }}"
      tags:
        - step1

* execute

ansible-playbook -i ~/repos/ansible_galaxy/phaustin/hosts.yaml -l n1x node_setup.yml 

* check 
