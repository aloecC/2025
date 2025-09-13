
import unittest

from main import Product, Category


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

class TestProductAndCategory(unittest.TestCase):

    def test_product_initialization(self):
        product = Product("Product 1", "Description 1", 19.99, 5)
        self.assertEqual(product.name, "Product 1")
        self.assertEqual(product.description, "Description 1")
        self.assertEqual(product.price, 19.99)
        self.assertEqual(product.quantity, 5)

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


    def test_category_initialization(self):
        category = Category("Test Category", "This is a category description")

        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "This is a category description")
        self.assertEqual(Category.get_total_categories(), 1)
        self.assertEqual(Category.get_total_products(), 0)

    def test_category_add_product(self):
        product1 = Product("Product 1", "Description 1", 19.99, 5)
        category = Category("Test Category", "This is a category description")

        category.add_product(product1)

        self.assertEqual(Category.get_total_products(), 1)
        self.assertEqual(category.goods, ["Product 1, 19.99 руб. Остаток: 5 шт."])

    def test_category_multiple_products(self):
        product1 = Product("Product 1", "Description 1", 19.99, 5)
        product2 = Product("Product 2", "Description 2", 15.99, 3)

        category = Category("Test Category", "This is a category description")

        category.add_product(product1)
        category.add_product(product2)

        self.assertEqual(Category.get_total_products(), 2)

        expected_output = ([
            "Product 1, 19.99 руб. Остаток: 5 шт.",
            "Product 2, 15.99 руб. Остаток: 3 шт."
        ])

        self.assertEqual(category.goods, expected_output)

    def test_no_products_in_category(self):
        category = Category("Empty Category", "This category has no products.")

        self.assertEqual(category.goods, "Нет товаров в категории.")



if __name__ == '__main__':
    unittest.main()
