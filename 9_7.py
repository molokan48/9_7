

def is_prime(f):
    def wrapper(*args):
        ret_func = f(*args)
        if ret_func == 2 or ret_func == 3:
            print("Простое")
            return ret_func
        for i in range(3 , ret_func , 2):
            if ret_func % 2 == 0:
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

result = sum_three(2, 3, 8)
print(result)