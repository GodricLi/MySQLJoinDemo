# _*_ coding=utf-8 _*_


import pymysql


"""SELECT语句关键字的执行顺序:
    SELECT 
    DISTINCT <select_list>
    FROM <left_table>
    <join_type> JOIN <right_table>
    ON <join_condition>
    WHERE <where_condition>
    GROUP BY <group_by_list>
    HAVING <having_condition>
    ORDER BY <order_by_condition>
    LIMIT <limit_number>
"""

# 连接
conn = pymysql.connect(host='localhost', user='root', password='123', database='db1')
# 游标
cursor = conn.cursor()

# 查询平均年龄大于30岁的部门名及平均年龄

sql = """select department.name,avg (age) from emp inner join  department on emp.dep_id=department.id
                group by department.name
                having avg (age>30)
                ; 
    """
# 执行sql语句
cursor.execute(sql)
# 获取全部记录
res = cursor.fetchall()
print(res)
