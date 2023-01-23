from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in range(len(question_data)):

    obj = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(obj)

brain = QuizBrain(question_bank)

while brain.still_has_question():
    brain.next_question()

print("You've completed the quiz.")
print(f"Your final score is {brain.score}/{brain.question_number}")

