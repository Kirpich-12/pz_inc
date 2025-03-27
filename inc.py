from datetime import datetime
import os
import pandas as pd

df = pd.DataFrame(columns=['', 'User', 'Func_name', 'Time', 'Date'])



def logging(func):
    def wrapper(df = df):
        
        usr_func = func
        usr_func_name = str(usr_func.__name__)
        usr_name = os.getlogin()
        time_act = str(datetime.now().time())
        day_act =  str(datetime.now().date())
        logs = 'log.csv'
        if os.path.isfile(logs):
            file_df = pd.read_csv(logs)
            data = {'': [len(file_df)], 'User': [usr_name], 'Func': [usr_func_name], 'Time':[time_act], 'Date':[day_act]}
            df = pd.DataFrame(data)
            df.to_csv('log.csv',header=False, index=False, mode='a')
        else:
            data = {'': [len(file_df)], 'User': [usr_name], 'Func': [usr_func_name], 'Time':[time_act], 'Date':[day_act]}
            df = pd.DataFrame(data)
            df.to_csv('log.csv')
        return func()
    return wrapper

@logging
def pr():
    print('hello')

for i in range(200):
    pr()