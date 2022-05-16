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

ansible-playbook -i hosts.yml -l n1x node_setup.yml 

* check 

ansible n1x -u root -i hosts.yml  -m ansible.builtin.shell -a 'cat /root/.ssh/authorized_keys'

* using lookup/query

You can use ansible-doc -t lookup -l to see the list of available plugins. Use ansible-doc -t lookup <plugin name> to see specific documents and examples.

https://docs.ansible.com/ansible/latest/plugins/lookup.html
