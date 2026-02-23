from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import gradio as gr


load_dotenv(find_dotenv())

client = OpenAI()

def summarize_text(text):
    response = client.responses.create(
        model="gpt-4o-mini", 
        instructions="""
        당신은 텍스트를 한국어로 요약하는 전문가이다. 
        요약 시 다음 사항을 반영해야 한다. 
        - 중복된 내용은 생략하되, 반복되는 내용은 요약해서 더 강조한다. 
        - 사례 중심보다는 개념과 주장 중심으로 요약한다. 
        - 3줄 이내로 요약
        - 불릿 기호(*) 형식으로 작성
        """,
        input=text
    )
    
    
    return response.output_text

demo = gr.Interface(
    fn=summarize_text,
    inputs=[gr.TextArea(lines=10, placeholder="요약할 긴 텍스트 입력", label="텍스트")],
    outputs=gr.Markdown(),
    title="OpenAI API 요약 프로그램 구현",
)

demo.launch()
