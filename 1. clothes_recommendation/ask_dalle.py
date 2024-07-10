from openai import OpenAI
import requests
import cv2
import numpy as np
import urllib

api_key = ''
client = OpenAI(api_key=api_key)


def prompt_dalle(msg):
    response = client.images.generate(
        model="dall-e-2",
        prompt=msg,
        size="1024x1024",
        n=1
    )

    image_url = response.data[0].url

    return image_url


def get_image(image_url):

    with urllib.request.urlopen(image_url) as url_response:
        image_array = np.asarray(
            bytearray(url_response.read()), dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    resize = cv2.resize(image, (256, 256))

    return resize


def dalle(user_input, recommended_clothings):
    recommended_pictures = []

    for i in recommended_clothings:
        recommended_pictures.append(prompt_dalle(f"A {user_input.age}-year-old {user_input.gender} fashion model wearing a {
                                    i} in white background. Make sure all the clothes from top to bottom are shown in the picture."))

    temp_img = np.concatenate(
        (get_image(recommended_pictures[0]), get_image(recommended_pictures[1])), axis=1)

    # cv2.imshow('temp', temp_img)
    cv2.imwrite(
        './todo-frontend/src/dallePictures/pic.png', temp_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return temp_img
