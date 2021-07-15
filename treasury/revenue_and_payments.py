from typing import Dict
from typing import List
from treasury.session import FederalTreasurySession


class RevenueAndPayments():

    """
    ## Overview:
    ----

    Revenue:

    Daily overview of federal revenue collections such as income tax
    deposits, customs duties, fees for government service, fines, and
    loan repayments.

    Payments:

    Listing of payments made through the Judgment Fund including the
    amount paid out, judgment type, legal representatives, agency,
    and associated costs.
    """

    def __init__(self, session: FederalTreasurySession) -> None:
        """Initializes the `RevenueAndPayments` object.

        ### Parameters
        ----
        session : `TreasurySession`
            An initialized session of the `TreasurySession`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> revenue_and_payments_service = treasury_client.revenue_and_payments()
        """

        # Set the session.
        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.RevenueAndPayments` object."""

        # define the string representation
        str_representation = '<FederalTreasuryClient.RevenueAndPayments (active=True, connected=True)>'

        return str_representation

    def judgement_fund_congress(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Judgment Fund: Annual Report to Congress.

        ### Overview
        ----
        This table provides a listing of payments made through the Judgment
        Fund including the amount paid out, judgment type, legal representatives,
        agencies involved, and associated costs.

        ### Parameters
        ----
        fields : List[str] (optional, Default=None)        
            The fields parameter allows you to select which field(s) should be
            included in the response. If desired fields are not specified, all
            fields will be returned.

        sort : List[str] (optional, Default=None)        
            The sort parameter allows a user to sort a field in ascending (least
            to greatest) or descending (greatest to least) order. When no sort parameter
            is specified, the default is to sort by the first column listed. Most API
            endpoints are thus sorted by date in ascending order (historical to most
            current).

        filters : List[str] (optional, Default=None)        
            Filters are used to view a subset of the data based on specific
            criteria. For example, you may want to find data that falls within
            a certain date range, or only show records which contain a value
            larger than a certain threshold. When no filters are provided,
            the default response will return all fields and all data.

        page_number : int (optional, Default=1)
            The page number will set the index for the pagination, starting
            at 1. This allows the user to paginate through the records
            returned from an API request

        page_size : int (optional, Default=100)
            The page size will set the number of rows that are returned
            on a request.

        ### Returns
        ----
        Dict
            A collection of `Records` resources.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> revenue_and_payments_service = treasury_client.revenue_and_payments()
            >>> revenue_and_payments_service.judgement_fund_congress()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/payments/jfics/jfics_congress_report',
            params={
                'format': 'json',
                'page[number]': page_number,
                'page[size]': page_size,
                'fields': fields,
                'sort': sort,
                'filters': filters
            }
        )

        return content

    def revenue_collection(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """U.S. Government Revenue Collections.

        ### Overview
        ----
        A daily overview of federal revenue collections such as individual
        and corporate income tax deposits, customs duties, fees for government
        service, fines, and loan repayments. These collections can be made through
        either electronic or non-electronic transactions by mail, internet, bank,
        or over-the-counter (OTC) channels.

        ### Parameters
        ----
        fields : List[str] (optional, Default=None)        
            The fields parameter allows you to select which field(s) should be
            included in the response. If desired fields are not specified, all
            fields will be returned.

        sort : List[str] (optional, Default=None)        
            The sort parameter allows a user to sort a field in ascending (least
            to greatest) or descending (greatest to least) order. When no sort parameter
            is specified, the default is to sort by the first column listed. Most API
            endpoints are thus sorted by date in ascending order (historical to most
            current).

        filters : List[str] (optional, Default=None)        
            Filters are used to view a subset of the data based on specific
            criteria. For example, you may want to find data that falls within
            a certain date range, or only show records which contain a value
            larger than a certain threshold. When no filters are provided,
            the default response will return all fields and all data.

        page_number : int (optional, Default=1)
            The page number will set the index for the pagination, starting
            at 1. This allows the user to paginate through the records
            returned from an API request

        page_size : int (optional, Default=100)
            The page size will set the number of rows that are returned
            on a request.

        ### Returns
        ----
        Dict
            A collection of `Records` resources.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> revenue_and_payments_service = treasury_client.revenue_and_payments()
            >>> revenue_and_payments_service.revenue_collection()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/revenue/rcm',
            params={
                'format': 'json',
                'page[number]': page_number,
                'page[size]': page_size,
                'fields': fields,
                'sort': sort,
                'filters': filters
            }
        )

        return content
