from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_body_policy_auto import PostV1ExtranetsBodyPolicyAuto
    from ..models.post_v1_extranets_body_policy_branches import PostV1ExtranetsBodyPolicyBranches
    from ..models.post_v1_extranets_body_policy_host_prefix_set import PostV1ExtranetsBodyPolicyHostPrefixSet
    from ..models.post_v1_extranets_body_policy_manual import PostV1ExtranetsBodyPolicyManual
    from ..models.post_v1_extranets_body_policy_source import PostV1ExtranetsBodyPolicySource


T = TypeVar("T", bound="PostV1ExtranetsBodyPolicy")


@_attrs_define
class PostV1ExtranetsBodyPolicy:
    """
    Attributes:
        auto (Union[Unset, PostV1ExtranetsBodyPolicyAuto]):
        branches (Union[Unset, PostV1ExtranetsBodyPolicyBranches]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        host_prefix_set (Union[Unset, PostV1ExtranetsBodyPolicyHostPrefixSet]):
        manual (Union[Unset, PostV1ExtranetsBodyPolicyManual]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        shared_prefixes (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        shared_segment (Union[Unset, str]):  Example: TYPE_INT64.
        source (Union[Unset, PostV1ExtranetsBodyPolicySource]):
        target_segments (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    auto: Union[Unset, "PostV1ExtranetsBodyPolicyAuto"] = UNSET
    branches: Union[Unset, "PostV1ExtranetsBodyPolicyBranches"] = UNSET
    description: Union[Unset, str] = UNSET
    host_prefix_set: Union[Unset, "PostV1ExtranetsBodyPolicyHostPrefixSet"] = UNSET
    manual: Union[Unset, "PostV1ExtranetsBodyPolicyManual"] = UNSET
    name: Union[Unset, str] = UNSET
    shared_prefixes: Union[Unset, list[str]] = UNSET
    shared_segment: Union[Unset, str] = UNSET
    source: Union[Unset, "PostV1ExtranetsBodyPolicySource"] = UNSET
    target_segments: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auto, Unset):
            auto = self.auto.to_dict()

        branches: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.branches, Unset):
            branches = self.branches.to_dict()

        description = self.description

        host_prefix_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.host_prefix_set, Unset):
            host_prefix_set = self.host_prefix_set.to_dict()

        manual: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.manual, Unset):
            manual = self.manual.to_dict()

        name = self.name

        shared_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shared_prefixes, Unset):
            shared_prefixes = self.shared_prefixes

        shared_segment = self.shared_segment

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        target_segments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.target_segments, Unset):
            target_segments = self.target_segments

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto is not UNSET:
            field_dict["auto"] = auto
        if branches is not UNSET:
            field_dict["branches"] = branches
        if description is not UNSET:
            field_dict["description"] = description
        if host_prefix_set is not UNSET:
            field_dict["hostPrefixSet"] = host_prefix_set
        if manual is not UNSET:
            field_dict["manual"] = manual
        if name is not UNSET:
            field_dict["name"] = name
        if shared_prefixes is not UNSET:
            field_dict["sharedPrefixes"] = shared_prefixes
        if shared_segment is not UNSET:
            field_dict["sharedSegment"] = shared_segment
        if source is not UNSET:
            field_dict["source"] = source
        if target_segments is not UNSET:
            field_dict["targetSegments"] = target_segments
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_body_policy_auto import PostV1ExtranetsBodyPolicyAuto
        from ..models.post_v1_extranets_body_policy_branches import PostV1ExtranetsBodyPolicyBranches
        from ..models.post_v1_extranets_body_policy_host_prefix_set import PostV1ExtranetsBodyPolicyHostPrefixSet
        from ..models.post_v1_extranets_body_policy_manual import PostV1ExtranetsBodyPolicyManual
        from ..models.post_v1_extranets_body_policy_source import PostV1ExtranetsBodyPolicySource

        d = src_dict.copy()
        _auto = d.pop("auto", UNSET)
        auto: Union[Unset, PostV1ExtranetsBodyPolicyAuto]
        if isinstance(_auto, Unset):
            auto = UNSET
        else:
            auto = PostV1ExtranetsBodyPolicyAuto.from_dict(_auto)

        _branches = d.pop("branches", UNSET)
        branches: Union[Unset, PostV1ExtranetsBodyPolicyBranches]
        if isinstance(_branches, Unset):
            branches = UNSET
        else:
            branches = PostV1ExtranetsBodyPolicyBranches.from_dict(_branches)

        description = d.pop("description", UNSET)

        _host_prefix_set = d.pop("hostPrefixSet", UNSET)
        host_prefix_set: Union[Unset, PostV1ExtranetsBodyPolicyHostPrefixSet]
        if isinstance(_host_prefix_set, Unset):
            host_prefix_set = UNSET
        else:
            host_prefix_set = PostV1ExtranetsBodyPolicyHostPrefixSet.from_dict(_host_prefix_set)

        _manual = d.pop("manual", UNSET)
        manual: Union[Unset, PostV1ExtranetsBodyPolicyManual]
        if isinstance(_manual, Unset):
            manual = UNSET
        else:
            manual = PostV1ExtranetsBodyPolicyManual.from_dict(_manual)

        name = d.pop("name", UNSET)

        shared_prefixes = cast(list[str], d.pop("sharedPrefixes", UNSET))

        shared_segment = d.pop("sharedSegment", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, PostV1ExtranetsBodyPolicySource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PostV1ExtranetsBodyPolicySource.from_dict(_source)

        target_segments = cast(list[str], d.pop("targetSegments", UNSET))

        type_ = d.pop("type", UNSET)

        post_v1_extranets_body_policy = cls(
            auto=auto,
            branches=branches,
            description=description,
            host_prefix_set=host_prefix_set,
            manual=manual,
            name=name,
            shared_prefixes=shared_prefixes,
            shared_segment=shared_segment,
            source=source,
            target_segments=target_segments,
            type_=type_,
        )

        post_v1_extranets_body_policy.additional_properties = d
        return post_v1_extranets_body_policy

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
