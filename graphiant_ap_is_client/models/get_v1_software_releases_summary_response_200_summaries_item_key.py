from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1SoftwareReleasesSummaryResponse200SummariesItemKey")


@_attrs_define
class GetV1SoftwareReleasesSummaryResponse200SummariesItemKey:
    """
    Attributes:
        model (Union[Unset, str]):  Example: TYPE_UINT32.
        version (Union[Unset, str]):  Example: TYPE_STRING.
    """

    model: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        model = d.pop("model", UNSET)

        version = d.pop("version", UNSET)

        get_v1_software_releases_summary_response_200_summaries_item_key = cls(
            model=model,
            version=version,
        )

        get_v1_software_releases_summary_response_200_summaries_item_key.additional_properties = d
        return get_v1_software_releases_summary_response_200_summaries_item_key

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
