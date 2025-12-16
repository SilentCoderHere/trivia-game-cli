from html import unescape
from random import shuffle

from trivia.input_utils import get_boolean, get_integer_in_range


class QuestionPresenter:
    def __init__(self, question: dict) -> None:
        self._type = question.get("type")
        self.difficulty = question.get("difficulty")
        self.category = unescape(question.get("category", ""))
        self.question = unescape(question.get("question", ""))
        self.correct_answer = unescape(question.get("correct_answer", ""))
        self.incorrect_answers = [
            unescape(answer) for answer in question.get("incorrect_answers", [])
        ]

    def handle_question(self) -> bool:
        if self._type == "boolean":
            return self.handle_boolean()
        else:
            return self.handle_multiple_choice()

    def handle_boolean(self) -> bool:
        print(self.question)
        answer = get_boolean("True(t) or False(f): ")
        if self.correct_answer == "True" and answer:
            print("Correct Answer")
            return True
        else:
            print(f"Incorrect, correct answer is {self.correct_answer}")
            return False

    def handle_multiple_choice(self) -> bool:
        print(self.question)
        options = [self.correct_answer, *self.incorrect_answers]
        shuffle(options)
        for index, option in enumerate(options):
            print(f"{index + 1}. {option}")
        user_answer = get_integer_in_range(
            f"Enter answer option (integer 1-{len(options)}: ", 1, 4, False
        )

        if options[user_answer - 1] == self.correct_answer:
            print("Correct Answer")
            return True
        else:
            print(
                f"Incorrect, correct option is {options.index(self.correct_answer) + 1}"
            )
            return False
