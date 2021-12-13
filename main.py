from question_bank import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
score = 0
for questions in range(0, len(question_data)):
    new_question = Question(question_data[questions]['text'], question_data[questions]['answer'])
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
print(quiz.next_question())

while quiz.still_has_questions():
    quiz.next_question()
print(f"you got {quiz.score}/ {len(quiz.q_list)}")