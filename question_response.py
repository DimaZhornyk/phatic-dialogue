import random
import re

from question_related_templates import *


def give_answer_by_question_word(default_input, splitted_input, question_word):
    # if we are asked personally
    if re.search("you", default_input):
        for outer_key in question_words[question_word].keys():
            for word in question_words[question_word][outer_key]["keywords"]:
                if re.search(word, default_input) is not None:
                    answers = question_words[question_word][outer_key]["answers"]
                    return answers[random.randint(0, len(answers) - 1)]
        return why_are_you_asking_responses[random.randint(0, len(why_are_you_asking_responses) - 1)]
    # if we are asked a broad question with no
    else:
        for question_topic in general_questions.keys():
            if question_topic in splitted_input:
                for subtopic in general_questions[question_topic].keys():
                    if subtopic in splitted_input:
                        topic_answers = general_questions[question_topic][subtopic]
                        return topic_answers[random.randint(0, len(topic_answers) - 1)]
    return None


def generate_answer(value):
    splitted_input = list(filter(lambda x: x != "", re.split(r"[\s,.!:;]", value)))
    for word in splitted_input:
        if word in question_words.keys():
            return give_answer_by_question_word(value, splitted_input, word)
        # question without question word
    for phrase in simple_answers_mapping.keys():
        if re.search(phrase, value):
            answers = simple_answers_mapping[phrase]
            return answers[random.randint(0, len(answers)-1)]
    return None
