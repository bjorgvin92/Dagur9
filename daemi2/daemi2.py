
def is_float(s):# is_float function definition goes here
    try:
        float(s)
        return True
    except Exception:
        return False
# Do not change the lines below
print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))