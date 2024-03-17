import gradio as gr
from gradio_calendar import Calendar

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            with gr.Row():
                query = gr.Textbox(label="ES Query", scale=4)
                index = gr.Dropdown(["index1", "index2"], label="Index")
            with gr.Row():
                start_year = Calendar(type="datetime", label="Select a start date", value="2024-01-01",
                                info="Click the calendar icon to bring up the calendar.")
                end_year = Calendar(type="datetime", label="Select an end date", value="2024-12-31",
                                info="Click the calendar icon to bring up the calendar.")
        with gr.Column():
            output = gr.Code(label="Response")

    def echo(query, index, start_year, end_year):
        return "Response to " + query + " in " + index + " from " + str(start_year) + " to " + str(end_year)
    query.submit(echo, [query, index, start_year, end_year], [output])
    
demo.queue()
demo.launch()