from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_summary_lsa_tos_metric import (
        GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemSummaryLsaTosMetric,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemSummaryLsa")


@_attrs_define
class GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemSummaryLsa:
    """
    Attributes:
        network_mask (Union[Unset, str]):  Example: TYPE_UINT32.
        tos_metric (Union[Unset, GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemSummaryLsaTosMetric]):
    """

    network_mask: Union[Unset, str] = UNSET
    tos_metric: Union[Unset, "GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemSummaryLsaTosMetric"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_mask = self.network_mask

        tos_metric: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tos_metric, Unset):
            tos_metric = self.tos_metric.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_mask is not UNSET:
            field_dict["networkMask"] = network_mask
        if tos_metric is not UNSET:
            field_dict["tosMetric"] = tos_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_summary_lsa_tos_metric import (
            GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemSummaryLsaTosMetric,
        )

        d = src_dict.copy()
        network_mask = d.pop("networkMask", UNSET)

        _tos_metric = d.pop("tosMetric", UNSET)
        tos_metric: Union[Unset, GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemSummaryLsaTosMetric]
        if isinstance(_tos_metric, Unset):
            tos_metric = UNSET
        else:
            tos_metric = GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemSummaryLsaTosMetric.from_dict(_tos_metric)

        get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_summary_lsa = cls(
            network_mask=network_mask,
            tos_metric=tos_metric,
        )

        get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_summary_lsa.additional_properties = d
        return get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_summary_lsa

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
