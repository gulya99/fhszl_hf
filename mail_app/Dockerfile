FROM python:latest
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install flask redis
RUN useradd pythonuser -ms /bin/bash
WORKDIR /home/pythonuser/app
USER pythonuser
COPY templates templates/
COPY app.py app.py
CMD python -u app.py
