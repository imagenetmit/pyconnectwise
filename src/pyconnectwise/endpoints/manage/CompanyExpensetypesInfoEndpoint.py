from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyExpensetypesInfoCountEndpoint import CompanyExpensetypesInfoCountEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyExpensetypesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyExpensetypesInfoCountEndpoint(client, parent_endpoint=self))