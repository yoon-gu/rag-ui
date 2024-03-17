import gradio as gr
import random

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(show_copy_button=True, likeable=True)
    with gr.Row():
        query = gr.Textbox(label="사용자 질문", scale=4)
        index = gr.Dropdown(["index1", "index2"], label="Index", value="index1")
    with gr.Accordion(open=False, label="Further Results"):
        with gr.Row():
            with gr.Column():
                results = gr.Code(label="Used Query")
            with gr.Column():
                retriever_results = gr.JSON(label="Retriever Results")
        with gr.Row():
            llm_prompt = gr.Code(label="LLM Prompt")


    def echo(query, history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        history.append((query, bot_message))
        return  "", history
    
    query.submit(echo, [query, chatbot], [query, chatbot])
    
demo.queue()
demo.launch()