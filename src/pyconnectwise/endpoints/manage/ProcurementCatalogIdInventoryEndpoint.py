from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdInventoryCountEndpoint import \
    ProcurementCatalogIdInventoryCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdInventoryIdEndpoint import \
    ProcurementCatalogIdInventoryIdEndpoint
from pyconnectwise.models.manage import CatalogInventory
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementCatalogIdInventoryEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inventory", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementCatalogIdInventoryCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementCatalogIdInventoryIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCatalogIdInventoryIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCatalogIdInventoryIdEndpoint: The initialized ProcurementCatalogIdInventoryIdEndpoint object.
        """
        child = ProcurementCatalogIdInventoryIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CatalogInventory]:
        """
        Performs a GET request against the /procurement/catalog/{id}/inventory endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CatalogInventory]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CatalogInventory,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CatalogInventory]:
        """
        Performs a GET request against the /procurement/catalog/{id}/inventory endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CatalogInventory]: The parsed response data.
        """
        return self._parse_many(CatalogInventory, super()._make_request("GET", data=data, params=params).json())