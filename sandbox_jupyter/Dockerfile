FROM jupyter/minimal-notebook:python-3.11

USER ${NB_UID}
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
