from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryRunningVersion")


@_attrs_define
class GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummaryRunningVersion:
    """
    Attributes:
        name (Union[Unset, str]):  Example: TYPE_STRING.
        release (Union[Unset, str]):  Example: TYPE_ENUM.
        version (Union[Unset, str]):  Example: TYPE_STRING.
    """

    name: Union[Unset, str] = UNSET
    release: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        release = self.release

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if release is not UNSET:
            field_dict["release"] = release
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        release = d.pop("release", UNSET)

        version = d.pop("version", UNSET)

        get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_running_version = cls(
            name=name,
            release=release,
            version=version,
        )

        get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_running_version.additional_properties = d
        return get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary_running_version

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
