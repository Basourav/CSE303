def Palindromecheaker2019_2_60_079(s):
    return s == s[::-1]


s = input("enter the word:")
ans = Palindromecheaker2019_2_60_079(s)

if ans:
    print("Yes")
else:
    print("No")