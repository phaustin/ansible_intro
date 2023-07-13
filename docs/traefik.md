# traefik step by step

* creae droplet on do
* assign reserved ip 24.199.78.126
* add ip address to entry do1x  in ~/playbooks/hosts.yml
* on digital ocean assign ip address to eoastest.xyz, web.eoastest.xyz and dashboard.eoastest.xyz
* add pub and private keys for do1x to ~/.ssh/
* test ping
  - `ansible -i playbooks/hosts.yml -i playbooks/hosts.yml -u root do1x -m ping`
* setup jovyan
  - `ansible-playbook -i hosts.yml -u root -l do1x setup_jovyan.yml`
* add hosts to ~/.ssh/config on local machine

        Host do1root
             IdentityFile ~/.ssh/do1_feb27
             HostName     24.199.78.126
             UserKnownHostsFile ~/.ssh/do_root_hosts
             User         root
             IdentitiesOnly yes

        Host do1jov
             IdentityFile ~/.ssh/do1_feb27
             HostName     24.199.78.126
             UserKnownHostsFile ~/.ssh/do_jov_hosts
             User         jovyan
             IdentitiesOnly yes

* setup git
  - `ansible-playbook -i hosts.yml -u jovyan -l do1x setup_git.yml`
* setup traefik
  - `ansible-playbook -i hosts.yml -u jovyan -l do1x setup_traefik.yml`
* start traefik
  - `ansible-playbook -i hosts.yml -u jovyan -l do1x start_traefik_noauth.yml`
