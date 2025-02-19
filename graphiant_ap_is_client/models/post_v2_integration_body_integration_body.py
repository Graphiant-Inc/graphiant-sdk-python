from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_integration_body_integration_body_created_on import (
        PostV2IntegrationBodyIntegrationBodyCreatedOn,
    )
    from ..models.post_v2_integration_body_integration_body_details import PostV2IntegrationBodyIntegrationBodyDetails


T = TypeVar("T", bound="PostV2IntegrationBodyIntegrationBody")


@_attrs_define
class PostV2IntegrationBodyIntegrationBody:
    """
    Attributes:
        created_by (Union[Unset, str]):  Example: TYPE_STRING.
        created_on (Union[Unset, PostV2IntegrationBodyIntegrationBodyCreatedOn]):
        details (Union[Unset, PostV2IntegrationBodyIntegrationBodyDetails]):
        enterprise (Union[Unset, str]):  Example: TYPE_INT64.
        integration_type (Union[Unset, str]):  Example: TYPE_ENUM.
        is_active (Union[Unset, str]):  Example: TYPE_BOOL.
        nick_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    created_by: Union[Unset, str] = UNSET
    created_on: Union[Unset, "PostV2IntegrationBodyIntegrationBodyCreatedOn"] = UNSET
    details: Union[Unset, "PostV2IntegrationBodyIntegrationBodyDetails"] = UNSET
    enterprise: Union[Unset, str] = UNSET
    integration_type: Union[Unset, str] = UNSET
    is_active: Union[Unset, str] = UNSET
    nick_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by

        created_on: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.to_dict()

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        enterprise = self.enterprise

        integration_type = self.integration_type

        is_active = self.is_active

        nick_name = self.nick_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_integration_body_integration_body_created_on import (
            PostV2IntegrationBodyIntegrationBodyCreatedOn,
        )
        from ..models.post_v2_integration_body_integration_body_details import (
            PostV2IntegrationBodyIntegrationBodyDetails,
        )

        d = src_dict.copy()
        created_by = d.pop("createdBy", UNSET)

        _created_on = d.pop("createdOn", UNSET)
        created_on: Union[Unset, PostV2IntegrationBodyIntegrationBodyCreatedOn]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = PostV2IntegrationBodyIntegrationBodyCreatedOn.from_dict(_created_on)

        _details = d.pop("details", UNSET)
        details: Union[Unset, PostV2IntegrationBodyIntegrationBodyDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PostV2IntegrationBodyIntegrationBodyDetails.from_dict(_details)

        enterprise = d.pop("enterprise", UNSET)

        integration_type = d.pop("integrationType", UNSET)

        is_active = d.pop("isActive", UNSET)

        nick_name = d.pop("nickName", UNSET)

        post_v2_integration_body_integration_body = cls(
            created_by=created_by,
            created_on=created_on,
            details=details,
            enterprise=enterprise,
            integration_type=integration_type,
            is_active=is_active,
            nick_name=nick_name,
        )

        post_v2_integration_body_integration_body.additional_properties = d
        return post_v2_integration_body_integration_body

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
