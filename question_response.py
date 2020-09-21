import random
import re

from templates import *


def give_answer_by_question_word(splitted_input, question_word):
    # if we are asked personally
    if "you" in splitted_input:
        for outer_key in question_words[question_word].keys():
            for word in question_words[question_word][outer_key]["keywords"]:
                if word in splitted_input:
                    answers = question_words[question_word][outer_key]["answers"]
                    return answers[random.randint(0, len(answers) - 1)]
        return "Why are you so interested in that?"
    # if we are asked a broad question with no
    else:
        for question_topic in general_questions.keys():
            if question_topic in splitted_input:
                return general_questions[question_topic][random.randint(0, len(general_questions[question_topic]) - 1)]
    return None


def generate_answer(value):
    splitted_input = list(filter(lambda x: x != "", re.split(r"[\s,.!:;]", value)))
    for word in splitted_input:
        if word in question_words.keys():
            return give_answer_by_question_word(splitted_input, word)
        # question without question word
    for phrase in simple_answers_mapping.keys():
        if re.search(phrase, value):
            answers = simple_answers_mapping[phrase]
            return answers[random.randint(0, len(answers))]
    return None
