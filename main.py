import json
import random
import re
from fuzzywuzzy import fuzz
from question_response import generate_answer
from templates import *

with open('dev.json') as json_file:
    basic_data = json.load(json_file)

previous_messages = []


def process_user_input(value):
    # if user already wrote the same text
    for message in previous_messages:
        if fuzz.ratio(message, value) > 92:
            return already_asked_response[random.randint(0, len(previous_messages) - 1)]
    else:
        previous_messages.append(value)
    # to find the full answer
    for category in basic_data["data"]:
        for paragraph in category["paragraphs"]:
            for question in paragraph["qas"]:
                if fuzz.ratio(question["question"], value) > 95:
                    res = question["answers"]
                    if len(question["answers"]) == 0:
                        return "Are you sure that you are asking a question which has an answer?"
                    return res[random.randint(0, len(question["answers"]) - 1)]["text"]
    if re.search(r"\?", value) is not None:
        # if its a question
        return generate_answer(value.split("?")[0].lower())
    return "K"


while True:
    val = input("> ")
    print(process_user_input(val))
