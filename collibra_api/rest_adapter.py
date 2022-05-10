import requests
# import requests.packages
import logging
from collibra_api.exceptions import CollibraApiException
from collibra_api.models import Result
from json import JSONDecodeError
from base64 import b64encode
logging.basicConfig()


class RestAdapter:
    def __init__(self, hostname: str, username: str, password: str, version: str = '2.0', logger: logging.Logger = None) -> None:
        """
        Constructor for RestAdapter Class
        :param hostname: normally the collibra dgc instance url, e.g. lloyds-dev.collibra.com
        :param username: username of the user to connect to the collibra dgc instance
        :param password: password of the user to connect to the collibra dgc instance
        :param version: version of the rest api for the dgc instance, currently 2.0
        :param logger: (optional) application specific logger
        """

        self._logger = logger or logging.getLogger(__name__)
        self._logger.setLevel(level=logging.DEBUG)
        self.url = f'https://{hostname}/rest/{version}'
        basic_auth = str(b64encode(f'{username}:{password}'.encode('utf-8')), 'utf-8')
        self._default_headers = {'Authorization': f'Basic {basic_auth}'}

    def _do(self, http_method: str, endpoint: str, query_params: dict = None, data: dict = None) -> Result:
        full_url = self.url + endpoint
        # log http_method, full_url, query_params and data, preform http request, catch and raise any errors
        try:
            self._logger.debug(f'{http_method=}, {full_url=}, {query_params=}, {data=}')
            response = requests.request(method=http_method,
                                        url=full_url,
                                        headers=self._default_headers,
                                        params=query_params,
                                        json=data)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=e)
            raise CollibraApiException("Request Failed") from e
        # validate response ok (200-299), log response status
        if response.ok:
            self._logger.debug(f'{response.ok=}, {response.status_code=}, {response.reason=}')
            # try to return the results object
            # if the response is a json array of dicts otherwise return the json dict
            # raise error if we can't parse the response
            try:
                return Result(status_code=response.status_code,
                              message=response.reason,
                              **response.json())
            except TypeError:
                return Result(status_code=response.status_code,
                              message=response.reason,
                              results=response.json())
            except (ValueError, JSONDecodeError) as e:
                self._logger.error(msg=e)
                raise CollibraApiException("Bad Json in Response") from e
        # raise invalid repsone error
        raise CollibraApiException(response.json()['userMessage'])

    def get(self, endpoint: str, query_params: dict = None) -> Result:
        return self._do(http_method='GET',
                        endpoint=endpoint,
                        query_params=query_params)

    def post(self, endpoint: str, query_parms: dict = None, data: dict = None) -> Result:
        return self._do(http_method='POST',
                        endpoint=endpoint,
                        query_params=query_parms,
                        data=data)

    def delete(self, endpoint: str, query_parms: dict = None, data: dict = None) -> Result:
        return self._do(http_method='DELETE',
                        endpoint=endpoint,
                        query_parms=query_parms,
                        data=data)
