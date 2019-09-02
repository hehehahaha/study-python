def sqrtBI(x, epsilon):
    assert x>0, 'X must be non-nagtive, not ' + str(x)
    assert epsilon > 0, 'epsilon must be postive, not ' + str(epsilon)

    low = 0
    high = x
    guess = (low + high)/2.0
    counter = 1
    while (abs(guess ** 2 - x) > epsilon) and (counter <= 100):
        if guess ** 2 < x:
            low = guess
        else :
            high = guess
        guess = (low + high)/2.0
        counter += 1
    return guess
a = sqrtBI(2,0.001)
print(a)
