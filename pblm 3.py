p = float(input("Enter the principal amount : "))

t = float(input("Enter the number of years : "))

r = float(input("Enter the rate of interest : "))


def compountinterest_2019_2_60_079(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)


compountinterest_2019_2_60_079(p, r,t)