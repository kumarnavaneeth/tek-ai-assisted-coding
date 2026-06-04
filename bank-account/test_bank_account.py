import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_initial_balance_defaults_to_zero(self):
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)

    def test_initial_balance_can_be_positive(self):
        account = BankAccount(initial_balance=100)
        self.assertEqual(account.get_balance(), 100)

    def test_initial_balance_negative_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            BankAccount(initial_balance=-1)
        self.assertIn("Initial balance cannot be negative", str(context.exception))

    def test_deposit_increases_balance(self):
        account = BankAccount(initial_balance=50)
        account.deposit(30)
        self.assertEqual(account.get_balance(), 80)

    def test_deposit_with_zero_amount_raises_value_error(self):
        account = BankAccount(initial_balance=20)
        with self.assertRaises(ValueError) as context:
            account.deposit(0)
        self.assertIn("Deposit amount must be positive", str(context.exception))
        self.assertEqual(account.get_balance(), 20)

    def test_deposit_with_negative_amount_raises_value_error(self):
        account = BankAccount(initial_balance=20)
        with self.assertRaises(ValueError) as context:
            account.deposit(-10)
        self.assertIn("Deposit amount must be positive", str(context.exception))
        self.assertEqual(account.get_balance(), 20)

    def test_withdraw_reduces_balance(self):
        account = BankAccount(initial_balance=100)
        account.withdraw(40)
        self.assertEqual(account.get_balance(), 60)

    def test_withdraw_entire_balance_sets_zero(self):
        account = BankAccount(initial_balance=75)
        account.withdraw(75)
        self.assertEqual(account.get_balance(), 0)

    def test_withdraw_with_zero_amount_raises_value_error(self):
        account = BankAccount(initial_balance=50)
        with self.assertRaises(ValueError) as context:
            account.withdraw(0)
        self.assertIn("Withdrawal amount must be positive", str(context.exception))
        self.assertEqual(account.get_balance(), 50)

    def test_withdraw_with_negative_amount_raises_value_error(self):
        account = BankAccount(initial_balance=50)
        with self.assertRaises(ValueError) as context:
            account.withdraw(-5)
        self.assertIn("Withdrawal amount must be positive", str(context.exception))
        self.assertEqual(account.get_balance(), 50)

    def test_withdraw_more_than_balance_raises_value_error(self):
        account = BankAccount(initial_balance=30)
        with self.assertRaises(ValueError) as context:
            account.withdraw(31)
        self.assertIn("Cannot withdraw more than the current balance", str(context.exception))
        self.assertEqual(account.get_balance(), 30)

    def test_multiple_transactions_produce_expected_balance(self):
        account = BankAccount(initial_balance=200)
        account.deposit(50)
        account.withdraw(75)
        account.deposit(25)
        self.assertEqual(account.get_balance(), 200)

    def test_float_amounts_are_supported(self):
        account = BankAccount(initial_balance=10.50)
        account.deposit(5.25)
        account.withdraw(3.75)
        self.assertAlmostEqual(account.get_balance(), 12.0)

    def test_non_numeric_initial_balance_raises_type_error(self):
        with self.assertRaises(TypeError):
            BankAccount(initial_balance="100")

    def test_non_numeric_deposit_raises_type_error(self):
        account = BankAccount(initial_balance=10)
        with self.assertRaises(TypeError):
            account.deposit("20")
        self.assertEqual(account.get_balance(), 10)

    def test_non_numeric_withdraw_raises_type_error(self):
        account = BankAccount(initial_balance=10)
        with self.assertRaises(TypeError):
            account.withdraw("5")
        self.assertEqual(account.get_balance(), 10)


if __name__ == "__main__":
    unittest.main()
