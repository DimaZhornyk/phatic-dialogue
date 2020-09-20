import json
import random

from fuzzywuzzy import fuzz

with open('dev.json') as json_file:
    basic_data = json.load(json_file)


def process_user_input(value):
    for category in basic_data["data"]:
        for paragraph in category["paragraphs"]:
            for question in paragraph["qas"]:
                if fuzz.token_set_ratio(question["question"], value) > 95:
                    return question["answers"][random.randint(0, len(question["answers"]))]["text"]
    return "K"


while True:
    val = input(">")
    print(process_user_input(val))
