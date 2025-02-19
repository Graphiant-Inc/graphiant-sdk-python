from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_bucketdetails_response_200_bucket_details import (
        PostV2AssuranceBucketdetailsResponse200BucketDetails,
    )


T = TypeVar("T", bound="PostV2AssuranceBucketdetailsResponse200")


@_attrs_define
class PostV2AssuranceBucketdetailsResponse200:
    """
    Attributes:
        bucket_details (Union[Unset, PostV2AssuranceBucketdetailsResponse200BucketDetails]):
    """

    bucket_details: Union[Unset, "PostV2AssuranceBucketdetailsResponse200BucketDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bucket_details, Unset):
            bucket_details = self.bucket_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_details is not UNSET:
            field_dict["bucketDetails"] = bucket_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_bucketdetails_response_200_bucket_details import (
            PostV2AssuranceBucketdetailsResponse200BucketDetails,
        )

        d = src_dict.copy()
        _bucket_details = d.pop("bucketDetails", UNSET)
        bucket_details: Union[Unset, PostV2AssuranceBucketdetailsResponse200BucketDetails]
        if isinstance(_bucket_details, Unset):
            bucket_details = UNSET
        else:
            bucket_details = PostV2AssuranceBucketdetailsResponse200BucketDetails.from_dict(_bucket_details)

        post_v2_assurance_bucketdetails_response_200 = cls(
            bucket_details=bucket_details,
        )

        post_v2_assurance_bucketdetails_response_200.additional_properties = d
        return post_v2_assurance_bucketdetails_response_200

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
