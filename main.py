import gradio as gr
from n01_single_file import demo as n01_single_file
from n02_multifiles_index import demo as n02_multifiles_index
from n03_elasticsearch_query import demo as n03_elasticsearch_query
from n04_rag_llm import demo as n04_rag_llm

demo = gr.TabbedInterface([n01_single_file, n02_multifiles_index, n03_elasticsearch_query, n04_rag_llm],
                            ["01. Single File", "02. Multi Files Index", "03. Elasticsearch Query", "04. RAG LLM"])


demo.launch()