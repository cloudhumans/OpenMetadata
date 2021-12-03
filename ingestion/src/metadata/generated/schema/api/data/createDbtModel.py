# generated by datamodel-codegen:
#   filename:  schema/api/data/createDbtModel.json
#   timestamp: 2021-12-02T02:28:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ...entity.data import dbtmodel, table
from ...type import basic, entityReference, tagLabel


class CreateDbtModelEntityRequest(BaseModel):
    name: dbtmodel.DbtModelName = Field(
        ...,
        description='Name that identifies the this entity instance uniquely. Same as id if when name is not unique',
    )
    description: Optional[str] = Field(
        None, description='Description of DBTModel instance.'
    )
    dbtNodeType: Optional[dbtmodel.DbtNodeType] = None
    columns: List[table.Column] = Field(..., description='Schema of the Model')
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this entity'
    )
    database: Optional[basic.Uuid] = Field(
        None, description='Database corresponding to this table'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this model'
    )
    viewDefinition: Optional[basic.SqlQuery] = Field(
        None, description='View Definition in SQL.'
    )