#python函数（下）->学习return的作用
#1、写一个计算BMI的函数
'''
def calculate_BMI(weight,height):
    BMI = weight/(height**2)
    if BMI <= 18.5:
        BMI_type = '偏瘦' 
    elif 18.5 < BMI <= 25:
        BMI_type = '正常'
    elif 25 < BMI <= 30:
        BMI_type = '偏胖'    
    else:
        BMI_type = '肥胖'
    print(f'你的BMI分类为{BMI_type}')
    return BMI
result = calculate_BMI(20,14)
print(result)
'''

#2、定义一个函数 calculate_grade(score)，根据学生成绩输出对应等级。
'''
def calculate_grade(score):
    if 90 <= score <= 100:
        student_grade = 'A'
    elif score >= 80:
        student_grade = 'B'
    elif score >= 70:
        student_grade = 'C'   
    elif score >= 60: 
        student_grade = 'D'
    else:
        student_grade = 'E'
    print(f'你的等级为{student_grade}')
    return score
result = calculate_grade(27)
print(f'你的成绩为{result}')
'''

#3、计算快递费用
'''
def calculate_shipping(weight):
    if weight <= 1:
        shipping_cost = 8
    elif weight <= 5:
        shipping_cost = 15
    elif weight <= 10:
        shipping_cost = 25
    else:
        shipping_cost = 40
    print(f'快递重量为{weight}kg')
    return shipping_cost
money = calculate_shipping(34)
print(f'本次运费为{money}元')
'''

#4、计算手机电量状态


















