from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def _is_valid_account(self, account: int) -> bool:
        """Check if account number is valid (1-indexed)."""
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Validate both accounts
        if not (self._is_valid_account(account1) and self._is_valid_account(account2)):
            return False
        
        # Check if enough balance to transfer
        if self.balance[account1 - 1] < money:
            return False

        # Perform the transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Validate account
        if not self._is_valid_account(account):
            return False

        # Deposit money
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Validate account
        if not self._is_valid_account(account):
            return False

        # Check if enough balance
        if self.balance[account - 1] < money:
            return False

        # Withdraw money
        self.balance[account - 1] -= money
        return True
