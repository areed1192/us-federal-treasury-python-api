from pprint import pprint
from treasury.client import FederalTreasuryClient

# Initialize the client.
treasury_client = FederalTreasuryClient()

# Initialize the `PublicDebtInstruments` service.
debt_instruments_service = treasury_client.public_debt_instruments()

# Grab public debts outstanding.
pprint(
    debt_instruments_service.treasury_securities_outstanding()
)

# Grab Statutory Debt limit table.
pprint(
    debt_instruments_service.statutory_debt_limit()
)

# Grab Details of Securities Outstanding table.
pprint(
    debt_instruments_service.details_of_securities_outstanding()
)

# Grab Details of Marketable Securities Outstanding table.
pprint(
    debt_instruments_service.details_of_marketable_securities_outstanding()
)

# Grab Details of Non-Marketable Securities Outstanding table.
pprint(
    debt_instruments_service.details_of_nonmarketable_securities_outstanding()
)

# Grab Historical Data table.
pprint(
    debt_instruments_service.historical_data()
)

# Grab Holding of Treasury Securities in Stripped Form table.
pprint(
    debt_instruments_service.holding_of_securities_stripped_form()
)
