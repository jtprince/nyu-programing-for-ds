class Questions(list):
    @classmethod
    def from_text(cls, text: str) -> "Answers":
        questions = [question.strip() for question in text.strip().split("\n")]
        return cls(questions)

    def answer(self, number: int, value):
        print(f"{number}.", self[number - 1])
        print("  ", value)
