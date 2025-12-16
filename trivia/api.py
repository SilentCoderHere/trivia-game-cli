from http.client import HTTPResponse
from json import loads
from urllib.parse import urlencode
from urllib.request import urlopen

from trivia.enums import Category, Difficulty, QuestionType


def check_response_code(data: dict) -> str:
    response_code = data.get("response_code", 0)
    codes = {
        0: "Success Returned results successfully.",
        1: "No Results Could not return results. The API doesn't have enough questions for your query.",
        2: "Invalid Parameter Contains an invalid parameter. Arguments passed in aren't valid.",
        3: "Token Not Found Session Token does not exist.",
        4: "Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary.",
        5: "Rate Limit Too many requests have occurred. Each IP can only access the API once every 5 seconds.",
    }

    return codes.get(response_code, "Unknown response code")


class UrlHandler:
    def __init__(
        self,
        total_questions: int = 10,
        category: Category = Category.ANY,
        difficulty: Difficulty = Difficulty.ANY,
        question_type: QuestionType = QuestionType.ANY,
    ):
        assert total_questions > 0 and total_questions <= 50

        self.total_questions = total_questions
        self.category = category
        self.difficulty = difficulty
        self.question_type = question_type

    @property
    def url(self) -> str:
        query_params = {"amount": str(self.total_questions)}

        if self.category != Category.ANY:
            query_params["category"] = self.category.value
        if self.difficulty != Difficulty.ANY:
            query_params["difficulty"] = self.difficulty.value
        if self.question_type != QuestionType.ANY:
            query_params["type"] = self.question_type.value

        return f"https://opentdb.com/api.php?{urlencode(query_params)}"

    def fetch(self) -> dict:
        response: HTTPResponse
        with urlopen(self.url) as response:
            data = loads(response.read().decode())

        if data["response_code"] != 0:
            raise Exception(check_response_code(data))

        return data
