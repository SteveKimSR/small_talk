from openai import OpenAI
import requests
import cv2
import numpy as np
import urllib
import matplotlib.pyplot as plt
import re

# OpenAI API 키 설정
api_key = ''
client = OpenAI(api_key=api_key)


def prompt_gpt(msg):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg}]
    )

    return (response.choices[0].message.content)


def extract_keywords(text):
    # Regular expression to find all keywords
    keywords = re.findall(r'\d+\.\s*(\w+)', text)
    return keywords


def extract_sentences(text):
    # Regular expression to find all sentences without the numbers and extra spaces
    sentences = re.findall(r'\d+\.\s*(.+)', text)
    return sentences


def gpt(user_input, daily_temperature):

    # input message에서 keywords 추출
    keywords = prompt_gpt(f"'{user_input.msg}' Pick out key keywords from the following sentences.\n'"
                          'When you tell me a keyword, put a number in front of each keyword. Set the starting number to 1.\n'
                          f'For example, 1. keyword 1\n2. keyword 2\n3. keyword 3 ... ')

    text = extract_keywords(keywords)

    # gpt에 물어보기
    answer = prompt_gpt(f'Can you recommend two styles of clothing for {user_input.age} year old {user_input.gender} in {daily_temperature} degrees Celsius weather?\n'
                        f'When recommending clothes, put a number in front of each styles. Explain the clothes in about 100 words. Set the starting number to 1.\n'
                        f'For example, 1. Style1\n 2. ... ')

    return extract_sentences(answer)
