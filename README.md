# Users API written with Python and MONGODB

```
git clone

cd <project>

pip3 install -r requirements.txt

python3 app.py
```


# ENV
```dotenv
SECRET_KEY = YOUR_SECRET_KEY
MONGO_URI = YOUR_MONGODB_URL
```


# USING docker
```docker
docker build -t image_name .

docker run -e SECRET_KEY="YOUR_SECRET_KEY" -e MONGO_URI = "YOUR_MONGODB_URL"  image_name:latest


```