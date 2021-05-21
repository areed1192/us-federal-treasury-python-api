import json
import requests
import logging
import pathlib

from typing import Dict
from datetime import datetime
from datetime import date


class TreasurySession():

    """
    Overview:
    ----
    Serves as the main Session for the Current Federal Treasury
    API. The `TreasurySession` object will handle all the
    requests made to the Federal Treasury API.
    """

    def __init__(self, client: object) -> None:
        """Initializes the `TreasurySession` client.

        ### Overview:
        ----
        The `TreasurySession` object handles all the requests made
        for the different endpoints on the Federal Treasury API.

        ### Parameters:
        ----
        client (str): The `treasury.FederalTreasuryClient` Python Client.

        ### Usage:
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> treasury_session = TreasurySession()
        """

        from treasury.client import FederalTreasuryClient

        # We can also add custom formatting to our log messages.
        log_format = '%(asctime)-15s|%(filename)s|%(message)s'

        self.client: FederalTreasuryClient = client
        self.resource = 'https://api.stlouisfed.org/fred'

        if not pathlib.Path('logs').exists():
            pathlib.Path('logs').mkdir()
            pathlib.Path('logs/fred_api_log.log').touch()

        logging.basicConfig(
            filename="logs/treasury_api_log.log",
            level=logging.INFO,
            encoding="utf-8",
            format=log_format
        )

    def __repr__(self) -> str:
        """String representation of the `TreasurySession` object."""

        # define the string representation
        str_representation = '<FederalTreasuryClient.TreasurySession (active=True, connected=True)>'

        return str_representation

    def build_url(self, endpoint: str) -> str:
        """Builds the full url for the endpoint.

        ### Parameters
        ----
        endpoint : str
            The endpoint being requested.

        ### Returns
        ----
        str:
            The full URL with the endpoint needed.
        """

        url = self.resource + endpoint

        return url

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict = None,
        data: dict = None,
        json_payload: dict = None
    ) -> Dict:
        """Handles all the requests in the library.

        ### Overview:
        ---
        A central function used to handle all the requests made in the library,
        this function handles building the URL, defining Content-Type, passing
        through payloads, and handling any errors that may arise during the request.

        ### Parameters:
        ----
        method : str
            The Request method, can be one of the
            following: ['get','post','put','delete','patch']

        endpoint : str
            The API URL endpoint.

        params : dict (optional, Default=None) 
            The URL params for the request.

        data : dict (optional, Default=None)
            A data payload for a request.

        json : dict (optional, Default=None)
            A json data payload for a request

        ### Returns:
        ----
            A Dictionary object containing the JSON values.
        """

        # Build the URL.
        url = self.build_url(endpoint=endpoint)

        logging.info(
            "URL: {url}".format(url=url)
        )

        if 'realtime_start' in params and isinstance(params['realtime_start'], datetime):
            params['realtime_start'] = params['realtime_start'].date().isoformat()

        if 'realtime_end' in params and isinstance(params['realtime_end'], datetime):
            params['realtime_end'] = params['realtime_end'].date().isoformat()

        if 'tag_names' in params and isinstance(params['tag_names'], list):
            logging.info('Joining Tag Names: {lst}'.format(
                lst=params['tag_names']))
            params['tag_names'] = ';'.join(params['tag_names'])

        if 'exclude_tag_names' in params and isinstance(params['exclude_tag_names'], list):
            logging.info('Joining Exclude Tag Names: {lst}'.format(
                lst=params['exclude_tag_names']))
            params['exclude_tag_names'] = ';'.join(params['exclude_tag_names'])

        params_cleaned = params.copy()
        params_cleaned['api_key'] = 'xxxxxxxx'

        logging.info(
            "PARAMS: {params}".format(params=params_cleaned)
        )

        # Define a new session.
        request_session = requests.Session()
        request_session.verify = True

        # Define a new request.
        request_request = requests.Request(
            method=method.upper(),
            url=url,
            params=params,
            data=data,
            json=json_payload
        ).prepare()

        # Send the request.
        response: requests.Response = request_session.send(
            request=request_request
        )

        # Close the session.
        request_session.close()

        # If it's okay and no details.
        if response.ok and len(response.content) > 0:
            return response.json()

        elif len(response.content) > 0 and response.ok:
            return {
                'message': 'response successful',
                'status_code': response.status_code
            }

        elif not response.ok:

            # Define the error dict.
            error_dict = {
                'error_code': response.status_code,
                'response_url': response.url,
                'response_body': json.loads(response.content.decode('ascii')),
                'response_request': dict(response.request.headers),
                'response_method': response.request.method,
            }

            # Log the error.
            logging.error(
                msg=json.dumps(obj=error_dict, indent=4)
            )

            raise requests.HTTPError()
