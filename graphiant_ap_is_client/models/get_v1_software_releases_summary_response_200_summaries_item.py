from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_software_releases_summary_response_200_summaries_item_key import (
        GetV1SoftwareReleasesSummaryResponse200SummariesItemKey,
    )
    from ..models.get_v1_software_releases_summary_response_200_summaries_item_release_ts import (
        GetV1SoftwareReleasesSummaryResponse200SummariesItemReleaseTs,
    )


T = TypeVar("T", bound="GetV1SoftwareReleasesSummaryResponse200SummariesItem")


@_attrs_define
class GetV1SoftwareReleasesSummaryResponse200SummariesItem:
    """
    Attributes:
        key (Union[Unset, GetV1SoftwareReleasesSummaryResponse200SummariesItemKey]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        release (Union[Unset, str]):  Example: TYPE_ENUM.
        release_ts (Union[Unset, GetV1SoftwareReleasesSummaryResponse200SummariesItemReleaseTs]):
    """

    key: Union[Unset, "GetV1SoftwareReleasesSummaryResponse200SummariesItemKey"] = UNSET
    name: Union[Unset, str] = UNSET
    release: Union[Unset, str] = UNSET
    release_ts: Union[Unset, "GetV1SoftwareReleasesSummaryResponse200SummariesItemReleaseTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        name = self.name

        release = self.release

        release_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.release_ts, Unset):
            release_ts = self.release_ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if release is not UNSET:
            field_dict["release"] = release
        if release_ts is not UNSET:
            field_dict["releaseTs"] = release_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_software_releases_summary_response_200_summaries_item_key import (
            GetV1SoftwareReleasesSummaryResponse200SummariesItemKey,
        )
        from ..models.get_v1_software_releases_summary_response_200_summaries_item_release_ts import (
            GetV1SoftwareReleasesSummaryResponse200SummariesItemReleaseTs,
        )

        d = src_dict.copy()
        _key = d.pop("key", UNSET)
        key: Union[Unset, GetV1SoftwareReleasesSummaryResponse200SummariesItemKey]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = GetV1SoftwareReleasesSummaryResponse200SummariesItemKey.from_dict(_key)

        name = d.pop("name", UNSET)

        release = d.pop("release", UNSET)

        _release_ts = d.pop("releaseTs", UNSET)
        release_ts: Union[Unset, GetV1SoftwareReleasesSummaryResponse200SummariesItemReleaseTs]
        if isinstance(_release_ts, Unset):
            release_ts = UNSET
        else:
            release_ts = GetV1SoftwareReleasesSummaryResponse200SummariesItemReleaseTs.from_dict(_release_ts)

        get_v1_software_releases_summary_response_200_summaries_item = cls(
            key=key,
            name=name,
            release=release,
            release_ts=release_ts,
        )

        get_v1_software_releases_summary_response_200_summaries_item.additional_properties = d
        return get_v1_software_releases_summary_response_200_summaries_item

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
