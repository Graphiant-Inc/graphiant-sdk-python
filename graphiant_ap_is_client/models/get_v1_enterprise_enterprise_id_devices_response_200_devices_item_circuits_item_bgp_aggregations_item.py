from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemCircuitsItemBgpAggregationsItem")


@_attrs_define
class GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemCircuitsItemBgpAggregationsItem:
    """
    Attributes:
        as_set (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        prefix (Union[Unset, str]):  Example: TYPE_STRING.
        summary_only (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    as_set: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    summary_only: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_set = self.as_set

        id = self.id

        prefix = self.prefix

        summary_only = self.summary_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_set is not UNSET:
            field_dict["asSet"] = as_set
        if id is not UNSET:
            field_dict["id"] = id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if summary_only is not UNSET:
            field_dict["summaryOnly"] = summary_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        as_set = d.pop("asSet", UNSET)

        id = d.pop("id", UNSET)

        prefix = d.pop("prefix", UNSET)

        summary_only = d.pop("summaryOnly", UNSET)

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_circuits_item_bgp_aggregations_item = cls(
            as_set=as_set,
            id=id,
            prefix=prefix,
            summary_only=summary_only,
        )

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_circuits_item_bgp_aggregations_item.additional_properties = d
        return get_v1_enterprise_enterprise_id_devices_response_200_devices_item_circuits_item_bgp_aggregations_item

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
