import requests

basic_disciplines = ["Иностранный язык в профессиональной сфере", "Информационное право", "Машинное обучение в семантическом и сетевом анализе"]
user_disciplines = ["Программирование в среде R", "Основы технологий интернета вещей"] + basic_disciplines

# Меняйте начало и конец тут
schedule_data = requests.get("https://ruz.fa.ru/api/schedule/group/110815?start=2024.02.12&finish=2024.02.18&lng=1").json()


def pretty_print_schedule(matches):
    if matches:
        header = f"{'Date':<12} {'Discipline':<50} {'Time':<18} {'Auditorium':<15}"
        print(header)
        print("-" * len(header))

        for match in matches:
            row = f"{match['date']:<12} {match['discipline']:<50} {match['beginLesson']} - {match['endLesson']:<11} {match['auditorium']:<15}"
            print(row)
    else:
        print("Расписание не найдено.")

def find_classes_for_date_and_disciplines(disciplines, schedule):
    matches = []
    for class_info in schedule:
        if class_info["discipline"] in disciplines:
            matches.append(class_info)
    return matches


# Find matching classes.
matching_classes = find_classes_for_date_and_disciplines(user_disciplines, schedule_data)

pretty_print_schedule(matching_classes)