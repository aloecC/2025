

class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт'
    # оптимизировать работу геттера, преобразовав объект продукта в строку.

    def __add__(self, other):
        if isinstance(other, Product):
            all_price = self.quantity * self.price + other.quantity * other.price
            return f'{all_price} руб.'
    #Для удобства работы с продуктами реализовать возможность их складывать.
    #Логика сложения должна работать так, чтобы в итоге у вас получалась полная стоимость всех товаров на складе.

    @classmethod
    def new_product(cls, product_data:dict):
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        if name is None or description is None or price is None or quantity is None:
            return "Все параметры продукта должны быть добавлены"

        return cls(name, description, price, quantity)



class Category:
    name = str
    description = str
    products = str

    total_categories = 0
    total_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._products = []

        Category.total_categories += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f'{self.name}, количество продуктов: {total_quantity} шт.'
    #В рамках реализации строкового представления для класса Category обойдите все продукты в списке
    #товаров категории, получите общее количество из атрибута количества и сложите все полученные числа.



    @property
    def goods(self):
        """
        Геттер для получения списка товаров в формате строки.
        """
        if not self._products:
            return "Нет товаров в категории."

        products_info = []
        for product in self._products:
            products_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_info

    def add_product(self, product: Product):
        """
        Добавляет объект класса Product в приватный список товаров категории.
        """
        if isinstance(product, Product):
            self._products.append(product)
            Category.total_products += 1  # Увеличиваем общее количество продуктов
            print(f"Товар '{product.name}' добавлен в категорию '{self.name}'")
        else:
            print(f"Ошибка: Объект '{product}' не является экземпляром класса Product.")

    @classmethod
    def get_total_categories(cls):
        return cls.total_categories

    @classmethod
    def get_total_products(cls):
        return cls.total_products

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)