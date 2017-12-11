from unittest import TestCase

import lib


class TestLib(TestCase):
    def test_email_validation(self):
        sample_1 = "invalid"
        self.assertFalse(lib.email_validation(sample_1))

        sample_2 = "me@morteza"
        self.assertFalse(lib.email_validation(sample_2))

        sample_3 = "me@morteza.123"
        self.assertFalse(lib.email_validation(sample_3))

        sample_4 = "me@morteza12@.com"
        self.assertFalse(lib.email_validation(sample_4))

        sample_5 = "me@motezana.com"
        self.assertTrue(lib.email_validation(sample_5))

    def test_num_validation(self):

        sample_5 = "12345678909887"
        self.assertTrue(number_validation(sample_5))  # check function if return True

        sample_2 = "is not digit "      # check function if raise a exception
        self.assertRaises(ValueError, number_validation, sample_2)

