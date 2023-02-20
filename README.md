poetry new api --name src
cd api/
poetry add fastapi 
poetry add uvicorn[standard]
poetry add requests
poetry add pytest
poetry add torch
poetry add black isort pytest httpx
poetry add diffusers
poetry add transformers
poetry add joblib
poetry add kubernetes

# Build container image
docker build -t capstone_api:1.1 .

# Run container image
docker run --rm --name capstone_api -p 8000:8000 -d capstone_api:1.1

# Push image to dockerhub
# from mids_capstone_api 
docker tag capstone_api:1.1 rmitchell88/capstone_api:1.1
docker login
docker push rmitchell88/capstone_api:1.1

# On VM terminal
docker pull rmitchell88/capstone_api:1.1
docker run --rm --name capstone_api --ipc=host --net=host -v /home/ubuntu:/workspace --gpus=all -d rmitchell88/capstone_api:1.1

# Testing 
curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello world!"}' http://54.145.236.113:443/generate