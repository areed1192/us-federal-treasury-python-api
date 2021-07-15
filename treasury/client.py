from treasury.session import FederalTreasurySession
from treasury.public_debt import PublicDebtInstruments
from treasury.outstanding_debt import OutstandingDebtInstruments


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
        Users:
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
        Users:
            The `OutstandingDebtInstruments` services Object.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
        """

        # Grab the `OutstandingDebtInstruments` object.
        object = OutstandingDebtInstruments(session=self.treasury_session)

        return object
