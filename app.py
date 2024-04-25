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


#HUGGINGFACEHUB_API_TOKEN ="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"

import requests

PATH = r'C:\Users\sasyn\.cache\mistral-7b-instruct-v0.1.Q4_0.gguf'


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

    with open("test.flac", "wb") as file:
        file.write(response.content)

    with open("test.flac", "rb") as file:
        audio = file.read()
        st.audio(audio, format="audio/flac")




# def process_image(image):
#     image = Image.fromarray(image)
#     scenario = img2text(image)
#     scenario = scenario[0]["generated_text"]
#
#     story = generate_story(scenario)
#     TTS(story)
#
#     audio = "audio.flac"
#     text = story
#     TTS(text)
#
#     return text, audio




if __name__ == "__main__":
    st.title("🦜🔗 Image to Story")
    #uploaded_file = st.camera_input()
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
        # If an image is uploaded
    if uploaded_file is not None:
        #image_bytes = uploaded_file.getvalue()
        img = Image.open(uploaded_file)
        # Display the image

        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        text = img2text(img)
        story = text_to_story(text[0]["generated_text"])
        st.write(story["text"])
        TTS(story["text"])



# if __name__ == "__main__":
#     st.title("🦜🔗 gpt for yall")
#     message = "Once upon a time, in a land far away, there were two brave knights named Sir Cedric and Sir Galahad. They both wore shining armor from head to toe and wielded their swords with great skill and precision. The two had been best friends since childhood and often engaged in friendly sword fights just for fun. But one day, a terrible dragon attacked the kingdom and the two knights were called upon to defend it. With their swords drawn, Sir Cedric and Sir Galahad rode out to face the beast together. Despite being vastly outnumbered, the two fought bravely and with honor, never giving an inch. In the end, they managed to defeat the dragon and save the kingdom. From that day on, the two knights were hailed as heroes and their friendship became legendary throughout the land."
#
#     HUGGINGFACEHUB_API_TOKEN = "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"
#
#     text = st.write(message + "\n" + HUGGINGFACEHUB_API_TOKEN)
#
#     API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
#     headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
#     payloads = {"inputs": message
#                 }
#     response = requests.post(API_URL, headers=headers, json=payloads)
#
#     with open("test.flac", "wb") as file:
#         file.write(response.content)
#
#     with open("test.flac", "rb") as file:
#         audio = file.read()
#         st.audio(audio, format="audio/flac")



