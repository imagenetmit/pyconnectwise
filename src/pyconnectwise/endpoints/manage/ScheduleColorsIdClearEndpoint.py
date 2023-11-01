from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import ScheduleColor
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ScheduleColorsIdClearEndpoint(
    ConnectWiseEndpoint, IPostable[ScheduleColor, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "clear", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, ScheduleColor)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ScheduleColor:
        """
        Performs a POST request against the /schedule/colors/{id}/clear endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleColor: The parsed response data.
        """
        return self._parse_one(
            ScheduleColor,
            super()._make_request("POST", data=data, params=params).json(),
        )
