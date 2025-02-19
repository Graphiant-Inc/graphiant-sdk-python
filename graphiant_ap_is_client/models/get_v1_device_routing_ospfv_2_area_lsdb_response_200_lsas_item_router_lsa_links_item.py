from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa_links_item_tos_metric import (
        GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItemTosMetric,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItem")


@_attrs_define
class GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItem:
    """
    Attributes:
        link_data (Union[Unset, str]):  Example: TYPE_STRING.
        link_id (Union[Unset, str]):  Example: TYPE_STRING.
        link_type (Union[Unset, str]):  Example: TYPE_STRING.
        metric (Union[Unset, str]):  Example: TYPE_UINT32.
        tos_metric (Union[Unset, GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItemTosMetric]):
    """

    link_data: Union[Unset, str] = UNSET
    link_id: Union[Unset, str] = UNSET
    link_type: Union[Unset, str] = UNSET
    metric: Union[Unset, str] = UNSET
    tos_metric: Union[Unset, "GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItemTosMetric"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link_data = self.link_data

        link_id = self.link_id

        link_type = self.link_type

        metric = self.metric

        tos_metric: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tos_metric, Unset):
            tos_metric = self.tos_metric.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_data is not UNSET:
            field_dict["linkData"] = link_data
        if link_id is not UNSET:
            field_dict["linkId"] = link_id
        if link_type is not UNSET:
            field_dict["linkType"] = link_type
        if metric is not UNSET:
            field_dict["metric"] = metric
        if tos_metric is not UNSET:
            field_dict["tosMetric"] = tos_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa_links_item_tos_metric import (
            GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItemTosMetric,
        )

        d = src_dict.copy()
        link_data = d.pop("linkData", UNSET)

        link_id = d.pop("linkId", UNSET)

        link_type = d.pop("linkType", UNSET)

        metric = d.pop("metric", UNSET)

        _tos_metric = d.pop("tosMetric", UNSET)
        tos_metric: Union[Unset, GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItemTosMetric]
        if isinstance(_tos_metric, Unset):
            tos_metric = UNSET
        else:
            tos_metric = GetV1DeviceRoutingOspfv2AreaLsdbResponse200LsasItemRouterLsaLinksItemTosMetric.from_dict(
                _tos_metric
            )

        get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa_links_item = cls(
            link_data=link_data,
            link_id=link_id,
            link_type=link_type,
            metric=metric,
            tos_metric=tos_metric,
        )

        get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa_links_item.additional_properties = d
        return get_v1_device_routing_ospfv_2_area_lsdb_response_200_lsas_item_router_lsa_links_item

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
