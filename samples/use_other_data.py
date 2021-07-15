from pprint import pprint
from treasury.client import FederalTreasuryClient

# Initialize the client.
treasury_client = FederalTreasuryClient()

# Initialize the `OtherData` service.
other_data_service = treasury_client.other_data()

# Grab Average Interest Rates.
pprint(
    other_data_service.average_interest_rates()
)

# Grab Balance Sheets.
pprint(
    other_data_service.balance_sheets()
)

# Grab Debt to Penny.
pprint(
    other_data_service.debt_to_penny()
)

# Grab Gift Contributions.
pprint(
    other_data_service.gift_contributions()
)

# Grab Gold Reserve.
pprint(
    other_data_service.gold_reserve()
)

# Grab Historical Debt Outstanding.
pprint(
    other_data_service.historical_debt_outstanding()
)

# Grab Interest Cost Fund.
pprint(
    other_data_service.interest_cost_fund()
)

# Grab Interest Expense.
pprint(
    other_data_service.interest_expense()
)

# Grab Interest Uninvested.
pprint(
    other_data_service.interest_uninvested()
)

# Grab Qualified Tax.
pprint(
    other_data_service.qualified_tax()
)

# Grab Record Setting Auctions.
pprint(
    other_data_service.record_setting_auction()
)

# Grab Redemption Tables.
pprint(
    other_data_service.redemption_tables()
)

# Grab Saving Bond Values.
pprint(
    other_data_service.saving_bonds_value()
)

# Grab State and Local Government Statistics.
pprint(
    other_data_service.state_and_local_gov_statistics()
)

# Grab Statement Net Cost.
pprint(
    other_data_service.statement_net_cost()
)

# Grab Title XII Social Security.
pprint(
    other_data_service.title_seven_ssi()
)
