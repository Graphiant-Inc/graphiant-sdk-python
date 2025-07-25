# coding: utf-8

"""
    Graphiant APIs

    Graphiant API documentation.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class V1NatEntriesDeviceIdGet200ResponseNatEntriesInner(BaseModel):
    """
    V1NatEntriesDeviceIdGet200ResponseNatEntriesInner
    """ # noqa: E501
    destination_ip_address: Optional[StrictStr] = Field(default=None, alias="destinationIpAddress")
    destination_port: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="destinationPort")
    inside_global_ip_address: Optional[StrictStr] = Field(default=None, alias="insideGlobalIpAddress")
    inside_global_port: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="insideGlobalPort")
    inside_local_ip_address: Optional[StrictStr] = Field(default=None, alias="insideLocalIpAddress")
    inside_local_port: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="insideLocalPort")
    nat_type: Optional[StrictStr] = Field(default=None, alias="natType")
    outside_global_ip_address: Optional[StrictStr] = Field(default=None, alias="outsideGlobalIpAddress")
    outside_global_port: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="outsideGlobalPort")
    pre_destination_ip_address: Optional[StrictStr] = Field(default=None, alias="preDestinationIpAddress")
    pre_destination_port: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="preDestinationPort")
    vrf_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="vrfId")
    __properties: ClassVar[List[str]] = ["destinationIpAddress", "destinationPort", "insideGlobalIpAddress", "insideGlobalPort", "insideLocalIpAddress", "insideLocalPort", "natType", "outsideGlobalIpAddress", "outsideGlobalPort", "preDestinationIpAddress", "preDestinationPort", "vrfId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1NatEntriesDeviceIdGet200ResponseNatEntriesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1NatEntriesDeviceIdGet200ResponseNatEntriesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destinationIpAddress": obj.get("destinationIpAddress"),
            "destinationPort": obj.get("destinationPort"),
            "insideGlobalIpAddress": obj.get("insideGlobalIpAddress"),
            "insideGlobalPort": obj.get("insideGlobalPort"),
            "insideLocalIpAddress": obj.get("insideLocalIpAddress"),
            "insideLocalPort": obj.get("insideLocalPort"),
            "natType": obj.get("natType"),
            "outsideGlobalIpAddress": obj.get("outsideGlobalIpAddress"),
            "outsideGlobalPort": obj.get("outsideGlobalPort"),
            "preDestinationIpAddress": obj.get("preDestinationIpAddress"),
            "preDestinationPort": obj.get("preDestinationPort"),
            "vrfId": obj.get("vrfId")
        })
        return _obj


