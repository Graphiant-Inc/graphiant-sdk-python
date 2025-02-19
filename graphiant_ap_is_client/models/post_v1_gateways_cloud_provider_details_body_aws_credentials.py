from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GatewaysCloudProviderDetailsBodyAwsCredentials")


@_attrs_define
class PostV1GatewaysCloudProviderDetailsBodyAwsCredentials:
    """
    Attributes:
        access_key_id (Union[Unset, str]):  Example: TYPE_STRING.
        secret_access_key (Union[Unset, str]):  Example: TYPE_STRING.
    """

    access_key_id: Union[Unset, str] = UNSET
    secret_access_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key_id is not UNSET:
            field_dict["accessKeyId"] = access_key_id
        if secret_access_key is not UNSET:
            field_dict["secretAccessKey"] = secret_access_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key_id = d.pop("accessKeyId", UNSET)

        secret_access_key = d.pop("secretAccessKey", UNSET)

        post_v1_gateways_cloud_provider_details_body_aws_credentials = cls(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
        )

        post_v1_gateways_cloud_provider_details_body_aws_credentials.additional_properties = d
        return post_v1_gateways_cloud_provider_details_body_aws_credentials

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
