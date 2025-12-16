from trivia.presenter import QuestionPresenter


class Trivia:
    def __init__(self, questions: list) -> None:
        self.total_questions = len(questions)
        self.questions = questions
        self.score = 0

    def play(self) -> None:
        for question in self.questions:
            question_handler = QuestionPresenter(question)
            if question_handler.handle_question():
                self.score += 1

    def get_score(self) -> int:
        return self.score

    def get_total_questions(self) -> int:
        return self.total_questions
