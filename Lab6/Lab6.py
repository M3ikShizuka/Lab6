#####################################################################################################################
################################################## Test data: #######################################################
#####################################################################################################################
#Петрова Ольга 10 10 10 10
#Селезнёва Алиса 10 10 10 10
#Калиниченко Иван 9 10 10 10
#Иванов Сергей 7 8 9 10
#Симонов Семён 5 5 5 5
#Борисов Андрей 0 4 10 10
#####################################################################################################################
##################################################### Data: #########################################################
#####################################################################################################################
class Cparticipant:
    surname = None
    name = None
    points = {}

    def __init__(self, surname, name, points):
        self.surname = surname
        self.name = name
        self.points = points

    def get_points_sum(self):
        return sum(self.points)

    def show_info(self):
        print("%s %s" % (self.surname, self.name))
#####################################################################################################################
##################################################### Funcs: ########################################################
#####################################################################################################################
def main():
    max_participants = 100
    participant_count = int(input("Количество участников: "))
    if participant_count > max_participants:
        print("Участников больше %i!" % max_participants)
        exit(1)
    
    participant_list = list()
    max_point = 0

    print("Введите имена участников:")
    participant_index = 0
    while participant_index < participant_count:
        full_name = input()
        points = [None] * 4

        # Обработка данных участника.
        surname, name, points[0], points[1], points[2], points[3] = full_name.split(" ")
        points = list(map(int, points))

        if max(points) > 10:
            print("Ошибка в количестве баллов!")
            print("Повторите попытку ввода.")
            continue
       
        if len(surname) > 20:
            print("Фамилия слишком длинная!")
            print("Повторите попытку ввода.")
            continue

        if len(name) > 15:
            print("Имя слишком длинное!")
            print("Повторите попытку ввода.")
            continue
        
        # Инициализация объектов класса учаник.
        participant = Cparticipant(surname, name, points)
        participant_points_sum = participant.get_points_sum()
        
        # Сравнение суммы балов ученика, с последним наивысшим баллом.
        if max_point < participant_points_sum:
            max_point = participant_points_sum

        # Добавление в общий список учеников.
        participant_list.append(participant)
        participant_index += 1

    # Поиск всех учеников с наивысшим баллом.
    participant_favorites = list()
    last_best_point = 10 * 4 + 1
    for place_index in range(3):
        temp_best_point = 0
        temp_best_participant = list()
        for participant in participant_list:
            participant_points_sum = participant.get_points_sum()
            if participant_points_sum < last_best_point and participant_points_sum > temp_best_point:
                temp_best_participant.clear()
                temp_best_participant.append(participant)
                temp_best_point = participant_points_sum
            elif participant_points_sum == temp_best_point:
                temp_best_participant.append(participant)

        participant_favorites.extend(temp_best_participant)
        last_best_point = temp_best_point
        place_index += 1

    # Вывод призёров.
    print("Фавориты:")
    for participant in participant_favorites:
        participant.show_info()
#####################################################################################################################
##################################################### Exec: #########################################################
#####################################################################################################################
main()