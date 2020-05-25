FROM mhart/alpine-node:8
EXPOSE 8888 8889


# Install Scrapoxy
RUN npm install -g scrapoxy


# Add configuration
ADD conf/config_default.json config.json


# Start scrapoxy
CMD scrapoxy start config.json -d
