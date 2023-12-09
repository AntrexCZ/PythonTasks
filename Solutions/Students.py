"""
Eсть список словарей, в которых хранятся студенты с двумя параметрами,
имя и оценка вернуть список имен таких студентов у кого оценка 4 и выше
Например :
[ {‘name’: ‘Anton’, ‘value’: 5}, {‘name’: ‘Anna’, ‘value’: 3}, {‘name’: ‘Sonya’, ‘value’: 4}, {‘name’: ‘Vitaly’, ‘value’: 3}]
ответ [‘Anton’, ‘Sonya’]
Если что вторая это просто задачка без привязки к каким либо типам данных :slightly_smiling_face:
"""

students = [{"name": "Anton", "value": 5}, {"name": "Anna", "value": 3}, {"name": "Sonya", "value": 4},
            {"name": "Vitaly", "value": 3}]

good_students = []

# for i in students:
#     if i["value"] >= 4:
#         good_students.append(i["name"])
# print(good_students)
#

result = [student["name"] for student in students if student["value"] >= 4]

print(result)