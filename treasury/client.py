
from typing import List
from typing import Dict
from typing import Union

from treasury.session import TreasurySession


class FederalTreasuryClient():

    def __init__(self) -> None:
        """Initializes the `FederalTreasuryClient`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
        """

        self.treasury_session = TreasurySession(client=self)

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient` object."""

        return '<FederalTreasuryClient (active=True, connected=True)>'
