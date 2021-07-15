# United States Federal Treasury API

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Support These Projects](#support-these-projects)

## Overview

Version: **0.1.0**

The U.S. Department of the Treasury is building a suite of open-source tools to deliver
standardized information about federal finances to the public. We are working to centralize
publicly available financial data, and this website will include datasets from the Fiscal
Service on topics including debt, revenue, spending, interest rates, and savings bonds.

Our API is based on Representational State Transfer, otherwise known as a RESTful API.
Our API accepts GET requests, returns JSON responses, and uses standard HTTP response
codes. Each endpoint on this site is accessible through unique URLs that respond with
data values and metadata from a single database table.

## Setup

**Setup - Requirements Install:**

For this particular project, you only need to install the dependencies, to use the project. The dependencies
are listed in the `requirements.txt` file and can be installed by running the following command:

```console
pip install -r requirements.txt
```

After running that command, the dependencies should be installed.

**Setup - Local Install:**

If you are planning to make modifications to this project or you would like to access it
before it has been indexed on `PyPi`. I would recommend you either install this project
in `editable` mode or do a `local install`. For those of you, who want to make modifications
to this project. I would recommend you install the library in `editable` mode.

If you want to install the library in `editable` mode, make sure to run the `setup.py`
file, so you can install any dependencies you may need. To run the `setup.py` file,
run the following command in your terminal.

```console
pip install -e .
```

If you don't plan to make any modifications to the project but still want to use it across
your different projects, then do a local install.

```console
pip install .
```

This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.

**Setup - PyPi Install:**

To **install** the library, run the following command from the terminal.

```console
pip install us-federal-treasury-python-api
```

**Setup - PyPi Upgrade:**

To **upgrade** the library, run the following command from the terminal.

```console
pip install --upgrade us-federal-treasury-python-api
```

## Usage

Here is a simple example of using the `treasury` library.

```python
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
```

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding). I'm
always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require me to
pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).
