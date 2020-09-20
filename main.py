import json
import random
import re

from question_response import generate_answer
from templates import *

from fuzzywuzzy import fuzz

with open('dev.json') as json_file:
    basic_data = json.load(json_file)


def process_user_input(value):
    # to find the full answer
    for category in basic_data["data"]:
        for paragraph in category["paragraphs"]:
            for question in paragraph["qas"]:
                if fuzz.ratio(question["question"], value) > 95:
                    res = question["answers"]
                    if len(question["answers"]) == 0:
                        return "Impossible to answer"
                    return res[random.randint(0, len(question["answers"]) - 1)]["text"]
    if re.search(r"\?", value) is not None:
        # if its a question
        return generate_answer(value.split("?")[0].lower())
    return "K"


while True:
    val = input("> ")
    print(process_user_input(val))
