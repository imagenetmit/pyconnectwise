from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCategoriesIdSubcategoriesInfoCountEndpoint import (
    ProcurementCategoriesIdSubcategoriesInfoCountEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import LegacySubCategoryInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ProcurementCategoriesIdSubcategoriesInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LegacySubCategoryInfo], ConnectWiseManageRequestParams],
    IPaginateable[LegacySubCategoryInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LegacySubCategoryInfo])
        IPaginateable.__init__(self, LegacySubCategoryInfo)

        self.count = self._register_child_endpoint(
            ProcurementCategoriesIdSubcategoriesInfoCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[LegacySubCategoryInfo]:
        """
        Performs a GET request against the /procurement/categories/{id}/subcategories/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LegacySubCategoryInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LegacySubCategoryInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[LegacySubCategoryInfo]:
        """
        Performs a GET request against the /procurement/categories/{id}/subcategories/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LegacySubCategoryInfo]: The parsed response data.
        """
        return self._parse_many(
            LegacySubCategoryInfo,
            super()._make_request("GET", data=data, params=params).json(),
        )
