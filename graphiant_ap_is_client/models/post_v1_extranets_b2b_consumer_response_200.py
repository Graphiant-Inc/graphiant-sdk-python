from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_b2b_consumer_response_200_device_item import (
        PostV1ExtranetsB2BConsumerResponse200DeviceItem,
    )
    from ..models.post_v1_extranets_b2b_consumer_response_200_policy_item import (
        PostV1ExtranetsB2BConsumerResponse200PolicyItem,
    )
    from ..models.post_v1_extranets_b2b_consumer_response_200_site_information_item import (
        PostV1ExtranetsB2BConsumerResponse200SiteInformationItem,
    )


T = TypeVar("T", bound="PostV1ExtranetsB2BConsumerResponse200")


@_attrs_define
class PostV1ExtranetsB2BConsumerResponse200:
    """
    Attributes:
        device (Union[Unset, list['PostV1ExtranetsB2BConsumerResponse200DeviceItem']]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        policy (Union[Unset, list['PostV1ExtranetsB2BConsumerResponse200PolicyItem']]):
        site_information (Union[Unset, list['PostV1ExtranetsB2BConsumerResponse200SiteInformationItem']]):
    """

    device: Union[Unset, list["PostV1ExtranetsB2BConsumerResponse200DeviceItem"]] = UNSET
    id: Union[Unset, str] = UNSET
    policy: Union[Unset, list["PostV1ExtranetsB2BConsumerResponse200PolicyItem"]] = UNSET
    site_information: Union[Unset, list["PostV1ExtranetsB2BConsumerResponse200SiteInformationItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device, Unset):
            device = []
            for device_item_data in self.device:
                device_item = device_item_data.to_dict()
                device.append(device_item)

        id = self.id

        policy: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = []
            for policy_item_data in self.policy:
                policy_item = policy_item_data.to_dict()
                policy.append(policy_item)

        site_information: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.site_information, Unset):
            site_information = []
            for site_information_item_data in self.site_information:
                site_information_item = site_information_item_data.to_dict()
                site_information.append(site_information_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if id is not UNSET:
            field_dict["id"] = id
        if policy is not UNSET:
            field_dict["policy"] = policy
        if site_information is not UNSET:
            field_dict["siteInformation"] = site_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_b2b_consumer_response_200_device_item import (
            PostV1ExtranetsB2BConsumerResponse200DeviceItem,
        )
        from ..models.post_v1_extranets_b2b_consumer_response_200_policy_item import (
            PostV1ExtranetsB2BConsumerResponse200PolicyItem,
        )
        from ..models.post_v1_extranets_b2b_consumer_response_200_site_information_item import (
            PostV1ExtranetsB2BConsumerResponse200SiteInformationItem,
        )

        d = src_dict.copy()
        device = []
        _device = d.pop("device", UNSET)
        for device_item_data in _device or []:
            device_item = PostV1ExtranetsB2BConsumerResponse200DeviceItem.from_dict(device_item_data)

            device.append(device_item)

        id = d.pop("id", UNSET)

        policy = []
        _policy = d.pop("policy", UNSET)
        for policy_item_data in _policy or []:
            policy_item = PostV1ExtranetsB2BConsumerResponse200PolicyItem.from_dict(policy_item_data)

            policy.append(policy_item)

        site_information = []
        _site_information = d.pop("siteInformation", UNSET)
        for site_information_item_data in _site_information or []:
            site_information_item = PostV1ExtranetsB2BConsumerResponse200SiteInformationItem.from_dict(
                site_information_item_data
            )

            site_information.append(site_information_item)

        post_v1_extranets_b2b_consumer_response_200 = cls(
            device=device,
            id=id,
            policy=policy,
            site_information=site_information,
        )

        post_v1_extranets_b2b_consumer_response_200.additional_properties = d
        return post_v1_extranets_b2b_consumer_response_200

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
