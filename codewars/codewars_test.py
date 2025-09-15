# import unittest


STRANGE_STRING = 'ß'

r = STRANGE_STRING.upper().lower()








#
# class TestWasPackageReceivedYesterday(unittest.TestCase):
#     def test_should_return_boolean(self):
#         self.assertIsInstance(was_package_received_yesterday(1, 1, 1, 1), bool)
#         self.assertIsInstance(was_package_received_yesterday(12, -11, 5, 6), bool)
#
#     def test_same_zone(self):
#         self.assertFalse(was_package_received_yesterday(0, 0, 0, 0))
#         self.assertFalse(was_package_received_yesterday(1, 1, 0, 1))
#         self.assertFalse(was_package_received_yesterday(-11, -11, 12, 8))
#
#     def test_east_to_zone(self):
#         self.assertFalse(was_package_received_yesterday(1, 5, 6, 3))
#         self.assertFalse(was_package_received_yesterday(-11, -8, 3, 12))
#
#     def test_west_past_midnight(self):
#         self.assertTrue(was_package_received_yesterday(7, 1, 5, 0))
#         self.assertTrue(was_package_received_yesterday(7, -3, 5, 3))
#
#     def test_west_not_past_midnight(self):
#         self.assertFalse(was_package_received_yesterday(7, 1, 5, 6))
#         self.assertFalse(was_package_received_yesterday(7, -3, 5, 8))
#
# if __name__ == "__main__":
#     unittest.main()

