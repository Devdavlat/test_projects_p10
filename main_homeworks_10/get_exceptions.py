from data_time import get_data_time


def get_exception(exception, e):
    with open('exceptions.txt', 'a') as file:
        file.write(f'{exception} : {e} time -> {get_data_time()}\n')
