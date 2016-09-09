

right_answers = 0
while right_answers < 2:

    def validate_answer(our_answer, valid_answer):
        global right_answers
        if our_answer == valid_answer:
            print('Right')
            right_answers += 1
        else:
            print('Wrong!')

    answer1 = input('What is 1? ')
    validate_answer(answer1,'int')
       

    answer2 = input('What is 2+2? ')
    validate_answer(answer2, 4)
        

    answer3 = input('What is capital of Russia? ')
    validate_answer(answer3,'Moscow')
break    



print('You gave %i answers' % right_answers)
