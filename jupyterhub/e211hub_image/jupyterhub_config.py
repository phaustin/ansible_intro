# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.Authenticator.admin_users = {'phaustin'}
# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'e211hub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
# c.DockerSpawner.image = 'phaustin/e211book:sep11'
c.DockerSpawner.allowed_images = {'e211' : 'phaustin/e211book:may27' }
notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'traefik_net'
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir,
                          "/home/jovyan/repos/ansible_intro/jupyterhub/data_share": 
                           {"bind": "/home/jovyan/work/data_share", "mode": "rw"}}

# delete containers when the stop
c.DockerSpawner.remove = True

