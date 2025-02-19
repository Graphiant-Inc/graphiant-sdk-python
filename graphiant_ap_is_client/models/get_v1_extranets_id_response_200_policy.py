from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_id_response_200_policy_auto import GetV1ExtranetsIdResponse200PolicyAuto
    from ..models.get_v1_extranets_id_response_200_policy_branches import GetV1ExtranetsIdResponse200PolicyBranches
    from ..models.get_v1_extranets_id_response_200_policy_created_at import GetV1ExtranetsIdResponse200PolicyCreatedAt
    from ..models.get_v1_extranets_id_response_200_policy_host_prefix_set import (
        GetV1ExtranetsIdResponse200PolicyHostPrefixSet,
    )
    from ..models.get_v1_extranets_id_response_200_policy_manual import GetV1ExtranetsIdResponse200PolicyManual
    from ..models.get_v1_extranets_id_response_200_policy_shared_segment import (
        GetV1ExtranetsIdResponse200PolicySharedSegment,
    )
    from ..models.get_v1_extranets_id_response_200_policy_source import GetV1ExtranetsIdResponse200PolicySource
    from ..models.get_v1_extranets_id_response_200_policy_target_segments_item import (
        GetV1ExtranetsIdResponse200PolicyTargetSegmentsItem,
    )
    from ..models.get_v1_extranets_id_response_200_policy_updated_at import GetV1ExtranetsIdResponse200PolicyUpdatedAt


T = TypeVar("T", bound="GetV1ExtranetsIdResponse200Policy")


@_attrs_define
class GetV1ExtranetsIdResponse200Policy:
    """
    Attributes:
        auto (Union[Unset, GetV1ExtranetsIdResponse200PolicyAuto]):
        branches (Union[Unset, GetV1ExtranetsIdResponse200PolicyBranches]):
        created_at (Union[Unset, GetV1ExtranetsIdResponse200PolicyCreatedAt]):
        created_by (Union[Unset, str]):  Example: TYPE_STRING.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        host_prefix_set (Union[Unset, GetV1ExtranetsIdResponse200PolicyHostPrefixSet]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        manual (Union[Unset, GetV1ExtranetsIdResponse200PolicyManual]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        shared_prefixes (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        shared_segment (Union[Unset, GetV1ExtranetsIdResponse200PolicySharedSegment]):
        source (Union[Unset, GetV1ExtranetsIdResponse200PolicySource]):
        target_segments (Union[Unset, list['GetV1ExtranetsIdResponse200PolicyTargetSegmentsItem']]):
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
        updated_at (Union[Unset, GetV1ExtranetsIdResponse200PolicyUpdatedAt]):
    """

    auto: Union[Unset, "GetV1ExtranetsIdResponse200PolicyAuto"] = UNSET
    branches: Union[Unset, "GetV1ExtranetsIdResponse200PolicyBranches"] = UNSET
    created_at: Union[Unset, "GetV1ExtranetsIdResponse200PolicyCreatedAt"] = UNSET
    created_by: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    host_prefix_set: Union[Unset, "GetV1ExtranetsIdResponse200PolicyHostPrefixSet"] = UNSET
    id: Union[Unset, str] = UNSET
    manual: Union[Unset, "GetV1ExtranetsIdResponse200PolicyManual"] = UNSET
    name: Union[Unset, str] = UNSET
    shared_prefixes: Union[Unset, list[str]] = UNSET
    shared_segment: Union[Unset, "GetV1ExtranetsIdResponse200PolicySharedSegment"] = UNSET
    source: Union[Unset, "GetV1ExtranetsIdResponse200PolicySource"] = UNSET
    target_segments: Union[Unset, list["GetV1ExtranetsIdResponse200PolicyTargetSegmentsItem"]] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, "GetV1ExtranetsIdResponse200PolicyUpdatedAt"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auto, Unset):
            auto = self.auto.to_dict()

        branches: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.branches, Unset):
            branches = self.branches.to_dict()

        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        created_by = self.created_by

        description = self.description

        host_prefix_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.host_prefix_set, Unset):
            host_prefix_set = self.host_prefix_set.to_dict()

        id = self.id

        manual: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.manual, Unset):
            manual = self.manual.to_dict()

        name = self.name

        shared_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shared_prefixes, Unset):
            shared_prefixes = self.shared_prefixes

        shared_segment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shared_segment, Unset):
            shared_segment = self.shared_segment.to_dict()

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        target_segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.target_segments, Unset):
            target_segments = []
            for target_segments_item_data in self.target_segments:
                target_segments_item = target_segments_item_data.to_dict()
                target_segments.append(target_segments_item)

        type_ = self.type_

        updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto is not UNSET:
            field_dict["auto"] = auto
        if branches is not UNSET:
            field_dict["branches"] = branches
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if host_prefix_set is not UNSET:
            field_dict["hostPrefixSet"] = host_prefix_set
        if id is not UNSET:
            field_dict["id"] = id
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
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_id_response_200_policy_auto import GetV1ExtranetsIdResponse200PolicyAuto
        from ..models.get_v1_extranets_id_response_200_policy_branches import GetV1ExtranetsIdResponse200PolicyBranches
        from ..models.get_v1_extranets_id_response_200_policy_created_at import (
            GetV1ExtranetsIdResponse200PolicyCreatedAt,
        )
        from ..models.get_v1_extranets_id_response_200_policy_host_prefix_set import (
            GetV1ExtranetsIdResponse200PolicyHostPrefixSet,
        )
        from ..models.get_v1_extranets_id_response_200_policy_manual import GetV1ExtranetsIdResponse200PolicyManual
        from ..models.get_v1_extranets_id_response_200_policy_shared_segment import (
            GetV1ExtranetsIdResponse200PolicySharedSegment,
        )
        from ..models.get_v1_extranets_id_response_200_policy_source import GetV1ExtranetsIdResponse200PolicySource
        from ..models.get_v1_extranets_id_response_200_policy_target_segments_item import (
            GetV1ExtranetsIdResponse200PolicyTargetSegmentsItem,
        )
        from ..models.get_v1_extranets_id_response_200_policy_updated_at import (
            GetV1ExtranetsIdResponse200PolicyUpdatedAt,
        )

        d = src_dict.copy()
        _auto = d.pop("auto", UNSET)
        auto: Union[Unset, GetV1ExtranetsIdResponse200PolicyAuto]
        if isinstance(_auto, Unset):
            auto = UNSET
        else:
            auto = GetV1ExtranetsIdResponse200PolicyAuto.from_dict(_auto)

        _branches = d.pop("branches", UNSET)
        branches: Union[Unset, GetV1ExtranetsIdResponse200PolicyBranches]
        if isinstance(_branches, Unset):
            branches = UNSET
        else:
            branches = GetV1ExtranetsIdResponse200PolicyBranches.from_dict(_branches)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1ExtranetsIdResponse200PolicyCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1ExtranetsIdResponse200PolicyCreatedAt.from_dict(_created_at)

        created_by = d.pop("createdBy", UNSET)

        description = d.pop("description", UNSET)

        _host_prefix_set = d.pop("hostPrefixSet", UNSET)
        host_prefix_set: Union[Unset, GetV1ExtranetsIdResponse200PolicyHostPrefixSet]
        if isinstance(_host_prefix_set, Unset):
            host_prefix_set = UNSET
        else:
            host_prefix_set = GetV1ExtranetsIdResponse200PolicyHostPrefixSet.from_dict(_host_prefix_set)

        id = d.pop("id", UNSET)

        _manual = d.pop("manual", UNSET)
        manual: Union[Unset, GetV1ExtranetsIdResponse200PolicyManual]
        if isinstance(_manual, Unset):
            manual = UNSET
        else:
            manual = GetV1ExtranetsIdResponse200PolicyManual.from_dict(_manual)

        name = d.pop("name", UNSET)

        shared_prefixes = cast(list[str], d.pop("sharedPrefixes", UNSET))

        _shared_segment = d.pop("sharedSegment", UNSET)
        shared_segment: Union[Unset, GetV1ExtranetsIdResponse200PolicySharedSegment]
        if isinstance(_shared_segment, Unset):
            shared_segment = UNSET
        else:
            shared_segment = GetV1ExtranetsIdResponse200PolicySharedSegment.from_dict(_shared_segment)

        _source = d.pop("source", UNSET)
        source: Union[Unset, GetV1ExtranetsIdResponse200PolicySource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = GetV1ExtranetsIdResponse200PolicySource.from_dict(_source)

        target_segments = []
        _target_segments = d.pop("targetSegments", UNSET)
        for target_segments_item_data in _target_segments or []:
            target_segments_item = GetV1ExtranetsIdResponse200PolicyTargetSegmentsItem.from_dict(
                target_segments_item_data
            )

            target_segments.append(target_segments_item)

        type_ = d.pop("type", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, GetV1ExtranetsIdResponse200PolicyUpdatedAt]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = GetV1ExtranetsIdResponse200PolicyUpdatedAt.from_dict(_updated_at)

        get_v1_extranets_id_response_200_policy = cls(
            auto=auto,
            branches=branches,
            created_at=created_at,
            created_by=created_by,
            description=description,
            host_prefix_set=host_prefix_set,
            id=id,
            manual=manual,
            name=name,
            shared_prefixes=shared_prefixes,
            shared_segment=shared_segment,
            source=source,
            target_segments=target_segments,
            type_=type_,
            updated_at=updated_at,
        )

        get_v1_extranets_id_response_200_policy.additional_properties = d
        return get_v1_extranets_id_response_200_policy

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
