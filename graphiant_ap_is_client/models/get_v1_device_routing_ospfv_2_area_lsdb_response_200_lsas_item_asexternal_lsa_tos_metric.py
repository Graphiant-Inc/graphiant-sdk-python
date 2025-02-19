from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemAsexternalLsaTosMetric")


@_attrs_define
class GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemAsexternalLsaTosMetric:
    """
    Attributes:
        tos (Union[Unset, str]):  Example: TYPE_UINT32.
        tos_metric (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    tos: Union[Unset, str] = UNSET
    tos_metric: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tos = self.tos

        tos_metric = self.tos_metric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tos is not UNSET:
            field_dict["tos"] = tos
        if tos_metric is not UNSET:
            field_dict["tosMetric"] = tos_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        tos = d.pop("tos", UNSET)

        tos_metric = d.pop("tosMetric", UNSET)

        get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_asexternal_lsa_tos_metric = cls(
            tos=tos,
            tos_metric=tos_metric,
        )

        get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_asexternal_lsa_tos_metric.additional_properties = d
        return get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_asexternal_lsa_tos_metric

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
