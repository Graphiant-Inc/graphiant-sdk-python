from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_site_twamp_site_id_response_200_data_item_samples_item import (
        PostV2MonitoringSiteTwampSiteIdResponse200DataItemSamplesItem,
    )
    from ..models.post_v2_monitoring_site_twamp_site_id_response_200_data_item_selector import (
        PostV2MonitoringSiteTwampSiteIdResponse200DataItemSelector,
    )


T = TypeVar("T", bound="PostV2MonitoringSiteTwampSiteIdResponse200DataItem")


@_attrs_define
class PostV2MonitoringSiteTwampSiteIdResponse200DataItem:
    """
    Attributes:
        carrier (Union[Unset, str]):  Example: TYPE_STRING.
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        samples (Union[Unset, list['PostV2MonitoringSiteTwampSiteIdResponse200DataItemSamplesItem']]):
        selector (Union[Unset, PostV2MonitoringSiteTwampSiteIdResponse200DataItemSelector]):
    """

    carrier: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    samples: Union[Unset, list["PostV2MonitoringSiteTwampSiteIdResponse200DataItemSamplesItem"]] = UNSET
    selector: Union[Unset, "PostV2MonitoringSiteTwampSiteIdResponse200DataItemSelector"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier = self.carrier

        device_id = self.device_id

        samples: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.samples, Unset):
            samples = []
            for samples_item_data in self.samples:
                samples_item = samples_item_data.to_dict()
                samples.append(samples_item)

        selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if samples is not UNSET:
            field_dict["samples"] = samples
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_site_twamp_site_id_response_200_data_item_samples_item import (
            PostV2MonitoringSiteTwampSiteIdResponse200DataItemSamplesItem,
        )
        from ..models.post_v2_monitoring_site_twamp_site_id_response_200_data_item_selector import (
            PostV2MonitoringSiteTwampSiteIdResponse200DataItemSelector,
        )

        d = src_dict.copy()
        carrier = d.pop("carrier", UNSET)

        device_id = d.pop("deviceId", UNSET)

        samples = []
        _samples = d.pop("samples", UNSET)
        for samples_item_data in _samples or []:
            samples_item = PostV2MonitoringSiteTwampSiteIdResponse200DataItemSamplesItem.from_dict(samples_item_data)

            samples.append(samples_item)

        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, PostV2MonitoringSiteTwampSiteIdResponse200DataItemSelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = PostV2MonitoringSiteTwampSiteIdResponse200DataItemSelector.from_dict(_selector)

        post_v2_monitoring_site_twamp_site_id_response_200_data_item = cls(
            carrier=carrier,
            device_id=device_id,
            samples=samples,
            selector=selector,
        )

        post_v2_monitoring_site_twamp_site_id_response_200_data_item.additional_properties = d
        return post_v2_monitoring_site_twamp_site_id_response_200_data_item

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
