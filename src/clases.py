

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

        self.more_products = []#Список продуктов не подходящих категориям Smartphone и LawnGrass

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт'
    # оптимизировать работу геттера, преобразовав объект продукта в строку.

    def __add__(self, other):
        if type(self) is type(other):  # Проверяем, являются ли объекты одного типа
            all_price = self.quantity * self.price + other.quantity * other.price
            return f'{all_price} руб.'
        raise TypeError(f"Cannot add {type(self).__name__} and {type(other).__name__}")


        #if isinstance(other, Product):
        #all_price = self.quantity * self.price + other.quantity * other.price
        #return f'{all_price} руб.'

    #Для удобства работы с продуктами реализовать возможность их складывать.
    #Логика сложения должна работать так, чтобы в итоге у вас получалась полная стоимость всех товаров на складе.

    def add_more_product(self):
        pass

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
        if isinstance(product, Product) or isinstance(product, Smartphone) or isinstance(product, LawnGrass):
            self._products.append(product)
            Category.total_products += 1  # Увеличиваем общее количество продуктов
            print(f"Товар '{product.name}' добавлен в категорию '{self.name}'")
        else:
            print(f"Ошибка: Объект '{product}' не является экземпляром класса Product и дочеррних классов.")

    @classmethod
    def get_total_categories(cls):
        return cls.total_categories


    @classmethod
    def get_total_products(cls):
        return cls.total_products


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,  country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
        self.lawngrass = [] #Список продуктов класса Lawngrass

    def __add__(self, other):
        if not isinstance(other, LawnGrass):  # Проверяем, является ли другой объект lawngrass
            raise TypeError(f"Cannot add LawnGrass and {type(other).__name__}")
        all_price = self.quantity * self.price + other.quantity * other.price
        return f'{all_price} руб.'

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        self.smartphone = [] #Список продуктов класса Smartphone

    def __add__(self, other):
        if not isinstance(other, Smartphone):  # Проверяем, является ли другой объект Smartphone
            raise TypeError(f"Cannot add Smartphone and {type(other).__name__}")
        all_price = self.quantity * self.price + other.quantity * other.price
        return f'{all_price} руб.'