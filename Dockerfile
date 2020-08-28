FROM ubuntu
RUN mkdir /code
WORKDIR /code
# ADD sources.list /code/
# RUN cp sources.list /etc/apt/sources.list
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-dev default-libmysqlclient-dev -y 
RUN apt-get install libmysqlclient-dev -y
RUN apt-get install python3-pip -y
# RUN pip install pip -U
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
ADD . /code/
