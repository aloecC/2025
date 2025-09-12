

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

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products
        self._products = self._products = products if products is not None else []

        Category.total_categories += 1
        Category.total_products += len(self._products)

    @property
    def products(self):
        """
        Геттер для получения списка товаров в формате строки.
        """
        if not self._products:
            return "Нет товаров в категории."

        product_strings = [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]
        return "\n".join(product_strings)

    def add_product(self, product: Product):
        """
        Добавляет объект класса Product в список товаров категории.
        """
        if isinstance(product, Product):
            self._products.append(product)
            print(f"Товар '{product.name}' добавлен в категорию '{self.name}'")
        else:
            print(f"Ошибка: Объект '{product}' не является экземпляром класса Product.")

    def get_products(self):
        """
        Возвращает список товаров в категории (вспомогательный метод).
        """
        return self._products


