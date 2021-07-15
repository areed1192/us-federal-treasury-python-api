from typing import Dict
from typing import List
from treasury.session import FederalTreasurySession


class MonthlyTreasuryStatements():

    """
    ## Overview:
    ----
    The Monthly Treasury Statement (MTS) dataset provides information on
    the flow of money into and out of the U.S. Department of the Treasury.
    It includes how deficits are funded, such as borrowing from the public
    or reducing operating cash, and how surpluses are distributed. Further
    tables categorize spending (outlays) by department and agency, revenue
    (receipts) by specific taxes or other government sources of income, and
    transactions with trust funds such as Social Security or Medicare. All
    values are reported in millions of U.S. dollars.
    """

    def __init__(self, session: FederalTreasurySession) -> None:
        """Initializes the `MonthlyTreasuryStatements` object.

        ### Parameters
        ----
        session : `TreasurySession`
            An initialized session of the `TreasurySession`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
        """

        # Set the session.
        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.MonthlyTreasuryStatements` object."""

        # define the string representation
        str_representation = '<FederalTreasuryClient.MonthlyTreasuryStatements (active=True, connected=True)>'

        return str_representation

    def receipts_outlays_and_deficits(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Summary of Receipts, Outlays, and the Deficit/Surplus of
        the U.S. Government.

        ### Overview
        ----
        This summary table shows the total amount of receipts and outlays and the
        amount of the budget surplus/deficit by month for the current and prior fiscal
        years. This table includes total and subtotal rows that should be excluded
        when aggregating data. Some rows represent elements of the dataset's hierarchy,
        but are not assigned values. The classification_id for each of these elements
        can be used as the parent_id for underlying data elements to calculate their
        implied values. Subtotal rows are available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.receipts_outlays_and_deficits()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_1',
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

    def budgets_and_financing(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Summary of Budget and Off-Budget Results and Financing
        of the U.S. Government.

        ### Overview
        ----
        This summary table shows the on-budget and off-budget receipts and outlays, the
        on-budget and off-budget surplus/deficit, and the means of financing the budget
        surplus/deficit. The table also shows the budgeted amounts estimated in the President's
        Budget for the current fiscal year and next fiscal year for each item on the table.
        This table includes total and subtotal rows that should be excluded when aggregating
        data. Some rows represent elements of the dataset's hierarchy, but are not assigned
        values. The classification_id for each of these elements can be used as the parent_id
        for underlying data elements to calculate their implied values. Subtotal rows are
        available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.budgets_and_financing()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_2',
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

    def receipts_and_outlays(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Summary of Receipts and Outlays of the U.S. Government.

        ### Overview
        ----
        This summary table shows, for Budget Receipts, the total amount of activity
        for the current month, the current fiscal year-to-date, the comparable prior
        period year-to-date and the budgeted amount estimated for the current fiscal
        year for various types of receipts (i.e. individual income tax, corporate income
        tax, etc.). The Budget Outlays section of the table shows the total amount of
        activity for the current month, the current fiscal year-to-date, the comparable
        prior period year-to-date and the budgeted amount estimated for the current fiscal
        year for agencies of the federal government. The table also shows the amounts for
        the budget/surplus deficit categorized as listed above. This table includes total
        and subtotal rows that should be excluded when aggregating data. Some rows represent
        elements of the dataset's hierarchy, but are not assigned values. The 
        classification_id for each of these elements can be used as the parent_id for underlying
        data elements to calculate their implied values. Subtotal rows are available to access
        this same information.


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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.receipts_and_outlays()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_3',
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

    def receipts(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Receipts of the U.S. Government.

        ### Overview
        ----
        This table shows the gross receipts, refunds and net receipts for the current month,
        the current fiscal year-to-date and the prior fiscal year-to-date for the various
        receipts of the federal government. This table includes total and subtotal rows
        that should be excluded when aggregating data. Some rows represent elements of the
        dataset's hierarchy, but are not assigned values. The classification_id for each of
        these elements can be used as the parent_id for underlying data elements to calculate
        their implied values. Subtotal rows are available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.receipts()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_4',
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

    def outlays(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Outlays of the U.S. Government.

        ### Overview
        ----
        This table shows the gross outlays, applicable receipts and net outlays
        for the current month, current fiscal year-to-date and prior fiscal
        year-to-date by various agency programs accounted for in the budget of the
        federal government. This table includes total and subtotal rows that should
        be excluded when aggregating data. Some rows represent elements of the 
        dataset's hierarchy, but are not assigned values. The classification_id for
        each of these elements can be used as the parent_id for underlying data elements
        to calculate their implied values. Subtotal rows are available to access
        this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.outlays()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_5',
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

    def means_of_financing(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Means of Financing the Deficit or Disposition of
        Surplus by the U.S. Government.

        ### Overview
        ----
        This table shows the net transactions for the current month, and the current
        and prior fiscal year-to-date, as well as account balances for the beginning
        of the current fiscal year and current accounting month and the close of the
        current accounting month. This activity is related to the means used to finance
        the budget deficit or to dispose of a budget surplus. An asset account would
        represent an asset to the United States Government, for example United States
        Treasury Operating Cash. A liability account would represent a liability to
        the United States Government, for example Borrowing from the Public. This table
        includes total and subtotal rows that should be excluded when aggregating data.
        Some rows represent elements of the dataset's hierarchy, but are not assigned
        values. The classification_id for each of these elements can be used as the 
        parent_id for underlying data elements to calculate their implied values. 
        Subtotal rows are available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.means_of_financing()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_6',
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

    def analysis_change_in_liabilities(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Analysis of Change in Excess of Liabilities of
        the U.S. Government.

        ### Overview
        ----
        This table is a subsidiary table for Means of Financing the Deficit or
        Disposition of Surplus by the U.S. Government providing a detailed view
        of the Change in Excess of Liabilities. This table includes total and subtotal
        rows that should be excluded when aggregating data. Some rows represent
        elements of the dataset's hierarchy, but are not assigned values. The
        classification_id for each of these elements can be used as the parent_id for
        underlying data elements to calculate their implied values. Subtotal rows are
        available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.analysis_change_in_liabilities()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_6a',
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

    def securities_issued_special_financing(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Securities Issued by Federal Agencies Under Special
        Financing Authorities.

        ### Overview
        ----
        This table is a subsidiary table for Means of Financing the Deficit or
        Disposition of Surplus by the U.S. Government providing a detailed view
        of the transactions labelled, Agency Securities, Issued Under Special
        Financing Authorities. Special financing authorities include financing that
        is established by legislation under special or unique circumstances and for
        a specific purpose. This table includes total and subtotal rows that should
        be excluded when aggregating data. Some rows represent elements of the dataset's
        hierarchy, but are not assigned values. The classification_id for each of these
        elements can be used as the parent_id for underlying data elements to calculate
        their implied values. Subtotal rows are available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.securities_issued_special_financing()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_6b',
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

    def borrowing_financed_treasury_securities(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Federal Agency Borrowing Financed Through the Issue
        of Treasury Securities.

        ### Overview
        ----
        This table is a subsidiary table for Means of Financing the Deficit or Disposition
        of Surplus by the U.S. Government, providing a detailed view of transactions and
        account balances for agency programs that borrow from the United States Treasury
        or from the Federal Financing Bank. This table includes total and subtotal rows
        that should be excluded when aggregating data. Some rows represent elements of the
        dataset's hierarchy, but are not assigned values. The classification_id for each of
        these elements can be used as the parent_id for underlying data elements to calculate
        their implied values. Subtotal rows are available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.borrowing_financed_treasury_securities()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_6c',
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

    def investments_federal_securities(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Investments of Federal Government Accounts in Federal
        Securities.

        ### Overview
        ----
        This table is a subsidiary table for Means of Financing the Deficit or Disposition
        of Surplus by the U.S. Government providing a detailed view of federal funds and
        trust funds that are invested in Government Account Series (GAS) securities. Federal
        funds include general funds, special funds, and revolving funds (public enterprise
        revolving funds, intragovernmental revolving funds, and credit financing accounts).
        A trust fund is a type of account, designated by law, for receipts or offsetting
        receipts dedicated to specific purposes and the expenditure of these receipts.
        This table includes total and subtotal rows that should be excluded when aggregating
        data. Some rows represent elements of the dataset's hierarchy, but are not assigned 
        values. The classification_id for each of these elements can be used as the parent_id
        for underlying data elements to calculate their implied values. Subtotal rows are
        available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.investments_federal_securities()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_6d',
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

    def direct_loan_financing(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Guaranteed and Direct Loan Financing, Net Activity.

        ### Overview
        ----
        This table is a subsidiary table for Means of Financing the Deficit or Disposition
        of Surplus by the U.S. Government providing a detailed view of all direct and
        guaranteed loan financing for federal credit programs under the Credit Reform Act
        of 1990. Guaranteed loan financing is issuing any debt obligation with a guarantee,
        insurance, or other pledge that payment of all or a part of the principal or interest
        will be made to the lender. This table applies to lending to non-federal borrowers by
        non-federal lenders that carries some form of guarantee by the federal government.
        Exceptions include the insurance of deposits, shares, or other withdrawable accounts in
        financial institutions. This table includes total and subtotal rows that should be excluded
        when aggregating data. Some rows represent elements of the dataset's hierarchy, but are not
        assigned values. The classification_id for each of these elements can be used as the parent_id
        for underlying data elements to calculate their implied values. Subtotal rows are available
        to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.direct_loan_financing()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_6e',
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

    def receipts_and_outlays_by_month(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Receipts and Outlays of the U.S. Government by Month.

        ### Overview
        ----
        This table shows the receipts and outlays of the United States Government
        by month for the current fiscal year, up to and including the current
        accounting month. The table also shows the total receipts and outlays for the
        current fiscal year-to-date and the comparable prior fiscal year-to-date. This
        table includes total and subtotal rows that should be excluded when aggregating data.
        Some rows represent elements of the dataset's hierarchy, but are not assigned values.
        The classification_id for each of these elements can be used as the parent_id for
        underlying data elements to calculate their implied values. Subtotal rows are available
        to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.receipts_and_outlays_by_month()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_7',
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

    def trust_fund_impact(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Trust Fund Impact on Budget Results and Investment Holdings.

        ### Overview
        ----
        This table shows the total receipts and outlays and the resulting surplus
        or deficit (shown on the table as excess) for the current month and the current
        fiscal year-to-date for all federal trust funds. The table also shows the totals
        for securities held as investments by the federal trust funds for the beginning
        of the fiscal year and the beginning and ending of the current accounting month.
        A trust fund is a type of account, designated by law, for receipts or offsetting
        receipts dedicated to specific purposes and the expenditure of these receipts.
        This table includes total and subtotal rows that should be excluded when aggregating
        data. Some rows represent elements of the dataset's hierarchy, but are not assigned
        values. The classification_id for each of these elements can be used as the parent_id
        for underlying data elements to calculate their implied values. Subtotal rows are
        available to access this same information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.trust_fund_impact()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_8',
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

    def receipts_by_source_outlay_by_function(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Summary of Receipts by Source, and Outlays by Function of the
        U.S. Government.

        ### Overview
        ----
        This summary table shows, for Budget Receipts, the total amount of activity
        for the current month, the current fiscal year-to-date, the comparable prior
        period year-to-date and the budgeted amount estimated for the current fiscal
        year for various types of receipts (i.e. individual income tax, corporate income
        tax, etc.). The Budget Outlays section of the table shows the total amount of
        activity for the current month, the current fiscal year-to-date, the comparable
        prior period year-to-date and the budgeted amount estimated for the current fiscal
        year for functions of the federal government. The table also shows the amounts for
        the budget/surplus deficit categorized as listed above. This table includes total
        and subtotal rows that should be excluded when aggregating data. Some rows represent
        elements of the dataset's hierarchy, but are not assigned values. The classification_id
        for each of these elements can be used as the parent_id for underlying data elements
        to calculate their implied values. Subtotal rows are available to access this same
        information.

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
            >>> monthly_treasury_service = treasury_client.monthly_treasury_statement()
            >>> monthly_treasury_service.receipts_by_source_outlay_by_function()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v1/accounting/mts/mts_table_9',
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
