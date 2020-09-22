import re
import random
from statement_related_templates import *


def process_statement(value):
    splitted_input = list(filter(lambda x: x != "", re.split(r"[\s,.!:;]", value)))
    for word in close_people_markers:
        if re.search("my " + word, value) is not None:
            return "Tell me more about your " + word
    for verb in verbs:
        if verb in splitted_input:
            return additional_sentences[
                       random.randint(0, len(additional_sentences) - 1)] + " What else you " + verb + "?"
