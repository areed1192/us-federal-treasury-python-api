import unittest

from unittest import TestCase
from treasury.other_data import OtherData
from treasury.client import FederalTreasuryClient
from treasury.session import FederalTreasurySession
from treasury.public_debt import PublicDebtInstruments
from treasury.outstanding_debt import OutstandingDebtInstruments
from treasury.daily_treasury_statements import DailyTreasuryStatements
from treasury.monthly_treasury_statement import MonthlyTreasuryStatements
from treasury.treasury_reports_on_receivables import TreasuryReportsOnReceivables


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

    def test_creates_instance_of_monthly_treasury_statements(self):
        """Create an instance and make sure it's a `MonthlyTreasuryStatements`."""

        self.assertIsInstance(
            self.client.monthly_treasury_statements(),
            MonthlyTreasuryStatements
        )

    def test_creates_instance_of_treasury_reports_receivables(self):
        """Create an instance and make sure it's a `TreasuryReportsOnReceivables`."""

        self.assertIsInstance(
            self.client.treasury_reports_on_receivables(),
            TreasuryReportsOnReceivables
        )

    def test_creates_instance_of_other_data(self):
        """Create an instance and make sure it's a `OtherData`."""

        self.assertIsInstance(
            self.client.other_data(),
            OtherData
        )

    def tearDown(self) -> None:
        """Teardown the `FederalTreasuryClient` Client."""

        del self.client


if __name__ == '__main__':
    unittest.main()
