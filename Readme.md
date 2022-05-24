1) new node on digital ocean

ansible -i hosts.yml -u root do1x -m ping

ansible-playbook  -i hosts.yml -u root -l do1x setup_jovyan.yml

ansible-playbook  -i hosts.yml -u root -l do1x setup_docker.yml

ansible-playbook  -i hosts.yml -u jovyan -l do1x setup_conda.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x setup_git.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x setup_traefik.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x --vault-password-file ~/.vault_pass  start_traefik.yml

ansible-playbook -i hosts.yml -u jovyan -l do1x  test_ansible.yml


* ansible adhoc command

ansible -i hosts.yml -u root do1x -m ping


ansible-vault encrypt_string create  --output do_encrypt.txt --show-input --prompt --ask-vault-pass

https://www.digitalocean.com/community/tutorials/how-to-use-vault-to-protect-sensitive-ansible-data#using-ansible-vault-with-a-password-file

echo 'my_vault_password' > ~/.vault_pass

ansible-vault encrypt_string --vault-password-file ~/.vault_pass e5c493f1c8e9d264cc5d7c5dfe2809fd264f5efd73d1d07d7b0f40c716e4bb21 --name DO_AUTH_TOKEN --output ~/encrypt.txt

