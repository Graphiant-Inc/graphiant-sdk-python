from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_integration_gettypes_enterprise_id_response_200_integrations_item_integrations_item import (
        GetV2IntegrationGettypesEnterpriseIdResponse200IntegrationsItemIntegrationsItem,
    )


T = TypeVar("T", bound="GetV2IntegrationGettypesEnterpriseIdResponse200IntegrationsItem")


@_attrs_define
class GetV2IntegrationGettypesEnterpriseIdResponse200IntegrationsItem:
    """
    Attributes:
        integrations (Union[Unset,
            list['GetV2IntegrationGettypesEnterpriseIdResponse200IntegrationsItemIntegrationsItem']]):
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    integrations: Union[
        Unset, list["GetV2IntegrationGettypesEnterpriseIdResponse200IntegrationsItemIntegrationsItem"]
    ] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integrations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.integrations, Unset):
            integrations = []
            for integrations_item_data in self.integrations:
                integrations_item = integrations_item_data.to_dict()
                integrations.append(integrations_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if integrations is not UNSET:
            field_dict["integrations"] = integrations
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_integration_gettypes_enterprise_id_response_200_integrations_item_integrations_item import (
            GetV2IntegrationGettypesEnterpriseIdResponse200IntegrationsItemIntegrationsItem,
        )

        d = src_dict.copy()
        integrations = []
        _integrations = d.pop("integrations", UNSET)
        for integrations_item_data in _integrations or []:
            integrations_item = (
                GetV2IntegrationGettypesEnterpriseIdResponse200IntegrationsItemIntegrationsItem.from_dict(
                    integrations_item_data
                )
            )

            integrations.append(integrations_item)

        type_ = d.pop("type", UNSET)

        get_v2_integration_gettypes_enterprise_id_response_200_integrations_item = cls(
            integrations=integrations,
            type_=type_,
        )

        get_v2_integration_gettypes_enterprise_id_response_200_integrations_item.additional_properties = d
        return get_v2_integration_gettypes_enterprise_id_response_200_integrations_item

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
