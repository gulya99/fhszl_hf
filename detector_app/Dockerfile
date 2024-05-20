FROM python:3.6.15-slim-buster
RUN pip3 install flask flask_wtf wtforms requests werkzeug flask_uploads
RUN useradd pythonuser -ms /bin/bash
WORKDIR /home/pythonuser/app
USER pythonuser
COPY app.py app.py
CMD python -u app.py
