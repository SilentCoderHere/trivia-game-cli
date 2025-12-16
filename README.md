# Trivia CLI

A simple, clean **command-line trivia game** built with Python using the **Open Trivia Database (OpenTDB)** API.

The project focuses on:

- clear structure
- standard library only (no third-party dependencies)
- readable, maintainable code
- a smooth CLI experience

---

## Features

- Fetches trivia questions from OpenTDB
- Supports multiple categories
- Difficulty selection (easy / medium / hard)
- Question types:

  - True / False
  - Multiple Choice

- Randomized answers
- Input validation
- Score tracking
- Clear correct / incorrect feedback

---

## How It Works

1. The user selects:

   - number of questions
   - category (or random)
   - difficulty (or random)
   - question type (or random)

2. The game fetches questions from OpenTDB

3. Questions are presented one by one in the terminal

4. The player answers each question

5. The final score is shown at the end

---

## How to Run

#### Clone the repository

```bash
git clone https://github.com/silentcoderhere/trivia-game-cli
```

#### Run the game

```bash
cd trivia-game-cli
python main.py
```

---

## Possible Improvements

These are intentionally left out to keep the project simple:

- Timed questions
- Persistent high scores
- Game statistics
- Session tokens

The structure makes these easy to add later.

---

## License

This project is **open source** under the [MIT License](LICENSE).
