from pprint import pprint
from treasury.client import FederalTreasuryClient

# Initialize the client.
treasury_client = FederalTreasuryClient()

# Initialize the `RevenueAndPayments` service.
revenue_and_payments_service = treasury_client.revenue_and_payments()

# Grab Judgement Fund for Congress.
pprint(
    revenue_and_payments_service.judgement_fund_congress()
)

# Grab Revenue Collections data.
pprint(
    revenue_and_payments_service.revenue_collection()
)
