from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_body_policy_source_prefix_set import PostV1ExtranetsBodyPolicySourcePrefixSet


T = TypeVar("T", bound="PostV1ExtranetsBodyPolicySource")


@_attrs_define
class PostV1ExtranetsBodyPolicySource:
    """
    Attributes:
        excluded_devices (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        prefix_set (Union[Unset, PostV1ExtranetsBodyPolicySourcePrefixSet]):
        sites (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
    """

    excluded_devices: Union[Unset, list[str]] = UNSET
    prefix_set: Union[Unset, "PostV1ExtranetsBodyPolicySourcePrefixSet"] = UNSET
    sites: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excluded_devices: Union[Unset, list[str]] = UNSET
        if not isinstance(self.excluded_devices, Unset):
            excluded_devices = self.excluded_devices

        prefix_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prefix_set, Unset):
            prefix_set = self.prefix_set.to_dict()

        sites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excluded_devices is not UNSET:
            field_dict["excludedDevices"] = excluded_devices
        if prefix_set is not UNSET:
            field_dict["prefixSet"] = prefix_set
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_body_policy_source_prefix_set import PostV1ExtranetsBodyPolicySourcePrefixSet

        d = src_dict.copy()
        excluded_devices = cast(list[str], d.pop("excludedDevices", UNSET))

        _prefix_set = d.pop("prefixSet", UNSET)
        prefix_set: Union[Unset, PostV1ExtranetsBodyPolicySourcePrefixSet]
        if isinstance(_prefix_set, Unset):
            prefix_set = UNSET
        else:
            prefix_set = PostV1ExtranetsBodyPolicySourcePrefixSet.from_dict(_prefix_set)

        sites = cast(list[str], d.pop("sites", UNSET))

        post_v1_extranets_body_policy_source = cls(
            excluded_devices=excluded_devices,
            prefix_set=prefix_set,
            sites=sites,
        )

        post_v1_extranets_body_policy_source.additional_properties = d
        return post_v1_extranets_body_policy_source

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
