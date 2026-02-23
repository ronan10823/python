from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv(find_dotenv())

client = OpenAI()

# 장르를 받은 후, 장르 작가에게 알맞는 질문 8개 생성
# 장르 특징 5줄 정리
def interview_text(genre):

    if not genre.strip():
        return gr.Error("장르를 입력해 주세요")
    
    response = client.responses.create(
        model="gpt-4o-mini", 
        input=[
            {
                "role":"developer",
                "content":"당신은 문학 전문 기자입니다."
            },
            {
                "role":"user",
                "content":f"""
                다음 장르의 특징을 분석하고, 그 분석을 바탕으로 인터뷰 질문을 작성하세요.
                
                [장르]
                {genre}

                요구사항
                1. 장르 특징 5줄 정리
                2. 인터뷰 질문 8개 작성
                """
            },
        ]
    )
    
    
    return response.output_text

demo = gr.Interface(
    fn=interview_text,
    inputs=[
        gr.TextArea(label="장르", placeholder="장르"),
        ],
    outputs=gr.Markdown(),
    title="🎤 작가 인터뷰 질문 생성 문구 프로그램 구현",
)

demo.launch()
