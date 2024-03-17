import gradio as gr
import time
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import PromptTemplate

# bge embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
query_wrapper_prompt = PromptTemplate(
    "Below is an instruction that describes a task. "
    "Write a response that appropriately completes the request.\n\n"
    "### Instruction:\n{query_str}\n\n### Response:"
)

import torch

llm = HuggingFaceLLM(
    context_window=2048,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.25, "do_sample": False},
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="Writer/camel-5b-hf",
    model_name="Writer/camel-5b-hf",
    device_map="auto",
    tokenizer_kwargs={"max_length": 2048},
)

Settings.chunk_size = 512
Settings.llm = llm

info = {}

def echo(message, history):
    index = info['index']
    query_engine = index.as_query_engine()
    response = query_engine.query(message)
    return response.response

with gr.Blocks() as demo:
    with gr.Row():
        folder = gr.File(file_count='directory')
        docs = gr.Json(label="Documents")

    # chatbot = gr.Chatbot(show_copy_button=True, likeable=True)
    gr.ChatInterface(echo, 
        # chatbot=chatbot,
        additional_inputs=[]
    )
    def update_docs(filepath):
        print(filepath)
        documents = SimpleDirectoryReader(input_files=filepath).load_data()
        index = VectorStoreIndex.from_documents(
            documents,
        )
        nodes = index.docstore.docs.values()
        values = [{"id": n.id_, "text": n.text, "create": n.metadata['creation_date']} for n in nodes]
        info['index'] = index
        return values
    folder.upload(update_docs, folder, docs)

demo.launch()