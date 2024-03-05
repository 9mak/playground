from InquirerPy import prompt

questions = [
    {
        "type": "list",
        "message": "Select an action:",
        "choices": ["Upload", "Download",
                    {"name": "Exit", "value": None}],
        "default": None,
        # "multiselect": True,
    },
]

answer = prompt(questions=questions)
print(answer)

