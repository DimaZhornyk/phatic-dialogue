import random
import re

from templates import *


def give_answer_by_question_word(value, question_word):
    # if we are asked personally
    if value.find("you") is not None:
        for outer_key in question_words[question_word].keys():
            for word in question_words[question_word][outer_key]["keywords"]:
                if value.find(word + " "):
                    answers = question_words[question_word][outer_key]["answers"]
                    return answers[random.randint(0, len(answers) - 1)]
        return "Why are you so interested in that?"
    # if we are asked about weather
    elif value.find("weather") is not None:
        return ""


def generate_answer(value):
    for word in re.split(r"[\s,.!]", value):
        if word in question_words.keys():
            return give_answer_by_question_word(value, word)
    else:
        return "Because I can"
