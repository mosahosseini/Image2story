from dotenv import find_dotenv, load_dotenv

from transformers import pipeline
from PIL import Image
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import GPT4All

import streamlit as st
import os

load_dotenv( find_dotenv())
HUGGINGFACEHUB_API_TOKEN =os.getenv("HUGGINGFACEHUB_API_TOKEN")


import requests

PATH = r'mistral-7b-instruct-v0.1.Q4_0.gguf'


def img2text(img):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

    # im = Image.open(im_name)
    return image_to_text(img, max_new_tokens=20)


def text_to_story(senario):
    llm = GPT4All(model=PATH, verbose=True)
    template = """
    #                         ### Instruction:
    #                         You are a storry teller, tell a story based on the prompt below. It should be max 100 words.
    #                         ### Prompt:
    #                         {senario}
    #                         ### Response:
    #                         """

    prompt = PromptTemplate.from_template(template)

    chain = LLMChain(prompt=prompt, llm=llm)

    response = chain.invoke(senario)
    return response


def TTS(message):

    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads = {"inputs": message
                }
    response = requests.post(API_URL, headers=headers, json=payloads)

    with open("audio.flac", "wb") as file:
        file.write(response.content)

    with open("audio.flac", "rb") as file:
        audio = file.read()
        st.audio(audio, format="audio/flac")







if __name__ == "__main__":
    st.title("🦜🔗 Image to Story")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        text = img2text(img)
        story = text_to_story(text[0]["generated_text"])
        st.write(story["text"])
        TTS(story["text"])






