from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeChargecodesIdExpensetypesCountEndpoint import \
    TimeChargecodesIdExpensetypesCountEndpoint
from pyconnectwise.endpoints.manage.TimeChargecodesIdExpensetypesIdEndpoint import \
    TimeChargecodesIdExpensetypesIdEndpoint
from pyconnectwise.models.manage import ChargeCodeExpenseType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeChargecodesIdExpensetypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "expenseTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            TimeChargecodesIdExpensetypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> TimeChargecodesIdExpensetypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeChargecodesIdExpensetypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeChargecodesIdExpensetypesIdEndpoint: The initialized TimeChargecodesIdExpensetypesIdEndpoint object.
        """
        child = TimeChargecodesIdExpensetypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ChargeCodeExpenseType]:
        """
        Performs a GET request against the /time/chargeCodes/{id}/expenseTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ChargeCodeExpenseType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ChargeCodeExpenseType,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ChargeCodeExpenseType]:
        """
        Performs a GET request against the /time/chargeCodes/{id}/expenseTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChargeCodeExpenseType]: The parsed response data.
        """
        return self._parse_many(ChargeCodeExpenseType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ChargeCodeExpenseType:
        """
        Performs a POST request against the /time/chargeCodes/{id}/expenseTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ChargeCodeExpenseType: The parsed response data.
        """
        return self._parse_one(ChargeCodeExpenseType, super()._make_request("POST", data=data, params=params).json())