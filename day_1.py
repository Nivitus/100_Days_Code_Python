def prime_or_not():
    num = int(input())
    is_prime = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = True
                break
    if is_prime:
        print("Not an Prime")
    else:
        print("Prime number")
prime_or_not()


    
