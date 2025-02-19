from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v2_integration_integration_id_body_integration_body import (
        PutV2IntegrationIntegrationIdBodyIntegrationBody,
    )


T = TypeVar("T", bound="PutV2IntegrationIntegrationIdBody")


@_attrs_define
class PutV2IntegrationIntegrationIdBody:
    """
    Attributes:
        integration_body (Union[Unset, PutV2IntegrationIntegrationIdBodyIntegrationBody]):
    """

    integration_body: Union[Unset, "PutV2IntegrationIntegrationIdBodyIntegrationBody"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.integration_body, Unset):
            integration_body = self.integration_body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if integration_body is not UNSET:
            field_dict["integrationBody"] = integration_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v2_integration_integration_id_body_integration_body import (
            PutV2IntegrationIntegrationIdBodyIntegrationBody,
        )

        d = src_dict.copy()
        _integration_body = d.pop("integrationBody", UNSET)
        integration_body: Union[Unset, PutV2IntegrationIntegrationIdBodyIntegrationBody]
        if isinstance(_integration_body, Unset):
            integration_body = UNSET
        else:
            integration_body = PutV2IntegrationIntegrationIdBodyIntegrationBody.from_dict(_integration_body)

        put_v2_integration_integration_id_body = cls(
            integration_body=integration_body,
        )

        put_v2_integration_integration_id_body.additional_properties = d
        return put_v2_integration_integration_id_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
