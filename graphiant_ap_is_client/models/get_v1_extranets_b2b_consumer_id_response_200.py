from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item import (
        GetV1ExtranetsB2BConsumerIdResponse200PolicyItem,
    )
    from ..models.get_v1_extranets_b2b_consumer_id_response_200_site_information_item import (
        GetV1ExtranetsB2BConsumerIdResponse200SiteInformationItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BConsumerIdResponse200")


@_attrs_define
class GetV1ExtranetsB2BConsumerIdResponse200:
    """
    Attributes:
        consumer_id (Union[Unset, str]):  Example: TYPE_INT64.
        policy (Union[Unset, list['GetV1ExtranetsB2BConsumerIdResponse200PolicyItem']]):
        service_name (Union[Unset, str]):  Example: TYPE_STRING.
        site_information (Union[Unset, list['GetV1ExtranetsB2BConsumerIdResponse200SiteInformationItem']]):
    """

    consumer_id: Union[Unset, str] = UNSET
    policy: Union[Unset, list["GetV1ExtranetsB2BConsumerIdResponse200PolicyItem"]] = UNSET
    service_name: Union[Unset, str] = UNSET
    site_information: Union[Unset, list["GetV1ExtranetsB2BConsumerIdResponse200SiteInformationItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consumer_id = self.consumer_id

        policy: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = []
            for policy_item_data in self.policy:
                policy_item = policy_item_data.to_dict()
                policy.append(policy_item)

        service_name = self.service_name

        site_information: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.site_information, Unset):
            site_information = []
            for site_information_item_data in self.site_information:
                site_information_item = site_information_item_data.to_dict()
                site_information.append(site_information_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumer_id is not UNSET:
            field_dict["consumerId"] = consumer_id
        if policy is not UNSET:
            field_dict["policy"] = policy
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if site_information is not UNSET:
            field_dict["siteInformation"] = site_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_consumer_id_response_200_policy_item import (
            GetV1ExtranetsB2BConsumerIdResponse200PolicyItem,
        )
        from ..models.get_v1_extranets_b2b_consumer_id_response_200_site_information_item import (
            GetV1ExtranetsB2BConsumerIdResponse200SiteInformationItem,
        )

        d = src_dict.copy()
        consumer_id = d.pop("consumerId", UNSET)

        policy = []
        _policy = d.pop("policy", UNSET)
        for policy_item_data in _policy or []:
            policy_item = GetV1ExtranetsB2BConsumerIdResponse200PolicyItem.from_dict(policy_item_data)

            policy.append(policy_item)

        service_name = d.pop("serviceName", UNSET)

        site_information = []
        _site_information = d.pop("siteInformation", UNSET)
        for site_information_item_data in _site_information or []:
            site_information_item = GetV1ExtranetsB2BConsumerIdResponse200SiteInformationItem.from_dict(
                site_information_item_data
            )

            site_information.append(site_information_item)

        get_v1_extranets_b2b_consumer_id_response_200 = cls(
            consumer_id=consumer_id,
            policy=policy,
            service_name=service_name,
            site_information=site_information,
        )

        get_v1_extranets_b2b_consumer_id_response_200.additional_properties = d
        return get_v1_extranets_b2b_consumer_id_response_200

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
