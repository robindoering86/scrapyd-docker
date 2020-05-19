FROM ubuntu:18.04
ADD requirements.txt /tmp/requirements.txt
RUN apt-get update \
  && apt-get install python3-pip -y \
  && apt-get install -y systemd \
  && apt-get install -y git \
  && apt-get clean
RUN pip3 install virtualenv \
  && pip3 install scrapyd
WORKDIR /scrapy
RUN pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt
ADD conf/scrapyd.conf /etc/scrapyd/scrapyd.conf
#ADD scrapy.service /etc/systemd/system/scrapy.service
#CMD systemctl enable scrapy.service

EXPOSE 6800
#CMD ["service", "scrapy", "start"]

#CMD ["scrapyd"]
CMD ["scrapyd", "--logfile=/var/log/scrapyd.log", "--pidfile="]
