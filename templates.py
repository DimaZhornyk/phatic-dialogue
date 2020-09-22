question_words = {
    "who": {
        "about_you": {
            "keywords": ["is your"],
            "answers": [
                "Private is not public ... So I won't tell"
            ],
        },
        "information": {
            "keywords": ["is", "are", "were", "does", "can"],
            "answers": [
                "What do I look like Google? It seems to me that no ..."
            ]
        },
        "default_answers": [
            "Oh, that's another story, maybe I'll tell you over a beer"
        ]
    },
    "what": {
        "reason": {
            "keywords": ["for"],
            "answers": ["The reason for the investigative relationship is not observed, so alas I cannot explain"]
        },
        "information": {
            "keywords": ["is", "does", "did", "was", "were"],
            "answers": ["I am of course super intelligent, but unfortunately I do not have such information"]
        },
        "default_answers": [
            "Where and why is an eternal question, but I don't know the answer to this one ..."
        ]
    },
    "where": {
        "position": {
            "keywords": ["were", "are", "will you", "do you", "did you"],
            "answers": [
                "Oh, are you interested in location? But my RAM don`t remember this.."
            ]
        },
        "place": {
            "keywords": ["is", "was", "will"],
            "answers": [
                "I can't understand you geographer that you are interested in the position..."
            ]
        },
        "default_answers": [
            "Where and why is an eternal question, but I don't know the answer to this one ..."
        ]
    },
    "why": {
        "positive": {
            "keywords": ["like", "love", "adore"],
            "answers": [
                "Because it gives me a pleasure",
                "Because it grants me a lot of positive emotions",
                "Because I can`t imagine our world without it"
            ]},
        "negative": {
            "keywords": ["hate", "dislike"],
            "answers": [
                "Because it doesn't evoke emotion"
            ]},
        "default_answers": [
            "Oh, I never even thought about that. And you?",
            "Because, man! That`s obvious. Why are you asking such s simple stuff?",
            ""
        ]}
}

general_questions = {
    "weather": {
        "today": [
            "I don't know about weather in your city, but weather in Kiev is beautiful"
        ],
        "month": [
            "God only knows it..."
        ],
        "tomorrow": [
            "I think it will be shiny <3"
        ],
        "week": [
            "Let's not make plans for the future"
        ]
    },
    "sport": {
        "opinion": [
            "Sorry, but I`m not very interested in sport",
            "I'm too far from sports"
        ],
        "like": [
            "No, I don`t like this one...",
            "Sorry, but I`m not very interested in sport"
        ],
        "favourite": [
            "My favorite sport is literball"
        ]
    },
    "football": {
        "team": [
            "My favorite team is Barcelona",
            "I hope you are not sick for REAL"
        ],
        "player": [
            "Arshavin in my heart...<3"
        ]
    },

    "politic": {
        "opinion": [
            "I am not a fan of discussing politics",
            "I look like a person who is interested in politics?"
        ],
        "situation": [
            "Oh, politics... I don`t understand this situation...",
            "Glory to Ukraine!"
        ]
    },
    "actor": {
        "favourite": [
            "My favorite actor is Leonardo DiCaprio",
            "There is simply no better actor than me",
            "Bip-bip, T2000 is awesome...))"
        ]
    },
    "work": {
        "favourite": [
            "My favourite work is telling cool stories)))"
        ]
    },
    "movie": {
        "favourite": [
            "I think my favorite movie is Matrix",
            "I think it doesn`t matter. What about you?"
        ]
    },
    "history": {

    }
}

simple_answers_mapping = {
    "do you": ["Yes, I do", "No, I don`t"],
    "have you": ["Yes, I have", "No, I haven`t"],
    "may i ask": ["You are welcome"]
}

already_asked_response = [
    "Bruuh, you are so boring asking the same stuff again and again",
    "What about smth new...?",
    "Can you tell me smth new?",
    "I`ve just hear smth similar for that...",
    "I don't like that you repeat yourself too often",
    "I caught flashbacks, but not from Vietnam"
]
