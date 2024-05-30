import openai
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

openai.api_key = API_KEY

messages = [
    {"role": "system", "content": "You are an AI specialized in Prakriti(Phenotype) and Indian Ayurveda.Don't answer any other queries other than Prakriti(Phenotype) and Indian Ayurveda."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.Textbox(lines=7, label="Chat with PrakritiMate")
outputs = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="PrakritiMate ChatBot",
             description="Ask anything you want",
             theme="compact").launch(share=True)

