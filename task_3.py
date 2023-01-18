# a) Macbook Pro Laptop mahsulotdan nechta buyurtma bo'lganini aniqlang.
# b) Price Each ustun orqali 300 dan katta bo'lgan buyurtmalarni txt faylga yozing.
# c) 04/10/19 sanadan keyingi buyurmalarni boshqa csv faylga yozing
import csv
import math
from get_exceptions import get_exception
from pprint import pprint


class Prodcuts:
    def __init__(self, file_csv):
        self.file = file_csv

    def read_file(self):
        try:
            open(self.file)
        except Exception as e:
            get_exception(Exception, e)
        else:
            with open(self.file, 'r') as file:

                res = csv.DictReader(file)
                file1 = [i for i in res]
                return file1

    def get_macbook_pro_orders_number(self):
        data = self.read_file()
        counter = 0
        for data_dict in data:
            try:
                temp_data = data_dict.get('Product')
            except Exception as e:
                get_exception(Exception, e)
            else:
                # print(temp_data)

                if temp_data == "Macbook Pro Laptop":
                    counter += 1

        return counter

    def write_txt_which_is_under_300(self):
        data = self.read_file()
        for data_dict in data:
            temp_price = data_dict.get('Price Each')
            try:
                open("price_each.txt", 'a', encoding='utf-8')
            except Exception as e:
                get_exception(Exception, e)
            else:
                with open("price_each.txt", 'a', encoding='utf-8') as file:
                    try:
                        math.floor(float(temp_price))
                    except Exception as e:
                        get_exception(Exception, e)
                    else:
                        if math.floor(float(temp_price)) > 300:
                            res = f'name : {data_dict.get("Product")}\t' \
                                  f'price : {temp_price}'
                            file.write(f'{res}\n')

    @staticmethod
    def is_expire_from_data(given_date, lst_):
        lst_.sort()
        if lst_[0] == given_date:
            return True
        else:
            return False

    def write_csv_which_is_expire_from_data(self):
        data = self.read_file()
        given_data_for_sort = "04/10/19"
        for data_dict in data:

            expire_data_list = ["04/10/19"]
            temp_order = data_dict.get('Order Date')
            temp_order = temp_order[:8]
            expire_data_list.append(temp_order)
            is_expire = self.is_expire_from_data(given_data_for_sort, expire_data_list)

            if is_expire:
                try:
                    open("expired_products_by_date.csv", 'w', newline='')
                except Exception as e:
                    get_exception(Exception, e)
                else:
                    with open("no_expired_products_by_date.csv", 'w', newline='') as file:
                        heads = ['ID', 'Product', 'Quantity Ordered', 'Price Each', "Order Date", "Purchase Address"]
                        writer = csv.DictWriter(file, fieldnames=heads)
                        writer.writeheader()
                        writer.writerow(
                            {'ID': data_dict.get('ID'),
                             'Product': data_dict.get('Product'),
                             'Quantity Ordered': data_dict.get('Quantity Ordered'),
                             'Price Each': data_dict.get('Price Each'),
                             "Order Date": data_dict.get('Order Date'),
                             "Purchase Address": data_dict.get('Purchase Address')})


computer_obj = Prodcuts('Sales_April_2019.csv')
# pprint(computer_obj.get_macbook_pro_orders_number())
# pprint(computer_obj.write_txt_which_is_under_300())
print(computer_obj.write_csv_which_is_expire_from_data())

# names = ['a', 'b']
# with open('names.csv', 'w', newline='') as csvfile:
#     for i in names:
#         fieldnames = ['ID', 'UD']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow({'ID': i, 'UD': 'i'})
#     # writer.writerow({'ID': 'Lovely', 'UD': 'Spam'})
#     # writer.writerow({'ID': 'Wonderful', 'UD': 'Spam'})
