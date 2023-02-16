import torch
import joblib
import logging
import base64
import io
from datetime import datetime as dt
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
#from fastapi.responses import JSONResponse, StreamingResponse
from diffusers import DiffusionPipeline
from pydantic import BaseModel
from io import BytesIO
from PIL import Image


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


app = FastAPI()

class Model(BaseModel):
    text: str

@app.get("/health")
async def datetime():
    return dt.now()


@app.get("/hello")
def read_name(name: str):
    return "hello {}".format(name)


pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")


# # Load model pipeline
# with open("./pipeline.pkl", "rb") as f:
#     pipeline = pickle.load(f)

#pipeline = joblib.load("./pipeline.pkl")

# @app.post("/generate")
# async def text_to_image(text: str = Form()): #added after reading https://fastapi.tiangolo.com/tutorial/request-forms/
#     logger.info("Received POST request with text: {}".format(text))
#     generated_image = pipeline(text).images[0]
#     return {"image": generated_image}

logger.info("Got to options_handler")
@app.options("/generate")
async def options_handler(request: Request):
    logger.info("Received OPTIONS request")
    response = Response(status_code=200, headers={
        "Access-Control-Allow-Origin": request.headers["Origin"],
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Credentials": "true"
    })
    logger.info("Returned response from options handler")
    return response

logger.info("Got to text_to_image fcn")
@app.post("/generate")
async def text_to_image(model: Model):# = Form()):
    logger.info("Received POST request with text: {}".format(model.text))
    generated_image = pipeline(model.text).images[0]
    logger.info("Type of image being generated: {}".format(type(generated_image)))
    # use a static image to see if it is even sending it to the page
    #generated_image = Image.open("image.png")
    #logger.info("Type of image being generated: {}".format(type(generated_image)))
    buffer = BytesIO()
    generated_image.save(buffer, format="PNG") # Save the image to a buffer
    img_str = base64.b64encode(buffer.getvalue()) # Convert the buffer to base64-encoded binary data
    # is image/png the right type to return?
    return Response(content=img_str.decode('utf-8'), media_type="image/png", headers={"Access-Control-Allow-Origin": "*"}) 

    # Can we just host the image that is generated automatically? And then load the src in the HTML?