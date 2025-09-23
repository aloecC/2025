from src.clases import Category, Product, Smartphone, LawnGrass
import unittest


class TestBaseProduct(unittest.TestCase):
    def setUp(self):
        self.category = Category("Test Category", "This is a category description")
        self.product1 = Product("Product 1", "Description 1", 19.99, 5)
        self.product2 = Product("Product 2", "Description 2", 15.99, 3)
        self.smartphone1 = Smartphone("IPhone", "В новом дизайне", 39000, 5, "4325 мА·ч", "12", "128гб", 'blue')
        self.smartphone2 = Smartphone("IPhone", "В новом дизайне", 89000, 15, "4325 мА·ч", "15", "256гб", 'green')
        self.lawngrass1 = LawnGrass('Grably', "Лучше, чем у конкурентов", 2000, 35, "Russia", "1 year", "green")
        self.lawngrass2 = LawnGrass('MaxGrass', "Газон вашей мечты", 1000, 15, "Germany", "2 years", "green")

    def tearDown(self):
        del (self.category, self.product1, self.product2, self.smartphone1, self.smartphone2, self.lawngrass1,
             self.lawngrass2)

    def test_change_price(self):
        self.assertEqual(self.lawngrass1.price, 2000)
        new_price = 2500
        self.lawngrass1.change_price(new_price)
        self.assertEqual(self.lawngrass1.price, 2500)

    def test_apply_discount(self):
        self.assertEqual(self.lawngrass1.price, 2000)
        discont = 300
        self.lawngrass1.apply_discount(discont)
        self.assertEqual(self.lawngrass1.price, 1700)

    def test_get_info(self):
        self.assertEqual(self.lawngrass1.get_info(), f'LawnGrass: {self.lawngrass1.name},'
                                                     f' Период: {self.lawngrass1.germination_period},'
                                                     f' Цена: {self.lawngrass1.price} руб.,'
                                                     f' Остаток: {self.lawngrass1.quantity} шт.')


class TestInfoMixin(unittest.TestCase):
    def setUp(self):
        self.category = Category("Test Category", "This is a category description")
        self.product1 = Product("Product 1", "Description 1", 19.99, 5)
        self.product2 = Product("Product 2", "Description 2", 15.99, 3)
        self.smartphone1 = Smartphone("IPhone", "В новом дизайне", 39000, 5, "4325 мА·ч", "12", "128гб", 'blue')
        self.smartphone2 = Smartphone("IPhone", "В новом дизайне", 89000, 15, "4325 мА·ч", "15", "256гб", 'green')
        self.lawngrass1 = LawnGrass('Grably', "Лучше, чем у конкурентов", 2000, 35, "Russia", "1 year", "green")
        self.lawngrass2 = LawnGrass('MaxGrass', "Газон вашей мечты", 1000, 15, "Germany", "2 years", "green")

    def tearDown(self):
        del (self.category, self.product1, self.product2, self.smartphone1, self.smartphone2, self.lawngrass1,
             self.lawngrass2)


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.category = Category("Test Category", "This is a category description")
        self.product1 = Product("Product 1", "Description 1", 19.99, 5)
        self.product2 = Product("Product 2", "Description 2", 15.99, 3)
        self.smartphone1 = Smartphone("IPhone", "В новом дизайне", 39000, 5, "4325 мА·ч", "12", "128гб", 'blue')
        self.smartphone2 = Smartphone("IPhone", "В новом дизайне", 89000, 15, "4325 мА·ч", "15", "256гб", 'green')
        self.lawngrass1 = LawnGrass('Grably', "Лучше, чем у конкурентов", 2000, 35, "Russia", "1 year", "green")
        self.lawngrass2 = LawnGrass('MaxGrass', "Газон вашей мечты", 1000, 15, "Germany", "2 years", "green")

    def tearDown(self):
        del (self.category, self.product1, self.product2, self.smartphone1, self.smartphone2, self.lawngrass1, self.lawngrass2)

    def test_product_initialization(self):
        self.assertEqual(self.product1.name, "Product 1")
        self.assertEqual(self.product1.description, "Description 1")
        self.assertEqual(self.product1.price, 19.99)
        self.assertEqual(self.product1.quantity, 5)

    def test_new_product(self):
        product_data = {
            'name': 'Product 1',
            'description': 'Description of Product 1',
            'price': 19.99,
            'quantity': 5
        }
        product = Product.new_product(product_data)

        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, 'Product 1')
        self.assertEqual(product.description, 'Description of Product 1')
        self.assertEqual(product.price, 19.99)
        self.assertEqual(product.quantity, 5)

    def test_missing_product(self):
        product_data = {
            'name': 'Product 1',
            'description': 'Description of Product 1',
            'price': 19.99,
        }
        result = Product.new_product(product_data)

        self.assertEqual(result, "Все параметры продукта должны быть добавлены")

    def test_str_product(self):
        self.assertEqual(str(self.product1), "Product 1, 19.99 руб. Остаток: 5 шт")

    def test_add_product(self):
        result = self.product1 + self.product2
        self.assertEqual(result, 147.92)

        with self.assertRaises(TypeError):
            _ = self.smartphone1 + self.lawngrass1

        result5 = self.smartphone1 + self.smartphone2
        self.assertEqual(result5, 1530000)


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Test Category", "This is a category description")
        self.product1 = Product("Product 1", "Description 1", 19.99, 5)
        self.product2 = Product("Product 2", "Description 2", 15.99, 3)
        self.smartphone1 = Smartphone("IPhone", "В новом дизайне", 39000, 5, "4325 мА·ч", "12", "128гб", 'blue')
        self.smartphone2 = Smartphone("IPhone", "В новом дизайне", 89000, 15, "4325 мА·ч", "15", "256гб", 'green')
        self.lawngrass1 = LawnGrass('Grably', "Лучше, чем у конкурентов", 2000, 35, "Russia", "1 year", "green")
        self.lawngrass2 = LawnGrass('MaxGrass', "Газон вашей мечты", 1000, 15, "Germany", "2 years", "green")

    def tearDown(self):
        del self.category
        del self.product1
        del self.product2

    def test_category_initialization(self):
        count_cat = Category.get_total_categories()
        category2 = Category('Sweet', "cool")

        self.assertEqual(category2.name, "Sweet")
        self.assertEqual(category2.description, "cool")
        self.assertEqual(Category.get_total_categories(), count_cat + 1)

    def test_category_add_product(self):
        self.category.add_product(self.smartphone1)

        self.assertEqual(Category.get_total_products(), 1)
        self.assertEqual(self.category.goods, ['IPhone, 39000 руб. Остаток: 5 шт.'])

    def test_category_multiple_products(self):
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)

        expected_output = ([
            "Product 1, 19.99 руб. Остаток: 5 шт.",
            "Product 2, 15.99 руб. Остаток: 3 шт."
        ])

        self.assertEqual(self.category.goods, expected_output)

    def test_no_products_in_category(self):
        self.assertEqual(self.category.goods, "Нет товаров в категории.")

    def test_str_category(self):
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        expected_str = 'Test Category, количество продуктов: 8 шт.'
        self.assertEqual(str(self.category), expected_str)


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone1 = Smartphone("IPhone", "В новом дизайне", 39000, 5, "4325 мА·ч", "12", "128гб", 'blue')
        self.smartphone2 = Smartphone("IPhone", "В новом дизайне", 89000, 15, "4325 мА·ч", "15", "256гб", 'green')

    def tearDown(self):
        del self.smartphone1
        del self.smartphone2

    def test_smartphone_initialization(self):
        self.assertEqual(self.smartphone1.efficiency, "4325 мА·ч")
        self.assertEqual(self.smartphone1.model, "12")
        self.assertEqual(self.smartphone1.memory, "128гб")
        self.assertEqual(self.smartphone1.color, 'blue')
        self.assertEqual(self.smartphone1.name, 'IPhone')
        self.assertEqual(self.smartphone1.description, 'В новом дизайне')
        self.assertEqual(self.smartphone1.price, 39000)
        self.assertEqual(self.smartphone1.quantity, 5)


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        self.lawngrass1 = LawnGrass('Grably', "Лучше, чем у конкурентов", 2000, 35, "Russia", "1 year", "green")
        self.lawngrass2 = LawnGrass('MaxGrass', "Газон вашей мечты", 1000, 15, "Germany", "2 years", "green")

    def tearDown(self):
        del self.lawngrass1
        del self.lawngrass2

    def test_lawngrass_initialization(self):
        self.assertEqual(self.lawngrass1.country, 'Russia')
        self.assertEqual(self.lawngrass1.germination_period, '1 year')
        self.assertEqual(self.lawngrass1.color, 'green')
        self.assertEqual(self.lawngrass1.name, 'Grably')
        self.assertEqual(self.lawngrass1.description, 'Лучше, чем у конкурентов')
        self.assertEqual(self.lawngrass1.price, 2000)
        self.assertEqual(self.lawngrass1.quantity, 35)


if __name__ == '__main__':
    unittest.main()
