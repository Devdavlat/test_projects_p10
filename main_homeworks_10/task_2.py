import csv
from get_exceptions import get_exception
from pprint import pprint


class Country:
    def __init__(self, file_csv):
        self.file = file_csv

    @staticmethod
    def get_lat_lng(dct_, key):
        # dct_kesy = dct_.keys()
        # print(dct_kesy)
        res = {'city': dct_[key].get('city'),
               'lat': dct_[key].get('lat'),
               'lng': dct_[key].get('lng')}
        with open('lat_lng.txt', "a", encoding='utf-8') as file:
            file.write(f"{res}\n")

    def read_file(self):
        try:
            open(self.file, 'r', encoding='utf-8')
        except Exception as e:
            get_exception(Exception, e)
        else:
            with open(self.file, 'r', encoding='utf-8') as file:
                res = csv.DictReader(file)
                return [i for i in res]

    def read_uzbekistan_country(self):
        full_info = self.read_file()

        result = []
        res = None
        for index in range(len(full_info)):
            res = {}
            data = full_info[index]

            try:
                data.get("country")
            except Exception as e:
                get_exception(Exception, e)

            else:
                if data.get('country') == 'Uzbekistan':
                    # print(data)
                    res[index + 1] = data
                    # print(res)
                    # result.append(res)
                    self.get_lat_lng(res, index + 1)
                    file = open('uzbekistan_country.txt', 'a+', encoding='utf-8')
                    file.writelines(f'{res}')

        return res


country_obj = Country('worldcities.csv')
pprint(country_obj.read_uzbekistan_country())
