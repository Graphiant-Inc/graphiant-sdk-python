from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_cloud_provider_details_body_aws import PostV1GatewaysCloudProviderDetailsBodyAws


T = TypeVar("T", bound="PostV1GatewaysCloudProviderDetailsBody")


@_attrs_define
class PostV1GatewaysCloudProviderDetailsBody:
    """
    Attributes:
        aws (Union[Unset, PostV1GatewaysCloudProviderDetailsBodyAws]):
    """

    aws: Union[Unset, "PostV1GatewaysCloudProviderDetailsBodyAws"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws is not UNSET:
            field_dict["aws"] = aws

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_gateways_cloud_provider_details_body_aws import PostV1GatewaysCloudProviderDetailsBodyAws

        d = src_dict.copy()
        _aws = d.pop("aws", UNSET)
        aws: Union[Unset, PostV1GatewaysCloudProviderDetailsBodyAws]
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = PostV1GatewaysCloudProviderDetailsBodyAws.from_dict(_aws)

        post_v1_gateways_cloud_provider_details_body = cls(
            aws=aws,
        )

        post_v1_gateways_cloud_provider_details_body.additional_properties = d
        return post_v1_gateways_cloud_provider_details_body

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
