from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_auth_gcs_body_api_key import PostV1AuthGcsBodyApiKey
    from ..models.post_v1_auth_gcs_body_gcs_name import PostV1AuthGcsBodyGcsName


T = TypeVar("T", bound="PostV1AuthGcsBody")


@_attrs_define
class PostV1AuthGcsBody:
    """
    Attributes:
        gcs_name (Union[Unset, PostV1AuthGcsBodyGcsName]):  Example: any.
        api_key (Union[Unset, PostV1AuthGcsBodyApiKey]):  Example: any.
    """

    gcs_name: Union[Unset, "PostV1AuthGcsBodyGcsName"] = UNSET
    api_key: Union[Unset, "PostV1AuthGcsBodyApiKey"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gcs_name: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gcs_name, Unset):
            gcs_name = self.gcs_name.to_dict()

        api_key: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.api_key, Unset):
            api_key = self.api_key.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gcs_name is not UNSET:
            field_dict["gcsName"] = gcs_name
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_auth_gcs_body_api_key import PostV1AuthGcsBodyApiKey
        from ..models.post_v1_auth_gcs_body_gcs_name import PostV1AuthGcsBodyGcsName

        d = src_dict.copy()
        _gcs_name = d.pop("gcsName", UNSET)
        gcs_name: Union[Unset, PostV1AuthGcsBodyGcsName]
        if isinstance(_gcs_name, Unset):
            gcs_name = UNSET
        else:
            gcs_name = PostV1AuthGcsBodyGcsName.from_dict(_gcs_name)

        _api_key = d.pop("apiKey", UNSET)
        api_key: Union[Unset, PostV1AuthGcsBodyApiKey]
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = PostV1AuthGcsBodyApiKey.from_dict(_api_key)

        post_v1_auth_gcs_body = cls(
            gcs_name=gcs_name,
            api_key=api_key,
        )

        post_v1_auth_gcs_body.additional_properties = d
        return post_v1_auth_gcs_body

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
