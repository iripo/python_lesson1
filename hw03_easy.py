# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


#не совсем удачный вариант. 

def my_round(number, ndigits):
    k = 1/10**ndigits
    number= number+0.5*k
    number= (number+k)//k
    result= number*k
    return result

print(my_round(2.1234567, 5))
2.12346

print(my_round(2.1999967, 5))
2.2

print(my_round(2.9999967, 5))
3.0000000000000004
	
#более удачный вариант
def my_round(number, ndigits):
##    k = 10**ndigits
    k = pow(10,ndigits)
    number= number*k
    number= ((number+0.5)*k )//k
    result= number/k
    return result

	
print(my_round(2.1234567, 5))
2.12346
print(my_round(2.1999967, 5))
2.2
print(my_round(2.9999967, 5))
3.0



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

#много формул в одной строке - плохо читается, но захотелось попробовать

def lucky_ticket(ticket_number):
    n=len(str(ticket_number))
    if n != 6:
        msg = "Неверный номер билета"
    else:
        h1=sum(list(map(int, str(ticket_number)))[:3])
        h2=sum(list(map(int, str(ticket_number)))[3:])
        if h1==h2:
            msg=("Этот билет счастливый!")
        else: 
            msg=("Это обычный билет")
    return msg

	


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
