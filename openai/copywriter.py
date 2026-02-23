from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import gradio as gr


load_dotenv(find_dotenv())

client = OpenAI()

def ads_text(name, brand_name, strength,tone_manner,keyword,value):
    response = client.responses.create(
        model="gpt-4o-mini", 
        input=[
            {
                "role":"developer",
                "content":"당신은 최고의 카피라이터다."
            },
            {
                "role":"user",
                "content":f"""
                아래 내용을 참고해서 1-2줄의 광고 문구 5개 작성.
                - 제품명 : {name}
                - 브랜드명 : {brand_name}
                - 브랜드 핵심 가치 : {value}
                - 제품특징 : {strength}
                - 톤앤매너 : {tone_manner}
                - 필수 포함 키워드 : {keyword}
                """
            },
        ]
    )
    
    
    return response.output_text

demo = gr.Interface(
    fn=ads_text,
    inputs=[
        gr.TextArea(label="제품명"),
        gr.TextArea(label="브랜드명"),
        gr.TextArea(label="브랜드 핵심 가치"),
        gr.TextArea(label="제품특징"),
        gr.TextArea(label="톤앤매너"),
        gr.TextArea(label="필수 포함 키워드")],
    outputs=gr.Markdown(),
    title="💄 OpenAI API 광고 문구 프로그램 구현",
)

demo.launch()
