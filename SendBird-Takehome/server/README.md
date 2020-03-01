# SBTakehome 


## 1. package install

```
pip install virtualenv
virtualenv env
source env/bin/activate
env/bin/pip install -r requirements.txt
```

## 2. Set server protocol

```
- Add webhooks URL on the sendbird's setting
- http://ec2-3-14-80-55.us-east-2.compute.amazonaws.com:5000

```
## 3. start SBTakehome

```
python sbtakehome.py
```

## 4. api TEST

- sb take home : http://localhost:5000
- To use sb sdk : http://ec2-3-14-80-55.us-east-2.compute.amazonaws.com:5000
- Use client's index.html of basic web sample
