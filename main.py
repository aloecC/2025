

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
        #Category.total_products += len(self._products)

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


