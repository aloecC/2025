from src.clases import Category, Product
import unittest


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.category = Category("Test Category", "This is a category description")
        self.product1 = Product("Product 1", "Description 1", 19.99, 5)
        self.product2 = Product("Product 2", "Description 2", 15.99, 3)

    def tearDown(self):
        del self.category
        del self.product1
        del self.product2


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
        result = f'{self.product1.quantity * self.product1.price + self.product2.quantity * self.product2.price} руб.'
        self.assertEqual(result, '147.92 руб.')

class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Test Category", "This is a category description")
        self.product1 = Product("Product 1", "Description 1", 19.99, 5)
        self.product2 = Product("Product 2", "Description 2", 15.99, 3)

    def tearDown(self):
        del self.category
        del self.product1
        del self.product2


    def test_category_initialization(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "This is a category description")
        self.assertEqual(Category.get_total_categories(), 1)#2 при запуске TestCategory
        self.assertEqual(Category.get_total_products(), 0)#1 при запуске TestCategory

    def test_category_add_product(self):
        self.category.add_product(self.product1)

        self.assertEqual(Category.get_total_products(), 1)
        self.assertEqual(self.category.goods, ["Product 1, 19.99 руб. Остаток: 5 шт."])

    def test_category_multiple_products(self):
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)

        self.assertEqual(Category.get_total_products(), 2)#3 при запуске TestCategory

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




if __name__ == '__main__':
    unittest.main()