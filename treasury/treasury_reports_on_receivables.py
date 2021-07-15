from typing import Dict
from typing import List
from treasury.session import FederalTreasurySession


class TreasuryReportsOnReceivables():

    """
    ## Overview:
    ----
    The Treasury Report on Receivables and Debt Collection Activities
    (TROR) is the federal government's primary means for collecting
    data on the status of non-tax receivables (delinquent and
    non-delinquent debt) owed to the United States.
    """

    def __init__(self, session: FederalTreasurySession) -> None:
        """Initializes the `TreasuryReportsOnReceivables` object.

        ### Parameters
        ----
        session : `TreasurySession`
            An initialized session of the `TreasurySession`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> reports_on_receivables_service = treasury_client.treasury_reports_on_receivables()
        """

        # Set the session.
        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.TreasuryReportsOnReceivables` object."""

        # define the string representation
        str_representation = '<FederalTreasuryClient.TreasuryReportsOnReceivables (active=True, connected=True)>'

        return str_representation

    def full_data(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries the full data report for TROR.

        ### Overview
        ----
        The Treasury Report on Receivables and Debt Collection Activities (TROR)
        is the federal government's primary means for collecting data on the status
        of non-tax receivables (delinquent and non-delinquent debt) owed to the
        United States. This report provides summary data on the value of receivables
        owed to the Federal government, the portion of those receivables that are
        delinquent, and efforts to collect or write off delinquent debt. Receivables
        are categorized as being either current or delinquent. Delinquent receivables
        are also referred to as delinquent debt. Receivables are also categorized by
        type of receivable: Administrative Receivables, Direct Loans, and Defaulted
        Guaranteed Loans. Administrative Receivables are non-loan receivables, including
        fines, payments, and overpayments. Direct Loans and Defaulted Guaranteed Loans are
        federal loan receivables. Generally, Federal creditor agencies assess interest on
        outstanding loan receivables. Federal creditor agencies are also generally required
        to assess interest, penalties, and administrative costs when receivables become
        delinquent. The rate of interest is generally governed by 31 U.S.C. Section 3717
        and published by the Department of the Treasury. Collections are not always mutually
        exclusive. The amount and count of collections are recorded for each tool or
        technique that is used to collect funds.

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
            >>> reports_on_receivables_service = treasury_client.treasury_reports_on_receivables()
            >>> reports_on_receivables_service.full_data()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/debt/tror',
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

    def collected_and_outstanding_receivables(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Collected & Outstanding Receivables from TROR.

        ### Overview
        ----
        Collected and Outstanding Receivables provides amounts owed to the federal government
        by an individual, organization, or entity other than another federal agency during
        the reporting period. The total outstanding receivable balance at the end of a fiscal
        year is the net of receivables that remained unpaid from prior fiscal years and new
        receivables recorded during that fiscal year, less collections, adjustments, and amounts
        written off and closed out. Receivables are categorized as being either current or
        delinquent. Delinquent receivables are also referred to as delinquent debt. Receivables
        are also categorized by type of receivable: Administrative Receivables, Direct Loans,
        and Defaulted Guaranteed Loans. Administrative Receivables are non-loan receivables,
        including fines, payments, and overpayments. Direct Loans and Defaulted Guaranteed Loans
        are federal loan receivables. Generally, federal creditor agencies assess interest on
        outstanding loan receivables. Federal creditor agencies are also generally required to
        assess interest, penalties, and administrative costs when receivables become delinquent.
        The rate of interest is generally governed by 31 U.S.C. Section 3717 and published by the
        Department of the Treasury. Collections are not always mutually exclusive. The amount and
        count of collections are recorded for each tool or technique that is used to collect funds.

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
            >>> reports_on_receivables_service = treasury_client.treasury_reports_on_receivables()
            >>> reports_on_receivables_service.collected_and_outstanding_receivables()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/debt/tror/collected_outstanding_recv',
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

    def collections_delinquent_debt(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Collections on Delinquent Debt from TROR.

        ### Overview
        ----
        Collections on Delinquent Debt provides amounts of delinquent debt collected during the
        reporting period. Federal creditor agencies utilize a combination of debt collection tools.
        Among these collection tools are administrative wage garnishment (AWG), use of private
        collection agencies (PCAs), offset of Federal and State payments through the Treasury Offset
        Program (TOP), use of Fiscal Service's Cross-Servicing Program (CS), and litigation. Before
        using most collection tools, federal creditor agencies must first provide debtors with due
        process. This includes providing notice and an opportunity to enter into a repayment agreement
        based on the debtor's financial circumstances, dispute the debt, or object to the intended
        collection action. Generally, federal creditor agencies are required to refer delinquent federal
        non-tax debt to Fiscal Service for collection through its delinquent debt collection programs,
        known as the Cross-Servicing Program and TOP. Federal creditor agencies generally are required
        to refer debts at no later than 120 days delinquent to the Cross-Servicing Program and TOP. Before
        referring a debt to Fiscal Service for collection, federal creditor agencies must provide debtors
        with notice and an opportunity to enter into a repayment agreement based on the debtor's financial
        circumstances, dispute the debt, or object to the intended collection action. While federal creditor
        agencies are responsible for providing this required due process, Fiscal Service also provides
        debtors with additional opportunities to resolve their debts prior to the initiation of adverse
        collection action. For example, prior to initiating a collection action, the Cross-Servicing
        Program sends a demand letter to each debtor, and TOP sends a warning letter to payees before offsetting
        recurring payments. Collections are not always mutually exclusive. The amount and count of collections
        are recorded for each tool or technique that is used to collect funds.

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
            >>> reports_on_receivables_service = treasury_client.treasury_reports_on_receivables()
            >>> reports_on_receivables_service.collections_delinquent_debt()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/debt/tror/collections_delinquent_debt',
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

    def data_act_compliance(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Data Act Compliance from TROR.

        ### Overview
        ----
        The 120 Day Delinquent Debt Referral Compliance Report provides access to tracking
        and benchmarking compliance with the requirements of a key provision of the Digital
        Accountability and Transparency Act of 2014 (the DATA Act). This table provides quick
        insights into federal agency compliance rates, as well as information on the number
        of eligible debts and debts referred or not referred each quarter, beginning in
        Fiscal Year 2016.

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
            >>> reports_on_receivables_service = treasury_client.treasury_reports_on_receivables()
            >>> reports_on_receivables_service.data_act_compliance()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/debt/tror/data_act_compliance',
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

    def delinquent_debt(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Delinquent Debt from TROR.

        ### Overview
        ----
        Delinquent Debt provides delinquent debt amounts owed to the federal government by
        an individual, organization, or entity other than another federal agency during the
        reporting period. A non-tax debt is considered delinquent if it has not been paid by
        the date specified in an agency's initial written demand for payment or applicable
        agreement. A non-tax debt may become delinquent during the same fiscal year that it
        was recorded as a receivable or during a subsequent fiscal year. The total outstanding
        delinquent debt balance at the end of a fiscal year is the net of debt that remained
        delinquent from previous fiscal years and debt that became delinquent during that fiscal
        year, less collections, adjustments, and amounts written off. The calculation of the
        amount that became delinquent during the fiscal year is based on debt that was between
        1 and 365 days delinquent as of September 30 of the Fiscal Year. Delinquent debts are
        categorized by age: 1-180 days, 181 days-2 years, 2-6 years, 6-10 years, and >10 years.
        Delinquent debts are also categorized by creditor agency category: Commercial, Consumer,
        Foreign and Sovereign Government, and State and Local Government. Beginning in first
        quarter of FY2016, the dataset includes additional detailed breakdowns of the U.S.
        Government's delinquent debt by age, as required by the DATA Act.

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
            >>> reports_on_receivables_service = treasury_client.treasury_reports_on_receivables()
            >>> reports_on_receivables_service.delinquent_debt()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/debt/tror/delinquent_debt',
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

    def written_off_delinquent_debt(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100
    ) -> Dict:
        """Queries Written Off Delinquent Debt from TROR.

        ### Overview
        ----
        Written Off Delinquent Debt provides amounts of delinquent debt written off
        during the reporting period. Federal creditor agencies are generally 
        to write off non-tax debt that is two years delinquent (see Office of Management
        and Budget Circular A-129). By writing off delinquent federal non-tax debt as
        uncollectible, federal creditor agencies more accurately reflect the value of
        their receivables on the books of the United States. Certain write-offs are
        categorized as currently not collectible (CNC), which means that collection 
        efforts continue until the agency determines it should terminate those efforts.
        Currently not collectibles debts are not always mutually exclusive as the amounts
        and counts are recorded for each tool or technique that is used to collect funds.
        Other write-offs are categorized as closed out, meaning a federal creditor agency
        has terminated all debt collection action. Consequently, a federal creditor agency
        may be required to report such write-offs to the Internal Revenue Service (IRS) as
        potential income to the debtor.

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
            >>> reports_on_receivables_service = treasury_client.treasury_reports_on_receivables()
            >>> reports_on_receivables_service.written_off_delinquent_debt()
        """

        if fields:
            fields = ','.join(fields)

        if filters:
            filters = ','.join(filters)

        if sort:
            sort = ','.join(sort)

        content = self.treasury_session.make_request(
            method='get',
            endpoint='/v2/debt/tror/written_off_delinquent_debt',
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
