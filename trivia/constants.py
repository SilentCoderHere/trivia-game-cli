from trivia.enums import Category, Difficulty, QuestionType

category_dict = {
    1: Category.GENERAL_KNOWLEDGE,
    2: Category.SCIENCE_NATURE,
    3: Category.SCIENCE_COMPUTERS,
    4: Category.SCIENCE_MATHEMATICS,
    5: Category.SPORTS,
    6: Category.GEOGRAPHY,
    7: Category.HISTORY,
}
question_type_dict = {
    1: QuestionType.TRUE_FALSE,
    2: QuestionType.MULTIPLE_CHOICE,
}
difficulty_dict = {
    1: Difficulty.EASY,
    2: Difficulty.MEDIUM,
    3: Difficulty.HARD,
}
