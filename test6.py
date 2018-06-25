x = input()

result = 0

Nof5 = x/5
while Nof5 >= 0:
    yuE5 = x - 5*Nof5
    Nof5 -= 1

    Nof2 = yuE5/2
    while Nof2 >= 0:
        yuE2 = yuE5 - 2*Nof2
        Nof2 -= 1
        result += 1
        # result << << Nof5 << << Nof2 <<<< yuE2 <<<< (Nof5+Nof2+yuE2)

print result


