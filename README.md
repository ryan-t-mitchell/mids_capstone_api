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

# move the pipeline.pkl file into the api/ directory

# Build container image
docker build -t capstone_api:1.0 .

# Run container image
docker run --rm --name capstone_api -p 8000:8000 -d capstone_api:1.0

