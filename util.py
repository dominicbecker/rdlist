import sample

def verify_res(n, num):
    for i in xrange(1, num+1):
        assert n.data == i
        assert n.down == None
        n = n.right

def test(fn):
    sm = fn(sample.SIMPLE)
    print sm
    print_res(sm)
    verify_res(sm, 3)
    print 'simple ok\n'

    cp = fn(sample.COMPLEX)
    print cp
    print_res(cp)
    verify_res(cp, 10)
    print 'complex ok'

def print_res(n):
    while n:
        print n.data
        n = n.right
