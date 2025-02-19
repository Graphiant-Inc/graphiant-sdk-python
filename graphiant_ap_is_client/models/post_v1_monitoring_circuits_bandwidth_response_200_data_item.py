from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_monitoring_circuits_bandwidth_response_200_data_item_dl_bw_kbps_samples_item import (
        PostV1MonitoringCircuitsBandwidthResponse200DataItemDlBwKbpsSamplesItem,
    )
    from ..models.post_v1_monitoring_circuits_bandwidth_response_200_data_item_selector import (
        PostV1MonitoringCircuitsBandwidthResponse200DataItemSelector,
    )
    from ..models.post_v1_monitoring_circuits_bandwidth_response_200_data_item_ul_bw_kbps_samples_item import (
        PostV1MonitoringCircuitsBandwidthResponse200DataItemUlBwKbpsSamplesItem,
    )


T = TypeVar("T", bound="PostV1MonitoringCircuitsBandwidthResponse200DataItem")


@_attrs_define
class PostV1MonitoringCircuitsBandwidthResponse200DataItem:
    """
    Attributes:
        carrier (Union[Unset, str]):  Example: TYPE_STRING.
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        dl_bw_kbps_samples (Union[Unset,
            list['PostV1MonitoringCircuitsBandwidthResponse200DataItemDlBwKbpsSamplesItem']]):
        selector (Union[Unset, PostV1MonitoringCircuitsBandwidthResponse200DataItemSelector]):
        ul_bw_kbps_samples (Union[Unset,
            list['PostV1MonitoringCircuitsBandwidthResponse200DataItemUlBwKbpsSamplesItem']]):
    """

    carrier: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    dl_bw_kbps_samples: Union[
        Unset, list["PostV1MonitoringCircuitsBandwidthResponse200DataItemDlBwKbpsSamplesItem"]
    ] = UNSET
    selector: Union[Unset, "PostV1MonitoringCircuitsBandwidthResponse200DataItemSelector"] = UNSET
    ul_bw_kbps_samples: Union[
        Unset, list["PostV1MonitoringCircuitsBandwidthResponse200DataItemUlBwKbpsSamplesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier = self.carrier

        device_id = self.device_id

        dl_bw_kbps_samples: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dl_bw_kbps_samples, Unset):
            dl_bw_kbps_samples = []
            for dl_bw_kbps_samples_item_data in self.dl_bw_kbps_samples:
                dl_bw_kbps_samples_item = dl_bw_kbps_samples_item_data.to_dict()
                dl_bw_kbps_samples.append(dl_bw_kbps_samples_item)

        selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        ul_bw_kbps_samples: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ul_bw_kbps_samples, Unset):
            ul_bw_kbps_samples = []
            for ul_bw_kbps_samples_item_data in self.ul_bw_kbps_samples:
                ul_bw_kbps_samples_item = ul_bw_kbps_samples_item_data.to_dict()
                ul_bw_kbps_samples.append(ul_bw_kbps_samples_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if dl_bw_kbps_samples is not UNSET:
            field_dict["dlBwKbpsSamples"] = dl_bw_kbps_samples
        if selector is not UNSET:
            field_dict["selector"] = selector
        if ul_bw_kbps_samples is not UNSET:
            field_dict["ulBwKbpsSamples"] = ul_bw_kbps_samples

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_monitoring_circuits_bandwidth_response_200_data_item_dl_bw_kbps_samples_item import (
            PostV1MonitoringCircuitsBandwidthResponse200DataItemDlBwKbpsSamplesItem,
        )
        from ..models.post_v1_monitoring_circuits_bandwidth_response_200_data_item_selector import (
            PostV1MonitoringCircuitsBandwidthResponse200DataItemSelector,
        )
        from ..models.post_v1_monitoring_circuits_bandwidth_response_200_data_item_ul_bw_kbps_samples_item import (
            PostV1MonitoringCircuitsBandwidthResponse200DataItemUlBwKbpsSamplesItem,
        )

        d = src_dict.copy()
        carrier = d.pop("carrier", UNSET)

        device_id = d.pop("deviceId", UNSET)

        dl_bw_kbps_samples = []
        _dl_bw_kbps_samples = d.pop("dlBwKbpsSamples", UNSET)
        for dl_bw_kbps_samples_item_data in _dl_bw_kbps_samples or []:
            dl_bw_kbps_samples_item = PostV1MonitoringCircuitsBandwidthResponse200DataItemDlBwKbpsSamplesItem.from_dict(
                dl_bw_kbps_samples_item_data
            )

            dl_bw_kbps_samples.append(dl_bw_kbps_samples_item)

        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, PostV1MonitoringCircuitsBandwidthResponse200DataItemSelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = PostV1MonitoringCircuitsBandwidthResponse200DataItemSelector.from_dict(_selector)

        ul_bw_kbps_samples = []
        _ul_bw_kbps_samples = d.pop("ulBwKbpsSamples", UNSET)
        for ul_bw_kbps_samples_item_data in _ul_bw_kbps_samples or []:
            ul_bw_kbps_samples_item = PostV1MonitoringCircuitsBandwidthResponse200DataItemUlBwKbpsSamplesItem.from_dict(
                ul_bw_kbps_samples_item_data
            )

            ul_bw_kbps_samples.append(ul_bw_kbps_samples_item)

        post_v1_monitoring_circuits_bandwidth_response_200_data_item = cls(
            carrier=carrier,
            device_id=device_id,
            dl_bw_kbps_samples=dl_bw_kbps_samples,
            selector=selector,
            ul_bw_kbps_samples=ul_bw_kbps_samples,
        )

        post_v1_monitoring_circuits_bandwidth_response_200_data_item.additional_properties = d
        return post_v1_monitoring_circuits_bandwidth_response_200_data_item

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
