def marks():
    name = input('enter the student name :')
    sub1 =int(input('enter the marks of the sub1 :'))
    sub2 = int(input('enter the marks of the sub2 :'))
    sub3 = int(input('enter the marks of the sub3 :'))
    total = sub1 + sub2 + sub3
    ave = (sub1 + sub2 + sub3) / 3
    if 0 < sub1 <= 39:
        print('fail')
        print('grad --> F')
    elif 39 < sub1 <= 44:
        print('pass')
        print('grad -->P')
    elif 44 < sub1 <= 49:
        print('pass')
        print('grad -->c')
    elif 49 < sub1 <= 54:
        print('pass')
        print('grad -->B')
    elif 54 < sub1 <= 59:
        print('pass')
        print('grad -->B+')
    elif 59 < sub1 <= 69:
        print('pass')
        print('grad -->A')
    elif 69 < sub1 <= 79:
        print('pass')
        print('grad -->A+')
    elif 79 < sub1 <= 100:
        print('pass')
        print('grad -->O')

    if 0 < sub2 <= 39:
        print('fail')
        print('grad --> F')
    elif 39 < sub2 <= 44:
        print('pass')
        print('grad -->P')
    elif 44 < sub2 <= 49:
        print('pass')
        print('grad -->c')
    elif 49 < sub2 <= 54:
        print('pass')
        print('grad -->B')
    elif 54 < sub2 <= 59:
        print('pass')
        print('grad -->B+')
    elif 59 < sub2 <= 69:
        print('pass')
        print('grad -->A')
    elif 69 < sub2 <= 79:
        print('pass')
        print('grad -->A+')
    elif 79 < sub2 <= 100:
        print('pass')
        print('grad -->O')
    if 0 < sub3 <= 39:
        print('fail')
        print('grad --> F')
    elif 39 < sub3 <= 44:
        print('pass')
        print('grad -->P')
    elif 44 < sub3 <= 49:
        print('pass')
        print('grad -->c')
    elif 49 < sub3 <= 54:
        print('pass')
        print('grad -->B')
    elif 54 < sub3 <= 59:
        print('pass')
        print('grad -->B+')
    elif 59 < sub3 <= 69:
        print('pass')
        print('grad -->A')
    elif 69 < sub3 <= 79:
        print('pass')
        print('grad -->A+')
    elif 79 < sub3 <= 100:
        print('pass')
        print('grad -->O')


marks()
