class QuizBrain:
    def __init__(self, ques_list):
        self.ques_no = 0
        self.score = 0
        self.ques_list = ques_list

    def still_has_questions(self):
        return self.ques_no < len(self.ques_list)

    def next_question(self):
        current_ques = self.ques_list[self.ques_no]
        self.ques_no += 1
        user_answer = input(f"Q{self.ques_no}: {current_ques.question} : (True or False) ")
        self.check_answer(user_answer, current_ques.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right! YAY!!")
        else:
            print("Oops! You got it Wrong.")
            print(f"The correct answer is {correct_ans}")
        print(f"Your score is {self.score}/{self.ques_no}")
        print("\n")


