from typing import Dict
from typing import List
from typing import Union
from datetime import datetime
from treasury.session import FederalTreasurySession

# Used for type hinting
todays_date = datetime.today().date().isoformat()


class PublicDebtInstruments():

    """
    ## Overview:
    ----
    The Federal Treasury provided a wide range of data on
    public debt instruments. The `PublicDebtInstrument`
    object is used to query data on these instruments.
    """

    def __init__(self, session: FederalTreasurySession) -> None:
        """Initializes the `PublicDebtInstruments` object.

        ### Parameters
        ----
        session : `TreasurySession`
            An initialized session of the `TreasurySession`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
        """

        # Set the session.
        self.treasury_session: FederalTreasurySession = session

        # Set the endpoint.
        self.endpoint = '/series'
        self._todays_date = datetime.today().date().isoformat()

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.PublicDebtInstruments` object."""

        # define the string representation
        str_representation = '<FederalTreasuryClient.PublicDebtInstruments (active=True, connected=True)>'

        return str_representation

    def treasury_securities_outstanding(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries amounts outstanding for all securities.

        ### Overview
        ----
        A table that summarizes the amounts outstanding for all the
        securities issued by the Bureau of the Fiscal Service that makes
        up the Total Public Debt Outstanding amount.

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
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
            >>> debt_instruments_service.treasury_securities_outstanding()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/debt/mspd/mspd_table_1',
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

    def statutory_debt_limit(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries the Statuatory Debt Limit table.

        ### Overview
        ----
        A table that summarizes the amounts outstanding for the securities
        issued by the Bureau of the Fiscal Service adjusted for Unamortized
        Discount on Treasury Bills and Zero Coupon Treasury Bonds, Other
        Debt (old debt issued before 1917 and old currency called United
        States Notes), Debt held by the Federal Financing Bank and Guaranteed
        Debt of Government Agencies that makes up the Total Public Debt Subject
        to Limit amount.

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
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
            >>> debt_instruments_service.statutory_debt_limit()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/debt/mspd/mspd_table_2',
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

    def details_of_securities_outstanding(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries the details of Securities Outstanding table.

        ### Overview
        ----
        A table that shows details on marketable and non-marketable
        Treasury securities that are outstanding as of the last
        business day of the month.

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
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
            >>> debt_instruments_service.details_of_securities_outstanding()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/debt/mspd/mspd_table_3',
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

    def details_of_marketable_securities_outstanding(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries the Details of Marketables Securities Outstanding table.

        ### Overview
        ----
        A table that shows in detail by CUSIP, interest rate, the issue date,
        maturity date, interest payment dates and amounts outstanding for
        unmatured Bills, Notes, Bonds, Treasury Inflation-Protected Securities
        and Floating Rate Notes as of the last business day of the month.

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
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
            >>> debt_instruments_service.details_of_marketable_securities_outstanding()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/debt/mspd/mspd_table_3_market',
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

    def details_of_nonmarketable_securities_outstanding(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries the Details of Non-Marketables Securities Outstanding table.

        ### Overview
        ----
        A table that summarizes the monthly activity and current month amounts
        outstanding for Savings Bonds, Government Account Series, and State and
        Local Government Series securities where legal ownership cannot be
        transferred. These securities are outstanding as of the last business
        day of the month.

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
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
            >>> debt_instruments_service.details_of_nonmarketable_securities_outstanding()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/debt/mspd/mspd_table_3_nonmarket',
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

    def historical_data(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries the Historical Data table.

        ### Overview
        ----
        A table that shows the historical breakdown of the Debt
        Held by the Public, Intragovernmental Holdings and the
        Total Public Debt Outstanding.

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
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
            >>> debt_instruments_service.historical_data()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/debt/mspd/mspd_table_4',
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

    def holding_of_securities_stripped_form(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries the Holdings of Treasury Securities in
        Stripped Form.

        ### Overview
        ----
        A table that shows in detail by CUSIP, the interest rate, the STRIP
        CUSIP, maturity date, and amounts outstanding for securities held in
        unstripped form, stripped form and amount that have been reconstituted.
        STRIP stands for Separate Trading of Registered Interest and Principal
        of Securities. This is a security that has been stripped down into
        separate securities representing the principal and each interest payment.
        Each payment has its own identification number and can be traded
        individually. These securities are also known as zero-coupon bonds.

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
            >>> debt_instruments_service = treasury_client.public_debt_instruments()
            >>> debt_instruments_service.holding_of_securities_stripped_form()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/debt/mspd/mspd_table_5',
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
