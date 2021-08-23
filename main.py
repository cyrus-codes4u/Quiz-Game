from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question_object = Question(question=text, answer=answer)
    question_bank.append(new_question_object)

quiz = QuizBrain(question_bank)
quiz.next_question()
