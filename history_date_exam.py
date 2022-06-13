import random

# dict of history dates
dates = {'Battle of Solicinium': 367, 'Battle of Ostia': 409, 'Battle of Cartagena': 461, 'Siege of Rome': 472,
         'Battle of Babylon': 636, 'Battle of Suntel': 782, 'Battle of Derby': 917, 'Battle of Cedynia': 972,
         'Battle of the River Bug': 1018, 'Siege of Lisbon': 1147, 'Battle of Garoza': 1287, 'Battle of Dimbos': 1303,
         'Battle of Saintes': 1351, 'Battle of Shrewsbury': 1403, 'Battle of Castillon': 1453, 'Battle of Świecino': 1462,
         'Battle of Shelon': 1471, 'Battle of Toro': 1476, 'Siege of Rhodes': 1480, 'Battle of Sacheon': 1598,
         'Battle of Glen Fruin ': 1603, 'Battle of Leeds': 1643, 'Siege of Viborg': 1710, 'Battle of Krefeld ': 1758,
         'Battle of the Malta Convoy': 1800, 'Battle of Alexandria': 1801, 'Battle of Seven Oaks': 1816, 'Battle of Kurekdere': 1854,
         'Battle of Abtao': 1866, 'Battle of Khartoum': 1885, 'Battle of Bekeriyah': 1904, 'Battle of Kruty': 1918,
         'Battle of Moscow': 1942, 'Black Friday': 1945, 'Battle of Goose Green': 1982, 'Battle of Komsomolskoye': 2000,
         'Battle of Herat': 2001, 'Battle of Nalchik': 2005, 'Operation Moshtarak': 2010, 'Attack on Snake Island': 2022}

# number of exams
for quiz_number in range(30):
    # creating quiz and answer files
    quiz_exam = open(f'exam\\History_Quiz_{quiz_number + 1}.txt', 'w')
    quiz_answers = open(f'answer\\History_Quiz_{quiz_number + 1}_answers.txt', 'w')

    # heading of quiz
    quiz_exam.write(f'Name:\nDate:\nGroup:\nGrade:\n\n')
    quiz_exam.write((' ' * 15) + f'History Exam Number {quiz_number + 1}\n\n\n')

    # taking keys and shuffle them
    battles = list(dates.keys())
    random.shuffle(battles)

    # 30 questions in one quiz
    for question in range(30):
        correct_ans = dates[battles[question]]
        wrong_ans = list(dates.values())
        # delete correct answer from list of wrong answers
        del wrong_ans[wrong_ans.index(correct_ans)]
        # taking 3 wrong answers from list
        wrong_ans = random.sample(wrong_ans, 3)
        # list with 3 wrong answers and one correct
        answers = [correct_ans] + wrong_ans
        random.shuffle(answers)

        # heading of every question
        quiz_exam.write(f'{question + 1}. Mark the date of the {battles[question]}\n')

        # answers
        for i in range(4):
            quiz_exam.write(f"{'ABCD'[i]} {answers[i]}\n")
        quiz_exam.write('\n')

        # file with correct answers
        quiz_answers.write(f"{question + 1} {'ABCD'[answers.index(correct_ans)]}\n")

    # closing files
    quiz_exam.close()
    quiz_answers.close()

