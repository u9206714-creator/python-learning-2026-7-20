#学习return的作用
#写一个计算BMI的函数
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




