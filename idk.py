numbers = ["null", "üks", "kaks", "kolm", "neli", "viis", "kuus", "seitse", "kaheksa", "üheksa"]
nr = 20
if len(str(nr)) == 1:
    print (numbers[int(nr)])
elif len(str(nr)) == 2: 
    a = (nr % 10)
    m = (nr - a)
    n = (m / 10)
    print (n, a)
    if nr in range (11, 19):
        print (numbers[int(n)] + "teist")
    if a == 1:
        print (numbers[int(n)] + "kümmend"
    else:
        print (numbers[int(n)] + "kümmend", numbers[int(a)])
elif len(str(nr)) == 3: 
    a = (nr % 100)
    m = (nr - a)
    c = (a % 10)
    b = (a - c)
    print (m, b, c)
    v = (m / 100)
    x = (b / 10)
    print (numbers[int(v)] + "sada", numbers[int(x)] + "kümmend", numbers[int(c)])