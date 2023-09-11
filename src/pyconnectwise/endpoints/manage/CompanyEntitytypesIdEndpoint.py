from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyEntitytypesIdInfoEndpoint import CompanyEntitytypesIdInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyEntitytypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyEntitytypesIdInfoEndpoint(client, parent_endpoint=self))