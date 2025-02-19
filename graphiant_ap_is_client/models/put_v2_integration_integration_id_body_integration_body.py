from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v2_integration_integration_id_body_integration_body_details import (
        PutV2IntegrationIntegrationIdBodyIntegrationBodyDetails,
    )


T = TypeVar("T", bound="PutV2IntegrationIntegrationIdBodyIntegrationBody")


@_attrs_define
class PutV2IntegrationIntegrationIdBodyIntegrationBody:
    """
    Attributes:
        details (Union[Unset, PutV2IntegrationIntegrationIdBodyIntegrationBodyDetails]):
        enterprise (Union[Unset, str]):  Example: TYPE_INT64.
        integration_type (Union[Unset, str]):  Example: TYPE_ENUM.
        is_active (Union[Unset, str]):  Example: TYPE_BOOL.
        nick_name (Union[Unset, str]):  Example: TYPE_STRING.
        updated_by (Union[Unset, str]):  Example: TYPE_STRING.
    """

    details: Union[Unset, "PutV2IntegrationIntegrationIdBodyIntegrationBodyDetails"] = UNSET
    enterprise: Union[Unset, str] = UNSET
    integration_type: Union[Unset, str] = UNSET
    is_active: Union[Unset, str] = UNSET
    nick_name: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        enterprise = self.enterprise

        integration_type = self.integration_type

        is_active = self.is_active

        nick_name = self.nick_name

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if enterprise is not UNSET:
            field_dict["enterprise"] = enterprise
        if integration_type is not UNSET:
            field_dict["integrationType"] = integration_type
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if nick_name is not UNSET:
            field_dict["nickName"] = nick_name
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v2_integration_integration_id_body_integration_body_details import (
            PutV2IntegrationIntegrationIdBodyIntegrationBodyDetails,
        )

        d = src_dict.copy()
        _details = d.pop("details", UNSET)
        details: Union[Unset, PutV2IntegrationIntegrationIdBodyIntegrationBodyDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PutV2IntegrationIntegrationIdBodyIntegrationBodyDetails.from_dict(_details)

        enterprise = d.pop("enterprise", UNSET)

        integration_type = d.pop("integrationType", UNSET)

        is_active = d.pop("isActive", UNSET)

        nick_name = d.pop("nickName", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        put_v2_integration_integration_id_body_integration_body = cls(
            details=details,
            enterprise=enterprise,
            integration_type=integration_type,
            is_active=is_active,
            nick_name=nick_name,
            updated_by=updated_by,
        )

        put_v2_integration_integration_id_body_integration_body.additional_properties = d
        return put_v2_integration_integration_id_body_integration_body

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
