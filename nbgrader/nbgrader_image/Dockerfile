FROM phaustin/autotest:v0.5
USER ${NB_USER}
WORKDIR ${HOME}

RUN echo "Moving nbgrader_config.py into home"
COPY --chown=${NB_USER}:${NB_USER} ./nbgrader_config.py ${HOME}/
