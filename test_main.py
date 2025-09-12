
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



    def test_category_initialization(self):
        product1 = Product("Product 1", "Description 1", 19.99, 5)
        product2 = Product("Product 2", "Description 2", 15.99, 3)
        product3 = Product("Product 3", "Description 2", 15.00, 3)
        category = Category("Test Category", "This is a category description", [product1, product2])

        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "This is a category description")
        self.assertEqual(len(category._products), 2)
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Category.total_products, 2)

        # Создаем еще одну категорию для тестирования
        category2 = Category("Another Category", "Another description", [product3])
        self.assertEqual(Category.total_categories, 2)
        self.assertEqual(Category.total_products, 3)  # Количество продуктов должно измениться

    def test_category_add_and_get_product(self):
        product1 = Product("laptop", "Description 1", 19.99, 5)
        product2 = Product("Phone", "Description 2", 15.99, 3)
        category = Category("Another Category", "Another description", [])
        category.add_product(product2)
        self.assertEqual(category._products,  [product2]) # Проверяем добавленный продукт

        category.get_products()
        self.assertEqual(category._products, [product2]) # Проверяем список продуктов

    def test_products(self):
        product1 = Product("laptop", "Description 1", 19.99, 5)
        product2 = Product("Phone", "Description 2", 15.99, 3)
        category = Category("Another Category", "Another description", [product1, product2])

        # Ожидаемая строка
        expected_output = (
            "laptop, 19.99 руб. Остаток: 5 шт.\n"
            "Phone, 15.99 руб. Остаток: 3 шт."
        )

        # Проверяем, что вывод соответствует ожидаемому
        self.assertEqual(category.products, expected_output)



if __name__ == '__main__':
    unittest.main()
