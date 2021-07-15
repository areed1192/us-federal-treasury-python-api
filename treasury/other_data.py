from typing import Dict
from typing import List
from treasury.session import FederalTreasurySession


class OtherData():

    """
    ## Overview:
    ----
    This service contains miscellaneous other data sets that
    contain financial information and different program debt
    obligations.
    """

    def __init__(self, session: FederalTreasurySession) -> None:
        """Initializes the `OtherData` object.

        ### Parameters
        ----
        session : `TreasurySession`
            An initialized session of the `TreasurySession`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> other_data_service = treasury_client.other_data()
        """

        # Set the session.
        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.OtherData` object."""

        # define the string representation
        str_representation = '<FederalTreasuryClient.OtherData (active=True, connected=True)>'

        return str_representation

    def average_interest_rates(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Average Interest Rates on U.S. Treasury Securities.

        ### Overview
        ----
        Average interest rates for marketable and non-marketable securities.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.average_interest_rates()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/avg_interest_rates',
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

    def balance_sheets(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Financial Report of the U.S. Government: Balance Sheets.

        ### Overview
        ----
        Overview of the U.S. government's financial position with a summary of
        assets, liabilities, and net position.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.balance_sheets()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/balance_sheets',
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

    def historical_debt_outstanding(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Historical Debt Outstanding.

        ### Overview
        ----
        U.S. debt outstanding at the end of each fiscal year.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.historical_debt_outstanding()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/debt_outstanding',
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

    def debt_to_penny(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Debt to the Penny.

        ### Overview
        ----
        Outstanding U.S. debt on a daily basis.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.debt_to_penny()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/debt_to_penny',
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

    def gift_contributions(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Gift Contributions to Reduce Debt Held by the Public.

        ### Overview
        ----
        Summary of gifts donated to the United States Government to reduce
        debt held by the public.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.gift_contributions()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/gift_contributions',
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

    def gold_reserve(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """U.S. Treasury-Owned Gold.

        ### Overview
        ----
        The amount of gold the U.S. Treasury holds in both weight
        and value.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.gold_reserve()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/gold_reserve',
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

    def interest_cost_fund(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Federal Investments Program: Interest Cost by Fund.

        ### Overview
        ----
        A monthly summary report containing premiums, discounts, 
        interest collected, interest payments, and inflation compensation
        for all accounts invested in Government Account Series (GAS)
        Securities, as well as premium and discount amortization for accounts
        invested in zero-coupon bonds (ZCBs).

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.interest_cost_fund()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/interest_cost_fund',
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

    def interest_expense(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Interest Expense on the Debt Outstanding.

        ### Overview
        ----
        The Interest Expense on the Debt Outstanding is a monthly summary
        of the cost of interest on U.S. debt, including U.S. Treasury notes
        and bonds, foreign and domestic series certificates of indebtedness,
        notes and bonds, savings bonds, State and Local Government series
        (SLGS) and other special purpose securities.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.interest_expense()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/interest_expense',
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

    def interest_uninvested(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Federal Borrowings Program: Interest on Uninvested Funds.

        ### Overview
        ----
        A quarterly report containing interest balances associated with Treasury's
        Credit Reform: Interest Paid on Uninvested Funds account.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.interest_uninvested()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/interest_uninvested',
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

    def qualified_tax(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Historical Qualified Tax Credit Bond Interest Rates.

        ### Overview
        ----
        Historical interest rate, term to maturity, and permitted sinking fund
        yield for qualified tax credit bonds reported daily through January
        30, 2018.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.qualified_tax()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/qualified_tax',
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

    def record_setting_auction(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Record-Setting Auction.

        ### Overview
        ----
        Rates, yields, offering, and auction dates of record high and low Treasury
        Bills, Notes, Bonds, Treasury Inflation-Protected Securities, Floating Rate
        Notes and Cash Management Bills.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.record_setting_auction()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/record_setting_auction',
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

    def redemption_tables(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Redemption Tables.

        ### Overview
        ----
        The Redemption Tables dataset contains monthly tables that list the
        redemption value, interest earned, and yield of accrual savings bonds
        purchased since 1941. Each monthly report lists the redemption value of
        all bonds at the time of publication. Investors and bond owners can use
        this dataset as an easy and understandable reference to know the 
        value of the bonds they hold.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.redemption_tables()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/redemption_tables',
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

    def saving_bonds_value(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Savings Bonds Value Files.

        ### Overview
        ----
        The Savings Bond Value Files dataset is used by developers of bond
        pricing programs to update their systems with new redemption values
        for accrual savings bonds (Series E, EE, I & Savings Notes). The core
        data is the same as the Redemption Tables but there are differences in
        format, amount of data, and date range. The Savings Bonds Value Files
        dataset is meant for programmers and developers to read in redemption
        values without having to first convert PDFs.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.saving_bonds_value()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/sb_value',
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

    def state_and_local_gov_statistics(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Monthly State and Local Government Series (SLGS) Securities
        Program Statistics.

        ### Overview
        ----
        This table shows what states and territories are borrowing from the
        federal Unemployment Trust Fund in order to pay out unemployment
        benefits.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.state_and_local_gov_statistics()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/slgs_statistics',
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

    def statement_net_cost(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Financial Report of the U.S. Government: Statement of Net Cost.

        ### Overview
        ----
        The Financial Report of the U.S. Government: Statement of Net Cost dataset
        presents the net cost of the government operations, including the operations
        related to funds from dedicated collections. Costs and earned revenues are
        categorized on the Statement of Net Cost by significant entity, providing
        greater accountability by showing the relationship of the entities' net cost
        to the government-wide net cost. Net cost is computed by subtracting earned
        revenue from gross cost, adjusted by the total gain or loss from changes in
        assumptions.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.statement_net_cost()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/statement_net_cost',
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

    def title_seven_ssi(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Advances to State Unemployment Funds (Social Security Act Title XII).

        ### Overview
        ----
        Monthly balances for securities outstanding and principal outstanding for
        State and Local Government Series (SLGS) securities.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.title_seven_ssi()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/title_xii',
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

    def utf_qtr_yields(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Unemployment Trust Fund: Quarterly Yields.

        ### Overview
        ----
        Current and historical yields earned each quarter from Unemployment
        Trust Funds from 1999 to the present.

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
            >>> other_data_service = treasury_client.other_data()
            >>> other_data_service.utf_qtr_yields()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/accounting/od/utf_qtr_yields',
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
