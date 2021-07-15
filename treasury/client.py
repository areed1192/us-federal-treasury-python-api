from treasury.session import FederalTreasurySession

from treasury.other_data import OtherData
from treasury.offest_program import OffsetProgram
from treasury.public_debt import PublicDebtInstruments
from treasury.revenue_and_payments import RevenueAndPayments
from treasury.outstanding_debt import OutstandingDebtInstruments
from treasury.daily_treasury_statements import DailyTreasuryStatements
from treasury.monthly_treasury_statement import MonthlyTreasuryStatements
from treasury.treasury_reports_on_receivables import TreasuryReportsOnReceivables


class FederalTreasuryClient():

    def __init__(self) -> None:
        """Initializes the `FederalTreasuryClient`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
        """

        self.treasury_session = FederalTreasurySession(client=self)

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient` object."""

        return '<FederalTreasuryClient (active=True, connected=True)>'

    def public_debt_instruments(self) -> PublicDebtInstruments:
        """Used to access the `PublicDebtInstruments` services.

        ### Returns
        ---
        PublicDebtInstruments:
            The `PublicDebtInstruments` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
        """

        # Grab the `PublicDebtInstruments` object.
        object = PublicDebtInstruments(session=self.treasury_session)

        return object

    def outstanding_debt_instruments(self) -> OutstandingDebtInstruments:
        """Used to access the `OutstandingDebtInstruments` services.

        ### Returns
        ---
        OutstandingDebtInstruments:
            The `OutstandingDebtInstruments` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
        """

        # Grab the `OutstandingDebtInstruments` object.
        object = OutstandingDebtInstruments(session=self.treasury_session)

        return object

    def daily_treasury_statements(self) -> DailyTreasuryStatements:
        """Used to access the `DailyTreasuryStatements` services.

        ### Returns
        ---
        DailyTreasuryStatements:
            The `DailyTreasuryStatements` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> daily_treasury_service = treasury_client.daily_treasury_service()
        """

        # Grab the `DailyTreasuryStatements` object.
        object = DailyTreasuryStatements(session=self.treasury_session)

        return object

    def monthly_treasury_statements(self) -> MonthlyTreasuryStatements:
        """Used to access the `MonthlyTreasuryStatements` services.

        ### Returns
        ---
        MonthlyTreasuryStatements:
            The `MonthlyTreasuryStatements` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statements()
        """

        # Grab the `MonthlyTreasuryStatements` object.
        object = MonthlyTreasuryStatements(session=self.treasury_session)

        return object

    def treasury_reports_on_receivables(self) -> TreasuryReportsOnReceivables:
        """Used to access the `TreasuryReportsOnReceivables` services.

        ### Returns
        ---
        TreasuryReportsOnReceivables:
            The `TreasuryReportsOnReceivables` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> treasury_reports_service = treasury_client.treasury_reports_on_receivables()
        """

        # Grab the `TreasuryReportsOnReceivables` object.
        object = TreasuryReportsOnReceivables(session=self.treasury_session)

        return object

    def other_data(self) -> OtherData:
        """Used to access the `OtherData` services.

        ### Returns
        ---
        OtherData:
            The `OtherData` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> other_data_service = treasury_client.other_data()
        """

        # Grab the `OtherData` object.
        object = OtherData(session=self.treasury_session)

        return object

    def revenue_and_payments(self) -> RevenueAndPayments:
        """Used to access the `RevenueAndPayments` services.

        ### Returns
        ---
        RevenueAndPayments:
            The `RevenueAndPayments` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> revenue_and_payment_service = treasury_client.revenue_and_payments()
        """

        # Grab the `RevenueAndPayments` object.
        object = RevenueAndPayments(session=self.treasury_session)

        return object

    def offset_program(self) -> OffsetProgram:
        """Used to access the `OffsetProgram` services.

        ### Returns
        ---
        OffsetProgram:
            The `OffsetProgram` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> offset_program_service = treasury_client.offset_program()
        """

        # Grab the `OffsetProgram` object.
        object = OffsetProgram(session=self.treasury_session)

        return object
