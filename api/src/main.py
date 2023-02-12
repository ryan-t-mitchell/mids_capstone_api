import torch
import joblib
from datetime import datetime as dt
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from diffusers import DiffusionPipeline

import logging

logger = logging.getLogger(__name__)

# set the logging level to debug
logger.setLevel(logging.DEBUG)

# create a file handler to log to a file
file_handler = logging.FileHandler('main.log')

# create a formatter to format the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# set the formatter for the file handler
file_handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(file_handler)

# log some information messages
logger.info("PRE:Starting the API")
logger.info("PRE:Listening on port 8000")

# log some debug messages
logger.debug("PRE:Received a request")
logger.debug("PRE:Processing the request")

# log some error messages
logger.error("PRE:Error processing the request")
logger.error("PRE:Request failed")

app = FastAPI()

@app.get("/hello")
def read_name(name: str):
    return "hello {}".format(name)

print('got here')
#pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
print('got heeeeere')

# # Load model pipeline
# with open("./pipeline.pkl", "rb") as f:
#     pipeline = pickle.load(f)

#pipeline = joblib.load("./pipeline.pkl")

@app.options("/generate")
async def generate_options(request: Request):
    return JSONResponse(content={})


@app.post("/generate")
async def text_to_image(text: str):
    logger.info("Received POST request with text: {}".format(text))
    #print("text input: {}").format(text)
    # Write your PyTorch code here to generate the image based on the input text
    # You can access the text from the request body using the `text` variable
    generated_image = pipeline(text).images[0]
    return {"image": generated_image}

print('got here too')

# @app.get("/health")
# async def datetime():
#     return dt.now()


# log some information messages
logger.info("Starting the API")
logger.info("Listening on port 8000")

# log some debug messages
logger.debug("Received a request")
logger.debug("Processing the request")

# log some error messages
logger.error("Error processing the request")
logger.error("Request failed")