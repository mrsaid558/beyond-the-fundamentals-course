# this is lesson number 5 in chapter 7
# creating a test case

def check_temp(temp):
    if temp < 15:
        print("wear a jacket")
    elif temp > 25 and temp <= 35:
        print("pack a jacket")
    elif temp > 35:
        print("leave the jacket at home")
check_temp(10)
check_temp(30)
check_temp(37)