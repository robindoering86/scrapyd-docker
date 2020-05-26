# About
This is a demo scrapy project which can be deployed to a remote (or local) srapyd server. It will make a couple of useless requests to httpbin.org and write the "scraped" data to the MongoDB database specified by the `MONGO_URI` parameter in `examples/scrapy_test/settings.py`.

If you want to use `scrapoxy`, you must also set the following variables in `examples/scrapy_test/settings.py`:

- `PROXY`: If using the full stack, set this to `http://<username>:<password>@scrapoxy:8888/?noconnect`, where `<username>` and `<password>` are the same as set in `conf/scrapoxy.conf.json`
- `API_SCRAPOXY`: If using the full stack, set this to "http://scrapoxy:8889/api"
- `API_SCRAPOXY_PASSWORD`: This is the "commander" password set in `conf/scrapoxy.conf.json`

Next, eggify your Scrapy project and prepare it to be sent to the scrapyd.

```bash
python setup.py bdist_egg
```
Create the project on the Scrapyd server.

```bash
curl http://<USERNAME>:<PASSWORD>@<SCRAPYD_IP_OR_HOSTNAME>:<PORT>/addproject.json -F project=<SCRAPY_PROJECT_NAME> -F version=<VERSION_NO> -F egg=@dist/project-1.0-py3.7.egg
```
To schedule a spider run execute the following command:
```bash
curl http://<USERNAME>:<PASSWORD>@<SCRAPYD_IP_OR_HOSTNAME>:<PORT>/schedule.json -d project=<SCRAPY_PROJECT_NAME> -d spider=<SCRAPY_SPIDER_TO_RUN>
```
The response will contain the status and jobid.
