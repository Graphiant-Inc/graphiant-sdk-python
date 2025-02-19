from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item import (
        PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItem,
    )


T = TypeVar("T", bound="PostV1GatewaysCloudProviderDetailsResponse200")


@_attrs_define
class PostV1GatewaysCloudProviderDetailsResponse200:
    """
    Attributes:
        aws_gateways (Union[Unset, list['PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItem']]):
    """

    aws_gateways: Union[Unset, list["PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_gateways: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.aws_gateways, Unset):
            aws_gateways = []
            for aws_gateways_item_data in self.aws_gateways:
                aws_gateways_item = aws_gateways_item_data.to_dict()
                aws_gateways.append(aws_gateways_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_gateways is not UNSET:
            field_dict["awsGateways"] = aws_gateways

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_gateways_cloud_provider_details_response_200_aws_gateways_item import (
            PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItem,
        )

        d = src_dict.copy()
        aws_gateways = []
        _aws_gateways = d.pop("awsGateways", UNSET)
        for aws_gateways_item_data in _aws_gateways or []:
            aws_gateways_item = PostV1GatewaysCloudProviderDetailsResponse200AwsGatewaysItem.from_dict(
                aws_gateways_item_data
            )

            aws_gateways.append(aws_gateways_item)

        post_v1_gateways_cloud_provider_details_response_200 = cls(
            aws_gateways=aws_gateways,
        )

        post_v1_gateways_cloud_provider_details_response_200.additional_properties = d
        return post_v1_gateways_cloud_provider_details_response_200

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
