from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_integration_getall_enterprise_id_response_200_integrations_item import (
        GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItem,
    )


T = TypeVar("T", bound="GetV2IntegrationGetallEnterpriseIdResponse200")


@_attrs_define
class GetV2IntegrationGetallEnterpriseIdResponse200:
    """
    Attributes:
        integrations (Union[Unset, list['GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItem']]):
    """

    integrations: Union[Unset, list["GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integrations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.integrations, Unset):
            integrations = []
            for integrations_item_data in self.integrations:
                integrations_item = integrations_item_data.to_dict()
                integrations.append(integrations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if integrations is not UNSET:
            field_dict["integrations"] = integrations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_integration_getall_enterprise_id_response_200_integrations_item import (
            GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItem,
        )

        d = src_dict.copy()
        integrations = []
        _integrations = d.pop("integrations", UNSET)
        for integrations_item_data in _integrations or []:
            integrations_item = GetV2IntegrationGetallEnterpriseIdResponse200IntegrationsItem.from_dict(
                integrations_item_data
            )

            integrations.append(integrations_item)

        get_v2_integration_getall_enterprise_id_response_200 = cls(
            integrations=integrations,
        )

        get_v2_integration_getall_enterprise_id_response_200.additional_properties = d
        return get_v2_integration_getall_enterprise_id_response_200

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
