import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

# Interface > function(must)
demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

demo.launch(share=True)

