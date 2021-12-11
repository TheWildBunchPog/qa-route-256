import copy

import json
import openpyxl

from builder import Builder


class ApiBase:

    def generated_json(self):
        builder = Builder().generated_fake_data()

        # Собираем json
        product_information = {
            "id": n,
            "article": builder.article,
            "category": builder.category,
            "weight": builder.weight_product[builder.category],
            "type": builder.type_product[builder.category],
            "colour": builder.color,
            "textile": [
                {
                    "material": "cotton",
                    "percent": builder.textile_material["cotton"]
                },
                {
                    "material": "acrylic",
                    "percent": builder.textile_material["acrylic"]
                },
                {
                    "material": "viscose",
                    "percent": builder.textile_material["viscose"]
                }
            ],
            "description": builder.description
        }

        # Избавляемся от ключей с пустыми значениями
        product_information = {key: value for key, value in product_information.items() if value}

        # Избавляемся в ключе "textile" от материала с 0%
        for i in reversed(product_information["textile"]):
            if i["percent"] == 0:
                product_information["textile"].remove(i)

        return product_information

    def generated_exel(self):

        # создаем книгу
        book = openpyxl.Workbook()
        # удаляем стандартную страницу Sheet
        book.remove(book.active)

        # создаем страницу "Товары"
        sheet = book.create_sheet("Товары")

        # создаем копию сгенерированного списка товаров
        product_list_exel = copy.deepcopy(product_list)

        # добавляем на страницу "Товары" заголовки
        headlines = ["id", "article", "category", "weight", "type", "colour", "textile", "description"]
        sheet.append(headlines)

        for product in product_list_exel:
            dict = {}
            for relation in product["textile"]:

                dict.update({relation["material"]: relation["percent"]})

            # Сортируем "textile" по материалу
            dict = sorted(dict.items(), key=lambda x: -x[1])

            # Собираем "textile" по формату
            composition = []
            for key, value in dict:
                composition.append(f'{value}% {key}')

            product["textile"] = ', '.join(composition)

            # Для товаров категории "socks" добавляем пустое поле в заголовок "Type"
            product = list(product.values())
            if product[2] == 'socks':
                product.insert(4, '')

            # Записываем товар в таблицу
            sheet.append(product)

        # Сохраняем таблицу
        book.save("product.xlsx")


if __name__ == "__main__":
    number_of_goods = int(input())

    product_list = []
    for n in range(1, number_of_goods + 1):
        product_list.append(ApiBase().generated_json())

    ApiBase().generated_exel()

    print(json.dumps(product_list, indent=4))
