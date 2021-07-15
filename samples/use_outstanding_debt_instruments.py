from pprint import pprint
from treasury.client import FederalTreasuryClient

# Initialize the client.
treasury_client = FederalTreasuryClient()

# Initialize the `OutstandingDebtInstruments` service.
outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()

# Grab Rates of Exchange.
pprint(
    outstanding_debt_instruments_service.rates_of_exchange()
)

# Grab Federal Debt by Month.
pprint(
    outstanding_debt_instruments_service.federal_debt_by_month()
)

# Grab Federal Debt by Fiscal Year To Date.
pprint(
    outstanding_debt_instruments_service.federal_debt_fiscal_ytd()
)

# Grab Mature Unredeemed Debt.
pprint(
    outstanding_debt_instruments_service.mature_unredeemed_debt()
)

# Grab Piece Information by Series.
pprint(
    outstanding_debt_instruments_service.piece_information_by_series()
)

# Grab Saving Bonds Securities.
pprint(
    outstanding_debt_instruments_service.saving_bond_securities()
)

# Grab Saving Bonds Reports.
pprint(
    outstanding_debt_instruments_service.saving_bonds_report()
)

# Grab State & Local Government Securities.
pprint(
    outstanding_debt_instruments_service.state_and_local_gov_securities()
)
