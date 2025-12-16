from trivia.api import UrlHandler, check_response_code
from trivia.constants import category_dict, difficulty_dict, question_type_dict
from trivia.enums import Category, Difficulty, QuestionType
from trivia.game import Trivia
from trivia.input_utils import get_integer_in_range

if __name__ == "__main__":
    total_questions = get_integer_in_range(
        "Enter total questions (1-50): ", 1, 50, False
    )

    print("Select a category:")
    print("1. General Knowledge")
    print("2. Science & Nature")
    print("3. Computers Science")
    print("4. Mathematics")
    print("5. Sports")
    print("6. Geography")
    print("7. History")

    category = get_integer_in_range(
        "Enter the category (1-7) [Empty for random]: ", 1, 7
    )

    print("Select a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = get_integer_in_range(
        "Enter the difficulty (1-3) [Empty for random]: ", 1, 3
    )

    print("Select a question type:")
    print("1. True/False")
    print("2. Multiple Choice")
    question_type = get_integer_in_range(
        "Enter the question type (1-2) [Empty for random]: ", 1, 2
    )

    url_handler = UrlHandler(
        total_questions=total_questions,
        category=category_dict.get(category, Category.ANY),
        difficulty=difficulty_dict.get(difficulty, Difficulty.ANY),
        question_type=question_type_dict.get(question_type, QuestionType.ANY),
    )

    print("Fetching questions .....")
    response = url_handler.fetch()

    if response.get("response_code") != 0:
        print(check_response_code(response))
        quit()

    print("Questions fetched successfully\n")

    trivia = Trivia(response.get("results", []))
    trivia.play()

    print(f"Score: {trivia.get_score()}/{trivia.get_total_questions()}")
