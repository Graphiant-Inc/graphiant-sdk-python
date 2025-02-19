from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_circuits_utilization_response_200_data_item_queue_utilization_item import (
        PostV2MonitoringCircuitsUtilizationResponse200DataItemQueueUtilizationItem,
    )
    from ..models.post_v2_monitoring_circuits_utilization_response_200_data_item_selector import (
        PostV2MonitoringCircuitsUtilizationResponse200DataItemSelector,
    )


T = TypeVar("T", bound="PostV2MonitoringCircuitsUtilizationResponse200DataItem")


@_attrs_define
class PostV2MonitoringCircuitsUtilizationResponse200DataItem:
    """
    Attributes:
        config_link_up_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        queue_utilization (Union[Unset,
            list['PostV2MonitoringCircuitsUtilizationResponse200DataItemQueueUtilizationItem']]):
        selector (Union[Unset, PostV2MonitoringCircuitsUtilizationResponse200DataItemSelector]):
    """

    config_link_up_speed_mbps: Union[Unset, str] = UNSET
    queue_utilization: Union[
        Unset, list["PostV2MonitoringCircuitsUtilizationResponse200DataItemQueueUtilizationItem"]
    ] = UNSET
    selector: Union[Unset, "PostV2MonitoringCircuitsUtilizationResponse200DataItemSelector"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_link_up_speed_mbps = self.config_link_up_speed_mbps

        queue_utilization: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.queue_utilization, Unset):
            queue_utilization = []
            for queue_utilization_item_data in self.queue_utilization:
                queue_utilization_item = queue_utilization_item_data.to_dict()
                queue_utilization.append(queue_utilization_item)

        selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_link_up_speed_mbps is not UNSET:
            field_dict["configLinkUpSpeedMbps"] = config_link_up_speed_mbps
        if queue_utilization is not UNSET:
            field_dict["queueUtilization"] = queue_utilization
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_circuits_utilization_response_200_data_item_queue_utilization_item import (
            PostV2MonitoringCircuitsUtilizationResponse200DataItemQueueUtilizationItem,
        )
        from ..models.post_v2_monitoring_circuits_utilization_response_200_data_item_selector import (
            PostV2MonitoringCircuitsUtilizationResponse200DataItemSelector,
        )

        d = src_dict.copy()
        config_link_up_speed_mbps = d.pop("configLinkUpSpeedMbps", UNSET)

        queue_utilization = []
        _queue_utilization = d.pop("queueUtilization", UNSET)
        for queue_utilization_item_data in _queue_utilization or []:
            queue_utilization_item = (
                PostV2MonitoringCircuitsUtilizationResponse200DataItemQueueUtilizationItem.from_dict(
                    queue_utilization_item_data
                )
            )

            queue_utilization.append(queue_utilization_item)

        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, PostV2MonitoringCircuitsUtilizationResponse200DataItemSelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = PostV2MonitoringCircuitsUtilizationResponse200DataItemSelector.from_dict(_selector)

        post_v2_monitoring_circuits_utilization_response_200_data_item = cls(
            config_link_up_speed_mbps=config_link_up_speed_mbps,
            queue_utilization=queue_utilization,
            selector=selector,
        )

        post_v2_monitoring_circuits_utilization_response_200_data_item.additional_properties = d
        return post_v2_monitoring_circuits_utilization_response_200_data_item

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
