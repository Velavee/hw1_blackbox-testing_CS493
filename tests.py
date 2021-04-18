# Credit Card Validator Tests
# Author: Gabrielle Josephson
# CS 362 - Software Engineering II, Spring 2021
# Date Due: 4/19/2021

import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    # Check that a credit card number of length zero is invalid
    # Category: Error Testing
    def test_1(self):
        self.assertEqual(credit_card_validator(''), False)

    # Check that valid Visa number works (prefix 4)
    # Picked to test valid number no on any boundaries
    def test_2(self):
        self.assertEqual(credit_card_validator('4136090845728260'), True)

    # Check that valid MasterCard number with prefix 51 works
    # Category: Boundary Testing
    def test_3(self):
        self.assertEqual(credit_card_validator('5100060000000002'), True)

    # Check that valid Mastercard number with prefix range 51-55 works
    # Picked valid number
    def test_3(self):
        self.assertEqual(credit_card_validator('5574843460000654'), True)

    # Check that valid MasterCard number with prefix 2221 works
    # Category: Boundary Testing
    def test_4(self):
        self.assertEqual(credit_card_validator('2221410700000003'), True)

    # Check that valid Mastercard number with prefix range 2221-2720 works
    # Picked valid number
    def test_5(self):
        self.assertEqual(credit_card_validator('2222410700000002'), True)

    # Check that valid MasterCard number with prefix 2720 works
    # Category: Boundary Testing
    def test_6(self):
        self.assertEqual(credit_card_validator('2720410700000009'), True)

    # Check that valid American Express number works (prefix 34)
    # Picked valid number not on boundary
    def test_7(self):
        self.assertEqual(credit_card_validator('348061068811416'), True)

    # Check that valid American Express number works (prefix 37)
    # Picked valid number not on boundary
    def test_8(self):
        self.assertEqual(credit_card_validator('370000000000002'), True)

    # Check that Visa number with invalid checksum does not work
    # Category: Partition Testing - isolating checksum
    def test_9(self):
        self.assertEqual(credit_card_validator('4136090845728268'), False)

    # Check that Mastercard number with invalid checksum does not work
    # Category: Partition Testing - isolating checksum
    def test_10(self):
        self.assertEqual(credit_card_validator('5574843460000650'), False)

    # Check that American Express number with invalid checksum does not work
    # Category: Partition Testing - isolating checksum
    def test_11(self):
        self.assertEqual(credit_card_validator('348061068811412'), False)

    # Check that Visa with wrong prefix (3) does not work
    # Category: Partition/Boundary Testing - 3 is one less than 4
    def test_12(self):
        self.assertEqual(credit_card_validator('3136090845728262'), False)

    # Check that Visa with wrong prefix (5) does not work
    # Category: Partition/Boundary Testing - 4 is one more than 4
    def test_13(self):
        self.assertEqual(credit_card_validator('5736090845728267'), False)

    # Check that MasterCard with wrong prefix (50 - Below lower range) does not work
    # Category: Partition/Boundary Testing - 50 is one less than 51
    def test_14(self):
        self.assertEqual(credit_card_validator('5074843460000659'), False)

    # Check that MasterCard with wrong prefix (56 - Above lower range) does not work
    # Category: Partition/Boundary Testing - 56 is one more than 55
    def test_15(self):
        self.assertEqual(credit_card_validator('5674843460000653'), False)

    # Check that MasterCard number with wrong prefix (2220 - Below upper range) does not work
    # Category: Partition/Boundary Testing - 2220 is one less than 2221
    def test_16(self):
        self.assertEqual(credit_card_validator('2220410700000004'), False)

    # Check that MasterCard number with wrong prefix (2721 - Above upper range) does not work
    # Category: Partition/Boundary Testing - 2721 is one more than 2720
    def test_17(self):
        self.assertEqual(credit_card_validator('2721410700000008'), False)

    # Check that American Express number with wrong prefix (33) does not work
    # Category: Partition/Boundary Testing 33 is one less than 34
    def test_18(self):
        self.assertEqual(credit_card_validator('338061068811418'), False)

    # Check that American Express number with wrong prefix (38) does not work
    # Category: Partition/Boundary Testing - 38 is one more than 37
    def test_19(self):
        self.assertEqual(credit_card_validator('388061068811417'), False)

    # Check that Visa card that is too short (15) does not work
    # Category: Partition/Error Testing - isolating length
    def test_20(self):
        self.assertEqual(credit_card_validator('413609084572824'), False)

    # Check that Visa card that is too long (17) does not work
    # Category: Partition/Error Testing - isolating length
    def test_21(self):
        self.assertEqual(credit_card_validator('41360908457282608'), False)

    # Check that MasterCard number that is too short (15) does not work
    # Category: Partition/Error Testing - isolating length
    def test_22(self):
        self.assertEqual(credit_card_validator('557484346000063'), False)

    # Check that MasterCard number that is too long (17 digits) does not work
    # Category: Partition/Error Testing - isolating length
    def test_23(self):
        self.assertEqual(credit_card_validator('55748434600006326'), False)

    # Check that American Express number that is too short (14 digits) does not work
    # Category: Partition/Error Testing - isolating length
    def test_24(self):
        self.assertEqual(credit_card_validator('34806106881147'), True)

    # Check that American Express number that is too long (16 digits) does not work
    # Category: Partition/Error Testing - isolating length
    def test_25(self):
        self.assertEqual(credit_card_validator('3480610688114239'), True)


if __name__ == '__main__':
    unittest.main()
