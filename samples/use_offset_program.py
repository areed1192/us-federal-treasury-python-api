from pprint import pprint
from treasury.client import FederalTreasuryClient

# Initialize the client.
treasury_client = FederalTreasuryClient()

# Initialize the `OffsetProgram` service.
offset_program_service = treasury_client.offset_program()

# Grab Federal Collections.
pprint(
    offset_program_service.federal_collections()
)

# Grab State Programs Collections.
pprint(
    offset_program_service.state_programs()
)
