# About
This is a demo scrapy project which can be deployed to a remote (or local) srapyd server. It will make a couple of useless requests to httpbin.org and write the "scraped" data to the MongoDB database specified by the `MONGO_URI` parameter in scrapy_test/settings.cfg.

```bash
python setup.py bdist_egg
```
 
```bash
curl http://<USERNAME>:<PASSWORD>@<SCRAPYD_IP_OR_HOSTNAME>:<PORT>/addproject.json -F project=<SCRAPY_PROJECT_NAME> -F version=<VERSION_NO> -F egg=@dist/project-1.0-py3.7.egg
```
To schedule a spider run execute the following command:
```bash
curl http://<USERNAME>:<PASSWORD>@<SCRAPYD_IP_OR_HOSTNAME>:<PORT>/schedule.json -d project=<SCRAPY_PROJECT_NAME> -d spider=<SCRAPY_SPIDER_TO_RUN>
```
The response will contain the status and jobid.
