from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_site_circuits_bandwidth_site_id_body_selectors_item import (
        PostV2MonitoringSiteCircuitsBandwidthSiteIdBodySelectorsItem,
    )
    from ..models.post_v2_monitoring_site_circuits_bandwidth_site_id_body_time_window import (
        PostV2MonitoringSiteCircuitsBandwidthSiteIdBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV2MonitoringSiteCircuitsBandwidthSiteIdBody")


@_attrs_define
class PostV2MonitoringSiteCircuitsBandwidthSiteIdBody:
    """
    Attributes:
        selectors (Union[Unset, list['PostV2MonitoringSiteCircuitsBandwidthSiteIdBodySelectorsItem']]):
        time_window (Union[Unset, PostV2MonitoringSiteCircuitsBandwidthSiteIdBodyTimeWindow]):
    """

    selectors: Union[Unset, list["PostV2MonitoringSiteCircuitsBandwidthSiteIdBodySelectorsItem"]] = UNSET
    time_window: Union[Unset, "PostV2MonitoringSiteCircuitsBandwidthSiteIdBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selectors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.selectors, Unset):
            selectors = []
            for selectors_item_data in self.selectors:
                selectors_item = selectors_item_data.to_dict()
                selectors.append(selectors_item)

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selectors is not UNSET:
            field_dict["selectors"] = selectors
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_site_circuits_bandwidth_site_id_body_selectors_item import (
            PostV2MonitoringSiteCircuitsBandwidthSiteIdBodySelectorsItem,
        )
        from ..models.post_v2_monitoring_site_circuits_bandwidth_site_id_body_time_window import (
            PostV2MonitoringSiteCircuitsBandwidthSiteIdBodyTimeWindow,
        )

        d = src_dict.copy()
        selectors = []
        _selectors = d.pop("selectors", UNSET)
        for selectors_item_data in _selectors or []:
            selectors_item = PostV2MonitoringSiteCircuitsBandwidthSiteIdBodySelectorsItem.from_dict(selectors_item_data)

            selectors.append(selectors_item)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2MonitoringSiteCircuitsBandwidthSiteIdBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2MonitoringSiteCircuitsBandwidthSiteIdBodyTimeWindow.from_dict(_time_window)

        post_v2_monitoring_site_circuits_bandwidth_site_id_body = cls(
            selectors=selectors,
            time_window=time_window,
        )

        post_v2_monitoring_site_circuits_bandwidth_site_id_body.additional_properties = d
        return post_v2_monitoring_site_circuits_bandwidth_site_id_body

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
