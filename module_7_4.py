team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
challenge_result = 'Победа команды Волшебники данных!'


print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач(и).')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(challenge_result)

