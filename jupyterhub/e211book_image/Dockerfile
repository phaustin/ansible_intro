FROM phaustin/base:may27

USER ${NB_USER}

RUN mkdir -p ${HOME}/work

RUN mkdir -p ${HOME}/work/data_share

COPY jupyter_notebook_config.py /etc/jupyter/

WORKDIR "${HOME}/work"

RUN touch "/home/jovyan/container_version_may27.txt"


CMD ["jupyterhub-singleuser"]

