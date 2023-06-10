import unittest
from shopping_cart import Cart

class TestShoppingCart(unittest.TestCase):
    def test_add(self):
        cart = Cart()
        cart.add()

    def test_remove(self):
        cart = Cart()
        cart.grocery_dict = {'apple': {'quantity': 5, 'price': 1.0}}
        cart.remove()
        self.assertNotIn('apple', cart.grocery_dict)

    def test_show(self):
        cart = Cart()
        cart.grocery_dict = {'apple': {'quantity': 5, 'price': 1.0}}
        output = cart.show()
        self.assertEqual(output.strip(), "{'apple': {'quantity': 5, 'price': 1.0}}")

if __name__ == '__main__':
    unittest.main()
