# scrapyd + nginx rproxy w/ basic auth stack
```bash
git clone git@gitlab.com:ginkgo_analytics/csr-ga_silvester-scraper.git /dir-to-clone-into
cd /dir-to-clone-to
```

## Build the scrapoxy scrapyd docker images

From the base directory change into the scrapoxy directory

```bash
cd scrapoxy
make build
```

Next, build the scrapyd image

```bash
cd ../scrapyd/
make build
```
## Configurering the Docker stack
### Scrapyd
Edit the `conf/scrapyd.env` file .

- `PROXY` parameter. If using the full stack, leave this at default value ("http://scrapoxy:8888/?noconnect"). If you choose to password-protect your scrapoxy proxy, must be of the format ("http://<USER>:<PASSWORD>@scrapoxy:8888/?noconnect")

- `API_SCRAPOXY`: If using the full stack, leave this at default value. ("http://scrapoxy:8889/api")

- `API_SCRAPOXY_PASSWORD`: The "commander" password set in scrapoxy config. Password to protect the access to the scrapoxy API

### Scrapoxy

Edit the `conf/scrapoxy.config.json` files to your needs. It is preconfigured to be run with AWS EC2 in the EU-West1 region. If you need the proxy to run in a different region, see (https://scrapoxy.readthedocs.io/en/master/standard/providers/awsec2/copy_ami_to_region/index.html)[description] on how to copy the scrapoxy image to another region. 

You must edit the following parameter in the `conf/scrapoxy.config.json` file:

- In the `commander` section, change the `password` key. Must be the same as the `API_SCRAPOXY_PASSWORD` in the scrapyd `conf/scrapyd.env` file.

- In the `aws2` sectio of the `providers` list: Change `accessKeyId` and `secretAccessKey` to your apropiate values.

- In the `proxy` section. Change `username` and `password` keys if you wish to password-protect your proxy. If not, delete the keys. `username` and `password` must be the same as in the `PROXY` variable the scrapyd `conf/scrapyd.env` file.

Example `conf/scrapoxy.config.json` file: 

```json
{
    "commander": {
        "port": 8889,
        "password": "DEFAULT_PW"
    },
    "instance": {
        "port": 3128,
        "scaling": {
            "min": 1,
            "max": 5
        }
    },
    "providers": [
        {
            "type": "awsec2",
            "accessKeyId": "YOUR_AWS_ACCESS_KEY_ID",
            "secretAccessKey": "YOUR_AWS_ACCESS_KEY",
            "region": "eu-west-1",
            "instance": {
                "InstanceType": "t2.micro",
                "ImageId": "ami-485fbba5",
                "SecurityGroups": [
                    "forward-proxy"
                ]
            }
        }
    ],
    "proxy": {
        "port": 8888,
        "auth": {
            "username": "DEFAULT_USER",
            "password": "DEFAULT_PW"
        }
    }
}
```
## Run the stack

```bash
docker-compose up -d
```

Scrapoxy should now be accessible using your EC2 instances public IP (`http://<YOUR_EC2_IP>:8889/). Use the `API_SCRAPOXY_PASSWORD` password to login (if set).

The proxy can now be used as standalone or (for web crawling) in conjunction with Scrapyd. Examples on how to use Scrapyd can be found in the `examples` folder.
