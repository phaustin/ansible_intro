FROM phaustin/base:may27

USER ${NB_USER}

RUN mkdir -p ${HOME}/work

COPY jupyter_notebook_config.py /etc/jupyter/

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc
COPY jupyter_notebook_config.py /etc/jupyter/

WORKDIR "${HOME}/work"

RUN touch "/home/jovyan/container_version_may27.txt"


CMD ["jupyterhub-singleuser"]

