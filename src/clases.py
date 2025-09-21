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
        self.more_products = []  # Список продуктов не подходящих категориям Smartphone и LawnGrass

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт'

    def __add__(self, other):
        if not isinstance(other, Product):  # Проверяем, является ли другой объект Product
            raise TypeError(f"Cannot add ___ and {type(other).__name__}")
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать объекты разных классов продуктов")
        all_price = self.quantity * self.price + other.quantity * other.price
        return all_price

    def add_more_product(self):
        pass

    @classmethod
    def new_product(cls, product_data: dict):
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        if name is None or description is None or price is None or quantity is None:
            return "Все параметры продукта должны быть добавлены"

        return cls(name, description, price, quantity)


class Category:
    name: str
    description: str
    _products: list

    categori_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        if products is None:
            self._products = []
        else:
            self._products = products

        Category.categori_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    @property
    def products(self):
        return self._products

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
            Category.product_count += 1  # Увеличиваем общее количество продуктов
            print(f"Товар '{product.name}' добавлен в категорию '{self.name}'")
        else:
            print(f"Ошибка: Объект '{product}' не является экземпляром класса Product и дочеррних классов.")

    @classmethod
    def get_total_categories(cls):
        return cls.categori_count

    @classmethod
    def get_total_products(cls):
        return cls.product_count


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
        self.lawngrass = []  # Список продуктов класса Lawngrass


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        self.smartphone = []  # Список продуктов класса Smartphone
