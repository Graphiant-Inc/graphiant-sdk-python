from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item_vpcs_item_subnets_item import (
        PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItemSubnetsItem,
    )


T = TypeVar("T", bound="PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItem")


@_attrs_define
class PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_STRING.
        subnets (Union[Unset,
            list['PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItemSubnetsItem']]):
    """

    id: Union[Unset, str] = UNSET
    subnets: Union[
        Unset,
        list["PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItemSubnetsItem"],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subnets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subnets, Unset):
            subnets = []
            for subnets_item_data in self.subnets:
                subnets_item = subnets_item_data.to_dict()
                subnets.append(subnets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if subnets is not UNSET:
            field_dict["subnets"] = subnets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item_vpcs_item_subnets_item import (
            PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItemSubnetsItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        subnets = []
        _subnets = d.pop("subnets", UNSET)
        for subnets_item_data in _subnets or []:
            subnets_item = PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItemTransitGatewaysItemVpcsItemSubnetsItem.from_dict(
                subnets_item_data
            )

            subnets.append(subnets_item)

        post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item_vpcs_item = cls(
            id=id,
            subnets=subnets,
        )

        post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item_vpcs_item.additional_properties = d
        return post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item_transit_gateways_item_vpcs_item

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
