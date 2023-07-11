from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel

class MemberDeactivationCompanyTeamModel(ConnectWiseModel):
    count: int
    id: int
    name: str
    re_assign_to_member: MemberReferenceModel
    re_assign_to_contact: ContactReferenceModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True