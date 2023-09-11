from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectPhasestatusesCountEndpoint import ProjectPhasestatusesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectPhasestatusesIdEndpoint import ProjectPhasestatusesIdEndpoint
from pyconnectwise.models.manage import PhaseStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectPhasestatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "phaseStatuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProjectPhasestatusesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectPhasestatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectPhasestatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectPhasestatusesIdEndpoint: The initialized ProjectPhasestatusesIdEndpoint object.
        """
        child = ProjectPhasestatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PhaseStatus]:
        """
        Performs a GET request against the /project/phaseStatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PhaseStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PhaseStatus,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PhaseStatus]:
        """
        Performs a GET request against the /project/phaseStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PhaseStatus]: The parsed response data.
        """
        return self._parse_many(PhaseStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PhaseStatus:
        """
        Performs a POST request against the /project/phaseStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PhaseStatus: The parsed response data.
        """
        return self._parse_one(PhaseStatus, super()._make_request("POST", data=data, params=params).json())