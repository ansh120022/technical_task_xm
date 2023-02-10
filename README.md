# Run server

```
cd webapp
pip install -r requirements.txt
uvicorn main:app --reload --log-config="log.ini"
```

run web add in container:

cd webapp

docker build -t webappimage .

docker run -d --name webapp -p 80:80 webappimage

export TEST_APP_URL=http://localhost
