import csv
from pprint import pprint
from get_exceptions import get_exception


class Country:
    def __init__(self, file):
        self.file = file

    def read_file(self):
        try:
            open(self.file)
        except Exception as e:
            get_exception(Exception, e)
        else:
            with open(self.file, 'r') as file:
                res = csv.DictReader(file)
                return [i for i in res]

    def get_population(self, values):
        res = {}
        for i in self.read_file():
            if int(i.get(values)) > 20000000:
                res[i.get('Country')] = i.get(values)
        return res

    def get_gdp(self, values):
        res = {}
        for i in self.read_file():
            if int(i.get(values)) > 1000:
                res[i.get('Country')] = i.get(values)
        return res

    def get_gdp_country(self, values):
        full_info = self.read_file()
        gdp_country = {}
        for i in full_info:
            try:
                int(i.get(")").strip())
            except Exception as e:
                get_exception(Exception, e)

            else:
                if int(i.get("GDP ($ per capita)").strip()) > 1000:
                    gdp_country[i.get('Country')] = i.get("GDP ($ per capita)")
        return gdp_country

    def get_country_names_with_c(self, values):
        # res = []

        # for i in self.read_file():
        #     country_name = i.get(values)
        #     char = "c"
        #     if country_name[0].lower() == char:
        #         res.append(i.get(values))

        return [i.get('Country') for i in self.read_file() if i.get('Country')[0] == "C"]

        # for i in self.read_file():
        #     country_name = i.get(values)
        #     char = "c"
        #     if country_name[0].lower() == char:
        #         res.append(i.get(values))
        # return res


country_obj = Country('countries of the world.csv')
# pprint(country_obj.read_file())
# pprint(country_obj.get_population("Population"))
print(country_obj.get_country_names_with_c("Country"))
# pprint(country_obj.get_gdp('GDP ($ per capita)'))
# print(country_obj.get_gdp_country("GDP ($ per capita)"))
