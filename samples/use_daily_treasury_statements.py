from pprint import pprint
from treasury.client import FederalTreasuryClient

# Initialize the client.
treasury_client = FederalTreasuryClient()

# Initialize the `DailyTreasuryStatements` service.
daily_treasury_service = treasury_client.daily_treasury_statements()

# Grab Public Debt Transactions.
pprint(
    daily_treasury_service.public_debt_transactions()
)

# Grab Adjusted Public Debt Transactions.
pprint(
    daily_treasury_service.adjusted_public_debt_transactions()
)

# Grab Debt Subject Limit.
pprint(
    daily_treasury_service.debt_subject_limit()
)

# Grab Deposits & Withdrawals for Operating Cash.
pprint(
    daily_treasury_service.deposits_and_withdrawals_operating_cash()
)

# Grab Federal Tax Deposits.
pprint(
    daily_treasury_service.federal_tax_deposits()
)

# Grab Federal Income Tax Refunds Issued.
pprint(
    daily_treasury_service.income_tax_refunds_issued()
)

# Grab Operating Cash Balance.
pprint(
    daily_treasury_service.operating_cash_balance()
)

# Grab Short Term Cash Investments.
pprint(
    daily_treasury_service.short_term_cash_investments()
)
