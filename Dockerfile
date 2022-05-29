FROM python:3.7.13-slim-buster

RUN mkdir /opt/fast
WORKDIR  /opt/fast
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
COPY requirements.txt .
RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/cpu
COPY . .
EXPOSE 8080
CMD ["python","app.py"]