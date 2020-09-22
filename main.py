import json
import random
import re
from fuzzywuzzy import fuzz
from question_response import generate_answer
from statement_related_templates import *
from statement_response import process_statement

with open('dev.json') as json_file:
    basic_data = json.load(json_file)

with open('simple_questions_answers.json') as json_file:
    simple_questions = json.load(json_file)

previous_messages = []


def process_user_input(value):
    # if user already wrote the same text
    for message in previous_messages:
        if fuzz.ratio(message, value) > 90:
            return already_asked_response[random.randint(0, len(previous_messages) - 1)]
    else:
        previous_messages.append(value)
    # to find the full answer
    for question in simple_questions.keys():
        if fuzz.partial_token_set_ratio(question, value) > 92:
            return simple_questions[question][random.randint(0, len(simple_questions[question]) - 1)]

    for category in basic_data["data"]:
        for paragraph in category["paragraphs"]:
            for question in paragraph["qas"]:
                if fuzz.ratio(question["question"], value) > 90:
                    res = question["answers"]
                    if len(question["answers"]) == 0:
                        return "Are you sure that you are asking a question which has an answer?"
                    return res[random.randint(0, len(question["answers"]) - 1)]["text"]
    if re.search(r"\?", value) is not None:
        # if its a question
        answer = generate_answer(value.split("?")[0])
        return answer if answer else default_responses[random.randint(0, len(default_responses) - 1)]
    else:
        answer = process_statement(value)
        return answer if answer else default_responses[random.randint(0, len(default_responses) - 1)]


while True:
    val = input("> ")
    print(process_user_input(val.lower()))
