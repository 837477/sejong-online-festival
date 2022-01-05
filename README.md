# SOF(Sejong-Online-Festival) 
__세종대학교 비대면 축제 서비스 플랫폼 - ONLINE__
<br /><br />

<div align=center>
  <strong>#</strong> Next.js &nbsp; &nbsp; <strong>#</strong> Styled-Components &nbsp; &nbsp; <strong>#</strong> @reduxjs/toolkit &nbsp; <strong>#</strong> Flask &nbsp; <strong>#</strong> MongoDB
  <br /><br />
</div>

![image](https://user-images.githubusercontent.com/47492535/144883212-5a942554-9a89-4468-8752-7f4f36cfd2e7.png)
![image](https://user-images.githubusercontent.com/47492535/144883244-5793d44c-87c7-4c38-84de-e1ba75d36eb4.png)
![image](https://user-images.githubusercontent.com/47492535/144883283-1eb064e9-fa39-4580-b0a5-b000b5ddbf78.png)
![image](https://user-images.githubusercontent.com/47492535/144883307-330c52d1-cdad-4f27-b141-46f874f46ae1.png)
![image](https://user-images.githubusercontent.com/47492535/144883339-10a81699-b2a4-45c8-9a29-081a7bea41d1.png)
![image](https://user-images.githubusercontent.com/47492535/144883382-8cfd31d6-3824-4ff9-8152-c13da11347fe.png)

<br /><br />

## Dependency

- **python 3.6+**
- **Flask==2.0.1**
- **flask-validation-extended==0.1.5**
- **pymongo==3.11.4**
- **python-dotenv==0.17.1**



## Environment variable
SOF_PHOTO_UPLOAD_PATH는 static URL을 사용하기 위해, app/asset/ 내에 지정하는 걸 추천.

```
SOF_MONGODB_NAME="SOF"
SOF_MONGODB_URI="mongodb://localhost:27017"
FLASK_APP="manage:application"
FLASK_CONFIG="development" # develop, production
FLASK_ENV="development" # develop, production
SOF_ERROR_LOG_PATH="./server.error.log"
SOF_PHOTO_UPLOAD_PATH="./app/asset/uploads"
SOF_SECRET_KEY="top-secret"
SOF_ADMIN_ID="admin"
SOF_ADMIN_PW="1234"
```



## Get Started

운영체제마다 세부적인 실행방법이 다를 수 있습니다. 

```shell
# Get Repository
$ git clone https://github.com/iml1111/IMFlask-Pymongo
$ cd IMFlask-Pymongo/

# virtual env
$ python3 -m venv venv
$ source ./venv/bin/activate

# Install dependency
$ pip install -r ./requirements/requirements.txt

$ cd IMFlask/

# DB init
$ flask db-init
[IMFlask] MongoDB Initialization Completed.

# App test
$ flask test
test_app_exists (test_basics.BasicsTestCase)
Application 검증 테스트 ... ok
...

# App start
$ flask run
```



##  Controller

- SejongAuth

```python
from controller.sejong_auth import SejongAuth

auth = SejongAuth()
id, pw = "16011089", "1234"
print(auth.do_sejong(id, pw))
print(auth.portal_sejong(id, pw))
```

