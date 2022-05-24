# Introduction to ansible

This repository contains a set of ansible playbooks that builds a docker-powered conda environment and runs a plotly dash server over https using letsencrypt.

## Prerequisites

* An Ubuntu 20.04 droplet on Digital Ocean (Regular, 2 Gbytes Ram, 50 Gbyte SSD, $US 0.015/hour)

* A domain name managed by Digital Ocean ($1/12 months at https://www.namecheap.com/ )

* A Digital Ocean Personal Access api token

## File edits

* replace `ansible_host`, `ansible_ssh_private_key_file` with your node ip address and private key files in [playbooks/host.yml](playbooks/host.yml)

* 


1) new node on digital ocean


ansible-playbook  -i hosts.yml -u root -l do1x setup_jovyan.yml

ansible-playbook  -i hosts.yml -u root -l do1x setup_docker.yml

ansible-playbook  -i hosts.yml -u jovyan -l do1x setup_conda.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x setup_git.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x setup_traefik.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x  start_traefik.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x  setup_dashboards.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x  start_dashboards.yml

R
* tools


* ansible adhoc command

ansible -i hosts.yml -u root do1x -m ping


ansible-playbook -i hosts.yml -u jovyan -l do1x  test_ansible.yml


ansible-vault encrypt_string create  --output do_encrypt.txt --show-input --prompt --ask-vault-pass

https://www.digitalocean.com/community/tutorials/how-to-use-vault-to-protect-sensitive-ansible-data#using-ansible-vault-with-a-password-file

echo 'my_vault_password' > ~/.vault_pass

ansible-config   init --disabled -t all > ~/.ansible.cfg

ansible-vault encrypt --encryhpt-vault-id traefik vault.yml


