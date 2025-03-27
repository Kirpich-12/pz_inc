import os, datetime
print(os.getlogin())
res = datetime.datetime.now()
print(res) # выведет текущую полную дату и врем


def log(func):
    def wraple():
        f = func
        st = f.__name__
        return st
    return wraple




@log
def pr():
    return 1

print(pr())