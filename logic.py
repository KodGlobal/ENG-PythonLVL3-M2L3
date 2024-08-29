# Task 2 - Import everything you need


class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        # Task 3 - Create a method for generating the Inline keyboard
        return buttons

# Task 4 - fill the list with your questions
quiz_questions = [
    Question("What do cats do when nobody sees them?", 1, "Sleep", "Write memes"),
    Question("How do cats express their love?", 0, "Loud purring", "Lovaely photos", "Barking"),
    Question("What books do cats like to read?", 3, "Self-help books", "Time management: how to sleep 18 hours a day", "101 ways to go to sleep 5 minutes earlier than your owner", "A guide to human management")
]

