FROM python:latest
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install flask requests pyproject-toml opencv-python-headless pika
RUN useradd pythonuser -ms /bin/bash
RUN mkdir -p /home/pythonuser/app/static/images && chown -R pythonuser:pythonuser /home/pythonuser/app/static/images
RUN mkdir -p /home/pythonuser/app/db && chown -R pythonuser:pythonuser /home/pythonuser/app/db
WORKDIR /home/pythonuser/app
USER pythonuser
COPY app.py app.py
COPY templates templates/
COPY haarcascade_car.xml haarcascade_car.xml
CMD python -u app.py
