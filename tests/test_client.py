import unittest

from unittest import TestCase
from treasury.client import FederalTreasuryClient
from treasury.public_debt import PublicDebtInstruments
from treasury.session import FederalTreasurySession
from treasury.outstanding_debt import OutstandingDebtInstruments
from treasury.daily_treasury_statements import DailyTreasuryStatements


class FederalTreasuryTest(TestCase):

    """Will perform a unit test for the `FederalTreasuryClient`."""

    def setUp(self) -> None:
        """Set up the `FederalTreasuryClient` Client."""

        self.client = FederalTreasuryClient()

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `FederalTreasuryClient`."""

        self.assertIsInstance(
            self.client,
            FederalTreasuryClient
        )

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `FederalTreasurySession`."""

        self.assertIsInstance(
            self.client.treasury_session,
            FederalTreasurySession
        )

    def test_creates_instance_of_public_debt(self):
        """Create an instance and make sure it's a `PublicDebtInstruments`."""

        self.assertIsInstance(
            self.client.public_debt_instruments(),
            PublicDebtInstruments
        )

    def test_creates_instance_of_outstanding_debt(self):
        """Create an instance and make sure it's a `OutstandingDebtInstruments`."""

        self.assertIsInstance(
            self.client.outstanding_debt_instruments(),
            OutstandingDebtInstruments
        )

    def test_creates_instance_of_daily_treasury_statements(self):
        """Create an instance and make sure it's a `DailyTreasuryStatements`."""

        self.assertIsInstance(
            self.client.daily_treasury_statements(),
            DailyTreasuryStatements
        )

    def tearDown(self) -> None:
        """Teardown the `FederalTreasuryClient` Client."""

        del self.client


if __name__ == '__main__':
    unittest.main()
