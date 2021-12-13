class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.q_number <= len(self.q_list) - 1:
            return True
        else:
            return False

    def next_question(self):
        question = self.q_list[self.q_number].question
        answer = self.q_list[self.q_number].answer
        self.q_number+=1
        user_answer = input(f"Q{self.q_number}: {question} true or false?")
        if user_answer == answer:
            print("yes you got it right")
            self.score+=1
        else:
            print(f"oh no, you failed it")
        return user_answer
