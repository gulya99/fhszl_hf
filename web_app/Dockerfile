FROM python:3.6.15-slim-buster
RUN pip3 install --upgrade pip3
RUN pip3 install flask requests opencv-python
RUN useradd pythonuser -ms /bin/bash
WORKDIR /home/pythonuser/app
USER pythonuser
COPY app.py app.py
COPY templates templates/
CMD python -u app.py
