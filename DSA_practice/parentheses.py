s = '[()]{}{[()()()}'

z = [i for i in s]


t=[]

for i in z:
    if i in ('{', '(', '['):
        t.append(i)
        print('if wala :', t)
    else:
        curr_brac = t.pop()
        print('else wala :', t)
        if i==')' and curr_brac!='(':
            print('Unbalanced')
        elif i=='}' and curr_brac!='{':
            print('Unbalanced')
        elif i==']' and curr_brac!='[':
            print('Unbalanced')


if not t:
    print('Balanced')
            

        


# for i, col in enumerate(z):
#     print(i, col)


# print(next(z))