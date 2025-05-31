from m_calc import m_calc

res = 0
num1 = 0
num2 = 0
op = ""
con = ""
mycalc = m_calc(0,0)

while con!= 'q' :
    op = input("연산자 : ")
    num1 = int(input("숫자1 : "))
    num2 = int(input("숫자2 : "))

    mycalc.setnum(num1, num2)

    if op == '+':
        mycalc.plus()
    elif op == '-':
        mycalc.minus()
    elif op == '*':
        mycalc.mul()
    elif op == '/':
        mycalc.div()

    con = input("계속하시겠습니까? (중단 : q입력) : ")

