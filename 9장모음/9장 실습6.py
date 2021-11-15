

strr=input("문자열을 입력해주세요.")
# list(strr)
digits=0
spaces=0
alphas=0

for i in strr:
    if i.isdigit()==True:
        digits = digits+1
    elif i.isspace() == True :
        spaces = spaces +1
    elif i.isalpha() == True :
        alphas = alphas +1
    else:
        pass

print("digits: %d , spaces: %d, alphas : %d" %(digits, spaces, alphas))
    # 문자열을 하나하나 isdigt() 등등 하여, 맞으면 1씩 카운트하기

