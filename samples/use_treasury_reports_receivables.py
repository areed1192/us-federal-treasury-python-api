from pprint import pprint
from treasury.client import FederalTreasuryClient

# Initialize the client.
treasury_client = FederalTreasuryClient()

# Initialize the `TreasuryReportsOnReceivables` service.
treasury_reports_service = treasury_client.treasury_reports_on_receivables()

# Grab Collected & Outstanding Receivables.
pprint(
    treasury_reports_service.collected_and_outstanding_receivables()
)

# Grab Written Off & Delinquent Debt.
pprint(
    treasury_reports_service.written_off_delinquent_debt()
)

# Grab Collections & Delinquent Debt.
pprint(
    treasury_reports_service.collections_delinquent_debt()
)

# Grab Data Act Compliance.
pprint(
    treasury_reports_service.data_act_compliance()
)

# Grab Delinquent Debt.
pprint(
    treasury_reports_service.delinquent_debt()
)

# Grab Full Data.
pprint(
    treasury_reports_service.full_data()
)
