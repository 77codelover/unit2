def positional(a,b,c):
    print(a,b,c)
a='a'
b='b'
c='c'
positional(a,b,c)

def keyword(a,b,c):
    print(a,b,c)
a='a'
b='b'
c='c'
keyword(a='a',b='b',c='c')

def default(a,b,c='c'):
    print(a,b,c)
a='a'
b='b'
default(a='a',b='b')
    