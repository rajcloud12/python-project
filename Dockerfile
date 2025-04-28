FROM debian:latest
RUN apt update && apt install -y \
python3 \
python3-pip
MAINTAINER Raj
WORKDIR /app
COPY . /app
CMD ["python3", "app.py"]
