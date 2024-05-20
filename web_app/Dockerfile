FROM python:latest
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install flask requests pyproject-toml opencv-python-headless
RUN useradd pythonuser -ms /bin/bash
RUN usermod -aG sudo pythonuser
WORKDIR /home/pythonuser/app
USER pythonuser
COPY app.py app.py
COPY templates templates/
COPY images images/
CMD python -u app.py
