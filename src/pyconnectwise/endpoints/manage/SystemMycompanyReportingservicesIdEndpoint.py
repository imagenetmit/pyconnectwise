from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyReportingservicesIdTestconnectionEndpoint import \
    SystemMycompanyReportingservicesIdTestconnectionEndpoint
from pyconnectwise.models.manage import ReportingService
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyReportingservicesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.test_connection = self._register_child_endpoint(
            SystemMycompanyReportingservicesIdTestconnectionEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ReportingService]:
        """
        Performs a GET request against the /system/mycompany/reportingServices/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportingService]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ReportingService,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ReportingService:
        """
        Performs a GET request against the /system/mycompany/reportingServices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportingService: The parsed response data.
        """
        return self._parse_one(ReportingService, super()._make_request("GET", data=data, params=params).json())

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ReportingService:
        """
        Performs a PUT request against the /system/mycompany/reportingServices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportingService: The parsed response data.
        """
        return self._parse_one(ReportingService, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ReportingService:
        """
        Performs a PATCH request against the /system/mycompany/reportingServices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportingService: The parsed response data.
        """
        return self._parse_one(ReportingService, super()._make_request("PATCH", data=data, params=params).json())