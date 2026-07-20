#python函数（下）
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



