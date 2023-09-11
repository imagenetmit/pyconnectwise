from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTracksCountEndpoint import CompanyContactsIdTracksCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTracksIdEndpoint import CompanyContactsIdTracksIdEndpoint
from pyconnectwise.models.manage import ContactTrack
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsIdTracksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tracks", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyContactsIdTracksCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyContactsIdTracksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdTracksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdTracksIdEndpoint: The initialized CompanyContactsIdTracksIdEndpoint object.
        """
        child = CompanyContactsIdTracksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ContactTrack]:
        """
        Performs a GET request against the /company/contacts/{id}/tracks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactTrack]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ContactTrack,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactTrack]:
        """
        Performs a GET request against the /company/contacts/{id}/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactTrack]: The parsed response data.
        """
        return self._parse_many(ContactTrack, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactTrack:
        """
        Performs a POST request against the /company/contacts/{id}/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactTrack: The parsed response data.
        """
        return self._parse_one(ContactTrack, super()._make_request("POST", data=data, params=params).json())