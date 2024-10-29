
def is_prime(f):
    def wrapper(*args):
        ret_func = f(*args)
        if ret_func <=3 :
            print("Простое")
            return ret_func
        else:
            for i in range(3 , int(ret_func)):
                if  ret_func % i == 0:
                    print("Составное")
                    return ret_func
            else:
                    print("Простое")
                    return ret_func
    return wrapper

@is_prime
def sum_three(*args):
    r = sum(args)
    return r

result = sum_three(5, 0, 2)
print(result)
