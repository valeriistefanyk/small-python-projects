
#! python3
# randomQuizGenerator - Создает экзаменационные билеты с
# вопросами и ответами, расположенными в случайном порядке
# вместе с ключами ответов

import random, os

# Данные билета. Ключи - названия штатов, а значения - столицы
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
}

# Генерация 35 файлов билетов.
path_to_folder = os.path.join(os.getcwd(), 'routine_tasks_automation', 'read_write_files', 'exam_blanks')
for quizNum in range(35):
    filenameQuiz = f'captitalsquiz{quizNum + 1}.txt'
    filenameQuizAnswers = f'captitalsquiz_answers{quizNum + 1}.txt'
    quizFile = open(os.path.join(path_to_folder, filenameQuiz), 'w', encoding='utf-8')
    answerKeyFile = open(os.path.join(path_to_folder, filenameQuizAnswers), 'w', encoding='utf-8')
    
    # Запись заголовка
    quizFile.write('Имя:\n\nДата:\n\nКурс:\n\n')
    quizFile.write((' ' * 15) +
        'Проверка знания столиц штатов (Билет %s)' % (quizNum + 1)
    )
    quizFile.write('\n\n')
    
    # Перемешивание порядка следования столиц штатов.
    states = list(capitals.keys())
    random.shuffle(states)

    # Цикл по всем штатам с созданием вопроса для каждого из них.
    for questionNum in range(len(capitals)):

        # Получение правильных и неправильных ответов.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Запись вариантов вопросов и ответов в файл билета.
        quizFile.write('%s. Выберите столицу штата %s.\n' % 
            (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Запись ключа ответа в файл
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 
            'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
