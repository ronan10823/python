from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import gradio as gr
import base64
from io import BytesIO
from PIL import Image


load_dotenv(find_dotenv())

client = OpenAI()

def generate_image(prompt):
    response = client.images.generate(
    model="gpt-image-1-mini",
    prompt=prompt.strip(),
    size = "1024x1024",
    quality="high",
    output_format="png")
    
    b64 = response.data[0].b64_json
    img_bytes = base64.b64decode(b64)
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    img.save("./python/image/panda.png")
    
    return img

demo = gr.Interface(
    fn=generate_image, 
    # inputs=gr.Image(type="filepath"), 
    inputs="text", 
    outputs=gr.Image()
)
    
demo.launch()
