from pprint import pprint
from treasury.client import FederalTreasuryClient

# Initialize the client.
treasury_client = FederalTreasuryClient()

# Initialize the `MonthlyTreasuryStatements` service.
monthly_treasury_service = treasury_client.monthly_treasury_statements()

# Grab Analysis Change in Liabilities.
pprint(
    monthly_treasury_service.analysis_change_in_liabilities()
)

# Grab Borrowing and Finance.
pprint(
    monthly_treasury_service.borrowing_financed_treasury_securities()
)

# Grab Budgets and Financing.
pprint(
    monthly_treasury_service.budgets_and_financing()
)

# Grab Direct Loan Financing.
pprint(
    monthly_treasury_service.direct_loan_financing()
)

# Grab Investment Federal Securities.
pprint(
    monthly_treasury_service.investments_federal_securities()
)

# Grab Mean of Financing.
pprint(
    monthly_treasury_service.means_of_financing()
)

# Grab Outlays.
pprint(
    monthly_treasury_service.outlays()
)

# Grab Receipts.
pprint(
    monthly_treasury_service.receipts()
)

# Grab Receipts & Outlays.
pprint(
    monthly_treasury_service.receipts_and_outlays()
)

# Grab Receipts & Outlays by Month.
pprint(
    monthly_treasury_service.receipts_and_outlays_by_month()
)

# Grab Receipts by Source and Outlays by Function.
pprint(
    monthly_treasury_service.receipts_by_source_outlay_by_function()
)

# Grab Borrowing Financed by Treasury Securities.
pprint(
    monthly_treasury_service.borrowing_financed_treasury_securities()
)

# Grab Securities Issued for Special Financing.
pprint(
    monthly_treasury_service.securities_issued_special_financing()
)
