from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_integration_getall_enterprise_id_response_200_integrations_item_details import (
        GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItemDetails,
    )


T = TypeVar("T", bound="GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItem")


@_attrs_define
class GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItem:
    """
    Attributes:
        created_by (Union[Unset, str]):  Example: TYPE_STRING.
        created_on (Union[Unset, str]):  Example: TYPE_STRING.
        details (Union[Unset, GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItemDetails]):
        enterprise_id (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        is_active (Union[Unset, str]):  Example: TYPE_BOOL.
        nick_name (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    created_by: Union[Unset, str] = UNSET
    created_on: Union[Unset, str] = UNSET
    details: Union[Unset, "GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItemDetails"] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_active: Union[Unset, str] = UNSET
    nick_name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by

        created_on = self.created_on

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        enterprise_id = self.enterprise_id

        id = self.id

        is_active = self.is_active

        nick_name = self.nick_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if details is not UNSET:
            field_dict["details"] = details
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if nick_name is not UNSET:
            field_dict["nickName"] = nick_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_integration_getall_enterprise_id_response_200_integrations_item_details import (
            GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItemDetails,
        )

        d = src_dict.copy()
        created_by = d.pop("createdBy", UNSET)

        created_on = d.pop("createdOn", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItemDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItemDetails.from_dict(_details)

        enterprise_id = d.pop("enterpriseId", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("isActive", UNSET)

        nick_name = d.pop("nickName", UNSET)

        type_ = d.pop("type", UNSET)

        get_v2_integration_getall_enterprise_id_response_200_integrations_item = cls(
            created_by=created_by,
            created_on=created_on,
            details=details,
            enterprise_id=enterprise_id,
            id=id,
            is_active=is_active,
            nick_name=nick_name,
            type_=type_,
        )

        get_v2_integration_getall_enterprise_id_response_200_integrations_item.additional_properties = d
        return get_v2_integration_getall_enterprise_id_response_200_integrations_item

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
