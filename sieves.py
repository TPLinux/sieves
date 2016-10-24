# coding: utf8

from __future__ import print_function


print("\n\n# Coded By : @i127001")
print("# Link     : https://twitter.com/i127001\n\n\n")

s = (0, 37.5, 19, 9.5, 4.75, 2.36, 1.18, 0.6, 0.3, 0.15)


def p_n(n):
    if(n < 10):
        return '00%.2f' % n
    elif(n > 10 and n < 100):
        return '0%.2f' % n
    else:
        return '%.2f' % n


# Percentages
def run():
    try:
        global p1, p2, p3, p4, p5, p6, p7, p8, p9, cont
        p1 = float(raw_input("Insert 1nd percentage: "))
        p2 = float(raw_input("Insert 2nd percentage: "))
        p3 = float(raw_input("Insert 3nd percentage: "))
        p4 = float(raw_input("Insert 4nd percentage: "))
        p5 = float(raw_input("Insert 5nd percentage: "))
        p6 = float(raw_input("Insert 6nd percentage: "))
        p7 = float(raw_input("Insert 7nd percentage: "))
        p8 = float(raw_input("Insert 8nd percentage: "))
        p9 = float(raw_input("Insert 9nd percentage: "))
        cont = float(raw_input("Insert CONT percentage: "))
    except ValueError:
        print('You must insert a FLOAT Number')
        raw_input("\n\nPress ENTER to retry ...\n\n")
        run()
try:
    run()
except KeyboardInterrupt:
    print("\n-------\nExited!\n-------\n")
    exit()

# % Summation
sum1 = p1
sum2 = sum1 + p2
sum3 = sum2 + p3
sum4 = sum3 + p4
sum5 = sum4 + p5
sum6 = sum5 + p6
sum7 = sum6 + p7
sum8 = sum7 + p8
sum9 = sum8 + p9
sum_cont = sum9 + cont

# % Passing
passed_arr = (
    0,
    100 - sum1,
    100 - sum2,
    100 - sum3,
    100 - sum4,
    100 - sum5,
    100 - sum6,
    100 - sum7,
    100 - sum8,
    100 - sum9,
    100 - sum_cont
    )

# Fineness Modulus

f_m = sum9 / 100

print("+------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")  # noqa
print("| Sieve-NO   | %s | %s | %s | %s | %s | %s | %s | %s | %s |  Cont  |" % (p_n(s[1]), p_n(s[2]), p_n(s[3]), p_n(s[4]), p_n(s[5]), p_n(s[6]), p_n(s[7]), p_n(s[8]), p_n(s[9])))  # noqa
print("+------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")  # noqa
print("| %% Retained | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (p_n(p1), p_n(p2), p_n(p3), p_n(p4), p_n(p5), p_n(p6), p_n(p7), p_n(p8), p_n(p9), p_n(cont)) )  # noqa
print("+------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")  # noqa
print("| %% Sum      | %s | %s | %s | %s | %s | %s | %s | %s | %s | ------ |" % (p_n(sum1), p_n(sum2), p_n(sum3), p_n(sum4), p_n(sum5), p_n(sum6), p_n(sum7), p_n(sum8), p_n(sum9)) )  # noqa
print("+------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")  # noqa
print("| %% Passed   | %s | %s | %s | %s | %s | %s | %s | %s | %s | ------ |" % (p_n(passed_arr[1]), p_n(passed_arr[2]), p_n(passed_arr[3]), p_n(passed_arr[4]), p_n(passed_arr[5]), p_n(passed_arr[6]), p_n(passed_arr[7]), p_n(passed_arr[8]), p_n(passed_arr[9])))  # noqa
print("+------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")  # noqa


# Points
print("--> Points <--")
print("+--------+--------+")
print("|   X    |    Y   |")
print("+--------+--------+")

for i in range(1, 10):
    print("| %s | %s |" % (p_n(s[i]), p_n(passed_arr[i])))
    print("+--------+--------+")


print("Fineness Modulus = %s" % (p_n(f_m)))
