from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdInfoEndpoint import SystemEmailconnectorsIdInfoEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdParsingstylesEndpoint import \
    SystemEmailconnectorsIdParsingstylesEndpoint
from pyconnectwise.models.manage import EmailConnector
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemEmailconnectorsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SystemEmailconnectorsIdInfoEndpoint(client, parent_endpoint=self))
        self.parsing_styles = self._register_child_endpoint(
            SystemEmailconnectorsIdParsingstylesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[EmailConnector]:
        """
        Performs a GET request against the /system/emailConnectors/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailConnector]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            EmailConnector,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EmailConnector:
        """
        Performs a GET request against the /system/emailConnectors/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailConnector: The parsed response data.
        """
        return self._parse_one(EmailConnector, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /system/emailConnectors/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EmailConnector:
        """
        Performs a PUT request against the /system/emailConnectors/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailConnector: The parsed response data.
        """
        return self._parse_one(EmailConnector, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EmailConnector:
        """
        Performs a PATCH request against the /system/emailConnectors/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailConnector: The parsed response data.
        """
        return self._parse_one(EmailConnector, super()._make_request("PATCH", data=data, params=params).json())