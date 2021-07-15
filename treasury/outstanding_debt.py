from typing import Dict
from typing import List
from treasury.session import FederalTreasurySession


class OutstandingDebtInstruments():

    """
    ## Overview:
    ----
    The Federal Treasury provided a wide range of data on
    outstanding debt instruments. The `OutstandingDebtInstruments`
    object is used to query data on these instruments.
    """

    def __init__(self, session: FederalTreasurySession) -> None:
        """Initializes the `OutstandingDebtInstruments` object.

        ### Parameters
        ----
        session : `TreasurySession`
            An initialized session of the `TreasurySession`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
        """

        # Set the session.
        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.OutstandingDebtInstruments` object."""

        # define the string representation
        str_representation = '<FederalTreasuryClient.OutstandingDebtInstruments (active=True, connected=True)>'

        return str_representation

    def rates_of_exchange(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Exchange rate of foreign currencies to the U.S.
        dollar for reporting.

        ### Overview
        ----
        Exchange rate of foreign currencies to the U.S. 
        for reporting.

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
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
            >>> outstanding_debt_instruments_service.rates_of_exchange()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/od/rates_of_exchange',
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

    def mature_unredeemed_debt(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Mature Unredeemed Debt table.

        ### Overview
        ----
        Savings bonds that have met their maturity date and have
        not been requested by the customer to be redeemed.

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
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
            >>> outstanding_debt_instruments_service.mature_unredeemed_debt()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/od/savings_bonds_mud',
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

    def piece_information_by_series(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Piece Information by Series table.

        ### Overview
        ----
        Total number of savings bonds by series issued, redeemed
        and outstanding as of the record_date.

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
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
            >>> outstanding_debt_instruments_service.piece_information_by_series()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/od/savings_bonds_pcs',
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

    def saving_bonds_report(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Paper Savings Bonds Issues, Redemptions, and
        Maturities by Series

        ### Overview
        ----
        For each series of Treasury savings bonds, this dataset
        details how many are issued and redeemed, the difference of
        these two values is how many are outstanding, which is also
        reported in the dataset. It does not contain any information
        on the values or yields of the Treasury savings bonds. Data
        in this report dates to the beginning of fiscal year 1999
        and is updated monthly.

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
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
            >>> outstanding_debt_instruments_service.saving_bonds_report()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/od/savings_bonds_report',
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

    def federal_debt_by_month(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Schedules of Federal Debt by Month.

        ### Overview
        ----
        This table represents monthly activity for the Federal Debt
        Managed by the Bureau of the Fiscal Service separated by Held
        by the Public and Intragovernmental Debt Holdings totaled by
        Principal, Accrued Interest Payable, and Net Unamortized
        Premiums/Discounts. All figures are rounded to the nearest
        million.

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
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
            >>> outstanding_debt_instruments_service.federal_debt_by_month()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/od/schedules_fed_debt',
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

    def federal_debt_fiscal_ytd(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Schedules of Federal Debt, Fiscal Year-to-Date.

        ### Overview
        ----
        This table represents fiscal year-to-date activity for the Federal
        Debt Managed by the Bureau of the Fiscal Service separated by Held
        by the Public and Intragovernmental Debt Holdings totaled by Principal,
        Accrued Interest Payable, and Net Unamortized Premiums/Discounts. All
        figures are rounded to the nearest million.

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
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
            >>> outstanding_debt_instruments_service.federal_debt_fiscal_ytd()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/od/schedules_fed_debt_fytd',
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

    def saving_bond_securities(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Savings Bonds Securities.

        ### Overview
        ----
        Statistics on sold, redeemed, outstanding, and interest rates
        of non-marketable savings bonds.

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
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
            >>> outstanding_debt_instruments_service.saving_bond_securities()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/od/slgs_savings_bonds',
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

    def state_and_local_gov_securities(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """State and Local Government Series Securities (Non-Marketable).

        ### Overview
        ----
        Recap of State and Local Government Series (SLGS) transaction
        and balance activity updated daily including subscriptions,
        cancellations, issues, outstanding, and redemptions of
        non-marketable SLGS securities.

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
            >>> outstanding_debt_instruments_service = treasury_client.outstanding_debt_instruments()
            >>> outstanding_debt_instruments_service.state_and_local_gov_securities()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/od/slgs_securities',
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
