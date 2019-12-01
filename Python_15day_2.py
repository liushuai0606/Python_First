import sqlite3

user_notify = """
请输入查询选项：
输入 1 : 查询整个数据库
输入 2 : 基于姓名查询
输入 3 : 基于年龄查询
输入 4 : 基于作业数1

输入 0 : 退出
"""


def search_result_str(search_sq1):
    conn = sqlite3.connect('qytanghomework.sqlite')
    cursor = conn.cursor()
    all_search_info = cursor.execute(search_sq1)
    all_description = [des[0] for des in all_search_info.description]

    search_result = cursor.fetchall()
    if not search_result:
        conn.close()
        return '学员信息未找到！'

    return_str = ''
    for x in search_result:
        for y in zip(all_description, x):
            return_str += f"{y[0]:>5}:{y[1]:<5}"
        return_str += '\n'
    conn.close()
    return return_str

while True:
    print(user_notify)
    user_input = input('请选择:')
    if user_input == '0':
        break

    elif user_input == '1':
        print(search_result_str("select * from qytang_homework_info"))

    elif user_input == '2':
        user_sn = input('请输入学员姓名:')
        if not user_sn:
            continue
        print(search_result_str("select * from qytang_homework_info where 学员姓名 = '{0}'".format(user_sn)))

    elif user_input == '3':
        user_age = input('搜索大于输入年龄的学员，请输入学员年龄:')
        if not user_age:
            continue
        print(search_result_str("select * from qytang_homework_info where 学员年龄 > '{0}'".format(user_age)))

    elif user_input == '4':
        user_homework = input('搜索大于输入作业数的学员，请输入作业数量:')
        if not user_homework:
            continue
        print(search_result_str("select * from qytang_homework_info where 学员作业数 > '{0}'".format(user_homework)))

    else:
        print('输入错误！请重试！')
