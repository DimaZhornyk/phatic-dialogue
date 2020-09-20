regexp_templates = [

]

# qna = [
#     {"question_word": "why",
#      "questions": [],
#      "answers": []}
# ]

question_words = {
    "who": {},
    "what": {"position": {},
             "preferences": {},
             },
    "where": {},
    "why": {"positive": {"keywords": ["like", "love", "adore"],
                         "answers": [
                             "Because it gives me a pleasure",
                             "Because it grants me a lot of positive emotions",
                             "Because I can`t imagine our world without it"
                         ]},
            "negative": {"keywords": ["hate", "dislike"],
                         "answers": ["Because it "]
                         },
            "default_answers": [
                "Oh, I never even thought about that. And you?",
                "Because, man! That`s obvious. Why are you asking such s simple stuff?",
                ""
            ]}}

general_questions = {
    "weather": [],
    "sport": ["Sorry, but I`m not very interested in sport"],
    "favorite football": ["My favorite team is Barcelona", "My favorite "],
    "politic": [],
    "favorite actor": ["My favorite actor is VladTUZ"],
    "work": [],
    "study": [],
    "favorite movie": [],
    "history": [],
    "opinion": []
}
