from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesIdEndpoint import ProcurementSubcategoriesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesCountEndpoint import ProcurementSubcategoriesCountEndpoint
from pyconnectwise.models.manage.SubCategoryModel import SubCategoryModel

class ProcurementSubcategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self._register_child_endpoint(
            ProcurementSubcategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementSubcategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementSubcategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementSubcategoriesIdEndpoint: The initialized ProcurementSubcategoriesIdEndpoint object.
        """
        child = ProcurementSubcategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SubCategoryModel]:
        """
        Performs a GET request against the /procurement/subcategories/ endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SubCategoryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request(
                "GET",
                params=params
            ),
            SubCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SubCategoryModel]:
        """
        Performs a GET request against the /procurement/subcategories/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SubCategoryModel]: The parsed response data.
        """
        return self._parse_many(SubCategoryModel, super()._make_request("GET", data=data, params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SubCategoryModel:
        """
        Performs a POST request against the /procurement/subcategories/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SubCategoryModel: The parsed response data.
        """
        return self._parse_one(SubCategoryModel, super()._make_request("POST", data=data, params=params).json())
        