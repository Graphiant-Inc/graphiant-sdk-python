from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_version_body_configuration_metadata import PostV1VersionBodyConfigurationMetadata


T = TypeVar("T", bound="PostV1VersionBody")


@_attrs_define
class PostV1VersionBody:
    """
    Attributes:
        configuration_metadata (Union[Unset, PostV1VersionBodyConfigurationMetadata]):
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        version (Union[Unset, str]):  Example: TYPE_INT32.
    """

    configuration_metadata: Union[Unset, "PostV1VersionBodyConfigurationMetadata"] = UNSET
    device_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.configuration_metadata, Unset):
            configuration_metadata = self.configuration_metadata.to_dict()

        device_id = self.device_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_metadata is not UNSET:
            field_dict["configurationMetadata"] = configuration_metadata
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_version_body_configuration_metadata import PostV1VersionBodyConfigurationMetadata

        d = src_dict.copy()
        _configuration_metadata = d.pop("configurationMetadata", UNSET)
        configuration_metadata: Union[Unset, PostV1VersionBodyConfigurationMetadata]
        if isinstance(_configuration_metadata, Unset):
            configuration_metadata = UNSET
        else:
            configuration_metadata = PostV1VersionBodyConfigurationMetadata.from_dict(_configuration_metadata)

        device_id = d.pop("deviceId", UNSET)

        version = d.pop("version", UNSET)

        post_v1_version_body = cls(
            configuration_metadata=configuration_metadata,
            device_id=device_id,
            version=version,
        )

        post_v1_version_body.additional_properties = d
        return post_v1_version_body

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
