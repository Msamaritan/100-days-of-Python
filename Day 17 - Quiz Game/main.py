from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    ques_txt = question["text"]
    ques_ans = question["answer"]
    new_ques = Question(ques_txt, ques_ans)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have successfully completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
