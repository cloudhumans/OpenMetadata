# generated by datamodel-codegen:
#   filename:  schema/type/entityUsage.json
#   timestamp: 2021-12-02T02:38:07+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from . import entityReference, usageDetails


class UsageDetailsOfAnEntity(BaseModel):
    entity: entityReference.EntityReference = Field(
        ..., description='Entity for which usage is returned.'
    )
    usage: List[usageDetails.TypeUsedToReturnUsageDetailsOfAnEntity] = Field(
        ..., description='List usage details per day.'
    )