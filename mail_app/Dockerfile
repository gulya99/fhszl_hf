FROM python:latest
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install flask Flask-Mail redis
RUN useradd pythonuser -ms /bin/bash
WORKDIR /home/pythonuser/app
USER pythonuser
COPY app.py app.py
COPY templates templates/
CMD python -u app.py
