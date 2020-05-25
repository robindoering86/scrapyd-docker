FROM mhart/alpine-node:8
EXPOSE 8888 8889


# Install Scrapoxy
RUN npm install -g scrapoxy


RUN mkdir -p /etc/scrapoxy
# Add configuration
ADD conf/config_default.json /etc/scrapoxy/config.json


# Start scrapoxy
CMD scrapoxy start /etc/scrapoxy/config.json -d
