from prettytable import PrettyTable
import platform
import os

# person_cnt = input("请输入消费人数(按回车默认2): ")
# if person_cnt == "":
#     person_cnt = 2
# else:
#     person_cnt = int(person_cnt)
person_cnt = 2
items = []
total_money = 0

print("请按照以下格式输入消费项目(输入空值结束): ")
print("[消费项目名称],[支出金额]")

user_in = input()
while user_in != "":
    if user_in.find('，') == -1:
        items.append(user_in.split(","))
    else:
        items.append(user_in.split("，"))
    user_in = input()

if platform.system() != "Windows":
    os.system("clear")
else:
    os.system("cls")

table = PrettyTable()
table.title = '消费项目清单'
table.field_names = ["消费项目", "支出(¥)"]
for item in items:
    table.add_row(item)
    total_money += int(item[1])
print(table)

table = PrettyTable()
table.title = "汇总"
table.field_names = ["总金额(¥)", "A应付", "B应付"]
ra = list(map(int, input("请输入分款比例(e.g. 4:6): ").split(":")))
a_pay = round(total_money*(ra[0]/(ra[0]+ra[1])), 2)
table.add_row([total_money, a_pay, round(total_money-a_pay, 2)])
print(table)
