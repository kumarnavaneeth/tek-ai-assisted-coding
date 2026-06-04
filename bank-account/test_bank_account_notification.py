import unittest
from unittest.mock import Mock

from bank_account_with_notification import BankAccount


class TestBankAccountWithNotification(unittest.TestCase):
    def test_deposit_triggers_notification_callback(self):
        notification = Mock()
        account = BankAccount(intial_balance=10, notification_callback=notification)

        account.deposit(25)

        self.assertEqual(account.get_balance(), 35)
        notification.assert_called_once_with(25, 35)

    def test_deposit_does_not_call_notification_on_failure(self):
        notification = Mock()
        account = BankAccount(intial_balance=10, notification_callback=notification)

        with self.assertRaises(ValueError):
            account.deposit(0)

        notification.assert_not_called()

    def test_deposit_works_without_notification_callback(self):
        account = BankAccount(intial_balance=5)

        account.deposit(15)

        self.assertEqual(account.get_balance(), 20)

    def test_notification_callback_receives_updated_balance(self):
        notification = Mock()
        account = BankAccount(intial_balance=50, notification_callback=notification)

        account.deposit(20)

        notification.assert_called_once()
        args, kwargs = notification.call_args
        self.assertEqual(args, (20, 70))
        self.assertEqual(kwargs, {})


if __name__ == "__main__":
    unittest.main()
