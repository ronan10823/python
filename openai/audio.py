# text -> 음성
from openai import OpenAI
import gradio as gr
import tempfile

from dotenv import load_dotenv, find_dotenv
# .env 파일 가져오기
load_dotenv(find_dotenv())

client = OpenAI()

def generate_voice(prompt):
    speech = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="shimmer",
        input=prompt
    )
    
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tmp_path = tmp.name
    tmp.close()

    with open(tmp_path, "wb") as f:
        f.write(speech.read())
    
    return tmp_path


demo = gr.Interface(
    fn=generate_voice,
    inputs=gr.Text(placeholder="예) 안녕하세요", label="텍스트", lines=3),
    outputs=gr.Audio(type="filepath",autoplay=True)
)
