def eseq():
    bn = 1
    for n in range(1,100):
        previous = bn
        bn = (1 + 1.0/n)**(n+1)
        print(bn, '\t', bn/previous)

eseq()