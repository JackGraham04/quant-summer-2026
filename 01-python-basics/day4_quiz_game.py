from random import shuffle

sports_set = [{'question': 'What year did Andy Murray win his first grand slam?', 
               'A': '2009', 'B': '2010', 'C': '2011', 'D': '2012', 'answer': 'D' },
              {'question': 'Who won the first ever FIFA World Cup?', 'A': 'Argentina', 
               'B': 'Brazil', 'C': 'Uruguay', 'D': 'West Germany', 'answer': 'C' },
              {'question': 'What is the 100m sprint world record?', 
               'A': '9.52', 'B': '9.54', 'C': '9.56', 'D': '9.58', 'answer': 'D' },
              {'question': 'How many Olympic gold medals does Michael Phelps have?', 
               'A': '23', 'B': '24', 'C': '25', 'D': '28', 'answer': 'A' },
              {'question': 'Who is the premier league all time top scorer?', 
               'A': 'Kane', 'B': 'Shearer', 'C': 'Rooney', 'D': 'Salah', 'answer': 'B' }]
maths_set = [{'question': 'What is 10 + 3 * 7', 
              'A': '91', 'B': '29', 'C': '31', 'D': '49', 'answer': 'C' },
             {'question': 'How many sides does a pentagon have?', 
              'A': '3', 'B': '4', 'C': '5', 'D': '6', 'answer': 'C' },
             {'question': 'Whats the next number in the sequence 2, 6, 12, 20, ...', 
              'A': '30', 'B': '32', 'C': '34', 'D': '36', 'answer': 'A' },
             {'question': 'What is the mean of 5, 6, 8, 10, 14?', 
              'A': '8', 'B': '8.6', 'C': '9', 'D': '9.2', 'answer': 'B' },
             {'question': 'What is the fifth decimal place of pi?', 
              'A': '1', 'B': '4', 'C': '7', 'D': '9', 'answer': 'D' }]
geography_set = [{'question': 'Whick country has the most castles?', 
                  'A': 'Germany', 'B': 'France', 'C': 'England', 'D': 'Spain', 'answer': 'A' },
                 {'question': 'In which country is Chernobyl', 
                  'A': 'Greece', 'B': 'Turkey', 'C': 'Russia', 'D': 'Ukraine', 'answer': 'D' },
                 {'question': 'Bratislava is the capital city of which country?', 
                  'A': 'Slovenia', 'B': 'Slovakia', 'C': 'Bosnia', 'D': 'Czechia', 'answer': 'B' },
                 {'question': 'What animal features on the flag of Sri Lanka', 
                  'A': 'Bear', 'B': 'Lion', 'C': 'Wolf', 'D': 'Eagle', 'answer': 'B' },
                 {'question': 'What is the largest continent on Earth by land mass?', 
                  'A': 'North America', 'B': 'Europe', 'C': 'Africa', 'D': 'Asia', 'answer': 'D' }]

# shuffles question set
def shuffle_questions(questions):
    shuffle(questions)
    return questions

# quiz function
def answering_questions(answers):

    score = 0

    for question in answers:
        print(f'{question['question']}')
        print('Is it:')
        for a in ['A', 'B', 'C', 'D']:
            print(f'{a} {question[a]}')
        answer = input('Answer: ').upper()
        if answer == question['answer']:
            print('Correct!')
            score +=1
        else:
            print(f'Incorrect! the answer was {question['answer']}')

    if score == 5:
        print(f'{score}/5 Congrats on the perfect score')
    elif score >= 3:
        print(f'{score}/5 Good effort!')
    else:
        print(f'{score}/5 Kepp practising!')

# input topic of quiz
quiz_type = input('What type of quiz would you like to play? Sports, Maths or Geography?').lower()

if quiz_type == 'sports':
    question_set = sports_set
elif quiz_type == 'maths':
    question_set = maths_set
else:
    question_set = geography_set

shuffled_questions = shuffle_questions(question_set)

# play the shuffled quiz
answering_questions(shuffled_questions)
