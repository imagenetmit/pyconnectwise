from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsIdAssociationsIdEndpoint import ServiceBoardsIdItemsIdAssociationsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsIdAssociationsCountEndpoint import ServiceBoardsIdItemsIdAssociationsCountEndpoint
from pyconnectwise.models.manage.BoardItemAssociationModel import BoardItemAssociationModel

class ServiceBoardsIdItemsIdAssociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "associations", parent_endpoint=parent_endpoint)
        
        self.count = self._register_child_endpoint(
            ServiceBoardsIdItemsIdAssociationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceBoardsIdItemsIdAssociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdItemsIdAssociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdItemsIdAssociationsIdEndpoint: The initialized ServiceBoardsIdItemsIdAssociationsIdEndpoint object.
        """
        child = ServiceBoardsIdItemsIdAssociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardItemAssociationModel]:
        """
        Performs a GET request against the /service/boards/{grandparentId}/items/{parentId}/associations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardItemAssociationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request(
                "GET",
                params=params
            ),
            BoardItemAssociationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardItemAssociationModel]:
        """
        Performs a GET request against the /service/boards/{grandparentId}/items/{parentId}/associations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardItemAssociationModel]: The parsed response data.
        """
        return self._parse_many(BoardItemAssociationModel, super()._make_request("GET", data=data, params=params).json())
        