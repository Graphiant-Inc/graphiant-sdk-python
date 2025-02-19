from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_cloud_provider_details_body_aws_credentials import (
        PostV1GatewaysCloudProviderDetailsBodyAwsCredentials,
    )


T = TypeVar("T", bound="PostV1GatewaysCloudProviderDetailsBodyAws")


@_attrs_define
class PostV1GatewaysCloudProviderDetailsBodyAws:
    """
    Attributes:
        credentials (Union[Unset, PostV1GatewaysCloudProviderDetailsBodyAwsCredentials]):
        region (Union[Unset, str]):  Example: TYPE_STRING.
    """

    credentials: Union[Unset, "PostV1GatewaysCloudProviderDetailsBodyAwsCredentials"] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_gateways_cloud_provider_details_body_aws_credentials import (
            PostV1GatewaysCloudProviderDetailsBodyAwsCredentials,
        )

        d = src_dict.copy()
        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, PostV1GatewaysCloudProviderDetailsBodyAwsCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = PostV1GatewaysCloudProviderDetailsBodyAwsCredentials.from_dict(_credentials)

        region = d.pop("region", UNSET)

        post_v1_gateways_cloud_provider_details_body_aws = cls(
            credentials=credentials,
            region=region,
        )

        post_v1_gateways_cloud_provider_details_body_aws.additional_properties = d
        return post_v1_gateways_cloud_provider_details_body_aws

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
