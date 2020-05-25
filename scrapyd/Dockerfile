FROM ubuntu:18.04
ADD requirements.txt /tmp/requirements.txt
RUN apt-get update \
  && apt-get install python3-pip -y \
  && apt-get install -y systemd \
  && apt-get install -y git \
  && apt-get install -y python-dev libxml2-dev libxslt1-dev libffi-dev \
  && apt-get clean 
WORKDIR /scrapy
RUN pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt
ADD conf/scrapyd.conf /etc/scrapyd/scrapyd.conf

EXPOSE 6800

CMD ["scrapyd", "--logfile=/var/log/scrapyd.log", "--pidfile="]
