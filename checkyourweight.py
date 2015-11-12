#weight = input('input your weight:')
#height=input ('input your height：')
weight=84
height=1.78
bmi=weight/(height*height)
print('bmi: %2f' % bmi)
if bmi<18.5:

    print('过轻')
	
elif bmi>18.5 and bmi<25:
    
    print('过轻')
	
elif bmi>25 and bmi<28:

    print('过重')
	
elif bmi>28 and bmi<32:

    print('肥胖')	
	
else :

    print('严重肥胖')