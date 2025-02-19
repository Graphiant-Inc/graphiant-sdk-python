from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_3_area_lsdb_response_200_lsas_item_asexternal_lsa_tos_metric import (
        GetV1DeviceRoutingOspfv3AreaLsdbResponse200LsasItemAsexternalLsaTosMetric,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv3AreaLsdbResponse200LsasItemAsexternalLsa")


@_attrs_define
class GetV1DeviceRoutingOspfv3AreaLsdbResponse200LsasItemAsexternalLsa:
    """
    Attributes:
        forwarding_address (Union[Unset, str]):  Example: TYPE_STRING.
        metric (Union[Unset, str]):  Example: TYPE_UINT32.
        metric_type (Union[Unset, str]):  Example: TYPE_STRING.
        network_mask (Union[Unset, str]):  Example: TYPE_UINT32.
        tag (Union[Unset, str]):  Example: TYPE_UINT32.
        tos_metric (Union[Unset, GetV1DeviceRoutingOspfv3AreaLsdbResponse200LsasItemAsexternalLsaTosMetric]):
    """

    forwarding_address: Union[Unset, str] = UNSET
    metric: Union[Unset, str] = UNSET
    metric_type: Union[Unset, str] = UNSET
    network_mask: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    tos_metric: Union[Unset, "GetV1DeviceRoutingOspfv3AreaLsdbResponse200LsasItemAsexternalLsaTosMetric"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forwarding_address = self.forwarding_address

        metric = self.metric

        metric_type = self.metric_type

        network_mask = self.network_mask

        tag = self.tag

        tos_metric: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tos_metric, Unset):
            tos_metric = self.tos_metric.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if forwarding_address is not UNSET:
            field_dict["forwardingAddress"] = forwarding_address
        if metric is not UNSET:
            field_dict["metric"] = metric
        if metric_type is not UNSET:
            field_dict["metricType"] = metric_type
        if network_mask is not UNSET:
            field_dict["networkMask"] = network_mask
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tos_metric is not UNSET:
            field_dict["tosMetric"] = tos_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_3_area_lsdb_response_200_lsas_item_asexternal_lsa_tos_metric import (
            GetV1DeviceRoutingOspfv3AreaLsdbResponse200LsasItemAsexternalLsaTosMetric,
        )

        d = src_dict.copy()
        forwarding_address = d.pop("forwardingAddress", UNSET)

        metric = d.pop("metric", UNSET)

        metric_type = d.pop("metricType", UNSET)

        network_mask = d.pop("networkMask", UNSET)

        tag = d.pop("tag", UNSET)

        _tos_metric = d.pop("tosMetric", UNSET)
        tos_metric: Union[Unset, GetV1DeviceRoutingOspfv3AreaLsdbResponse200LsasItemAsexternalLsaTosMetric]
        if isinstance(_tos_metric, Unset):
            tos_metric = UNSET
        else:
            tos_metric = GetV1DeviceRoutingOspfv3AreaLsdbResponse200LsasItemAsexternalLsaTosMetric.from_dict(
                _tos_metric
            )

        get_v1_device_routing_ospfv_3_area_lsdb_response_200_lsas_item_asexternal_lsa = cls(
            forwarding_address=forwarding_address,
            metric=metric,
            metric_type=metric_type,
            network_mask=network_mask,
            tag=tag,
            tos_metric=tos_metric,
        )

        get_v1_device_routing_ospfv_3_area_lsdb_response_200_lsas_item_asexternal_lsa.additional_properties = d
        return get_v1_device_routing_ospfv_3_area_lsdb_response_200_lsas_item_asexternal_lsa

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
