from oauthenticator.github import GitHubOAuthenticator
from pathlib import Path

# dummy for testing. Don't use this in production!
# c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.Authenticator.admin_users = {'phaustin'}
# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'e211hub'

# pick a docker image. This should have the same version of jupyterhub
# two identical entries here to show image choice pulldown menue
c.DockerSpawner.allowed_images = {'e211' : 'phaustin/e211book:may27',
                                  'a405' : 'phaustin/e211book:may27'}
notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'traefik_net'
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir,
                          "/home/jovyan/repos/ansible_intro/jupyterhub/data_share": 
                           {"bind": "/home/jovyan/work/data_share", "mode": "rw"}}

# delete containers when the stop
c.DockerSpawner.remove = True

c.Authenticator.allowed_users = allowed = set()
c.Authenticator.admin_users = admin = set()

curr_dir = Path()
user_list = curr_dir / 'user_list.txt'

with open(user_list,'r') as f:
   all_lines=f.readlines()
   for the_line in all_lines:
      parts=the_line.split(';')
      username=parts[0].strip()
      allowed.add(username)
      if len(parts) > 1 and parts[1] == 'admin':
         admin.add(username)
   

