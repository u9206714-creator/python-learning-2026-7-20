#python函数（下）
#一、学习return的作用
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
'''
def battery_status(power):
    if power >= 80:
        status = 'enough'
    elif power >= 50:
        status = 'normal'
    elif power >= 20:
        status = 'a bit low'
    else:
        status = 'please charge your phone now'
    print(f'your battery power is {power}%')
    return status
electricity = battery_status(71) 
print(f'your battery status is {electricity}')
'''

#5、购物结算
'''
def discount(price, vip):
    if vip == False:
        final_price = price 
    elif vip == True and price >= 200:
        final_price = price*0.8
    elif vip == True and 0 < price <= 200:
        final_price = price*0.9
    else:
        final_price = 'this is a wrong number' 
    return final_price
result = discount(483,True)
print(f'优惠后的价格为{result}')
'''



#二、python引入模块
#1、 // -> 除完后向下取整
#eg.3//2 = 1 而 3/2 = 1.5
#practice: 1. 10//3 = 3     2. -7//2 = -4

#2、举特殊例子：引入staistics模块
'''
import statistics #内置函数是很常用的函数
print(statistics.median([69,124,-32,27,217]))  #如何使用：模块名.函数名 / 模块名.变量名
'''

#3、引入模块的三种方法
#1)import语句
'''
import statistics 
print(statistics.median([19,-15,36]))
print(statistics.mean([19,-15,36]))
'''
#2)from...import...
'''
from statistics import median , mean #推荐，来源清楚,代码简洁
print(median([19,-15,36]))
print(mean([19,-15,36]))
'''
#3)from...import*
'''
from statistics import* #不太推荐，不同模块间可能会有重名函数
print(median([19,-15,36]))
print(mean([19,-15,36]))
'''

#practice
#1)题目:写一段代码:导入statistics模块，输入一组学生的考试成绩,分别输出:众数（mode）,平均分(mean),中位数(median),最高分和最低分
'''
student_scores = [67,47,85,37,39]
from statistics import mean , median , mode
print(mean(student_scores))
print(median(student_scores))
print(mode(student_scores))
print(max(student_scores))
print(min(student_scores))
'''
#2)题目:比较from...import...和import
'''
list1 = [100,-50,25,75]
import statistics
print(statistics.mean(list1))
print(statistics.median(list1))
from statistics import mean , median
print(mean(list1))    #是mean(),即函数名()
print(median(list1))     #函数用函数名（） , 方法用方法名.()
'''



