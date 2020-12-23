# Modovision private proxy pool
- [x] mongodb
- [x] [mongo express (GUI)](http://172.16.16.103:8082/)
- [x] [scylla](https://github.com/imWildCat/scylla)
- [x] automatically check the ips in proxy pool (located in mongo)
- [ ] visualized the process of automation (e.g. airflow ..etc)

# Usage scylla:
scylla is an open source api from [here](https://github.com/imWildCat/scylla) 

## python
```python
import requests
res_json = reqests.get("http://172.16.16.103:8899/api/v1/proxies").json()

print(res_json)
```
### Then the schema of the respond json object is as follow:
```json
{
    "proxies":[
        {
            "id":206,
            "ip":"116.58.237.87",
            "port":8080,
            "is_valid":true,
            "created_at":1608271848,
            "updated_at":1608272458,
            "latency":117.0,
            "stability":1.0,
            "is_anonymous":false,
            "is_https":false,
            "attempts":1,
            "https_attempts":0,
            "location":"24.9889,121.3176","organization":"HiNet",
            "region":"Taoyuan",
            "country":"TW",
            "city":"Taoyuan District"
        },
        {
            .........
        }    
    ],
    "count": counts of proxies,
    "per_page": per page number of proxies,
    "page": now page,
    "total_page": total page
}
```
to get more api information please check [here](https://github.com/imWildCat/scylla)
---
# Usage of the Automation check proxy:
```cmd
./start.sh
```
