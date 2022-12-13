text='Python is the best programming language in the world in 2020 Edureka is the biggest Ed-tech platform to learn python Python programming is as easy as writing a program in simple English language '
with open('example.txt','w') as f1:
    f1.write(text)
with open('example.txt','r') as f2:
    t1=f2.readline(5)
    print(t1)