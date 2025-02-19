from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_created_at import (
        GetV1ExtranetsIdResponse200PolicySourceSitesItemCreatedAt,
    )
    from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_devices_item import (
        GetV1ExtranetsIdResponse200PolicySourceSitesItemDevicesItem,
    )
    from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_location import (
        GetV1ExtranetsIdResponse200PolicySourceSitesItemLocation,
    )
    from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_policy_tag import (
        GetV1ExtranetsIdResponse200PolicySourceSitesItemPolicyTag,
    )
    from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_updated_at import (
        GetV1ExtranetsIdResponse200PolicySourceSitesItemUpdatedAt,
    )


T = TypeVar("T", bound="GetV1ExtranetsIdResponse200PolicySourceSitesItem")


@_attrs_define
class GetV1ExtranetsIdResponse200PolicySourceSitesItem:
    """
    Attributes:
        address (Union[Unset, str]):  Example: TYPE_STRING.
        created_at (Union[Unset, GetV1ExtranetsIdResponse200PolicySourceSitesItemCreatedAt]):
        devices (Union[Unset, list['GetV1ExtranetsIdResponse200PolicySourceSitesItemDevicesItem']]):
        edge_count (Union[Unset, str]):  Example: TYPE_UINT32.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        location (Union[Unset, GetV1ExtranetsIdResponse200PolicySourceSitesItemLocation]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        notes (Union[Unset, str]):  Example: TYPE_STRING.
        policy_reference_count (Union[Unset, str]):  Example: TYPE_UINT32.
        policy_tag (Union[Unset, GetV1ExtranetsIdResponse200PolicySourceSitesItemPolicyTag]):
        segment_count (Union[Unset, str]):  Example: TYPE_UINT32.
        site_list_reference_count (Union[Unset, str]):  Example: TYPE_UINT32.
        tags (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        updated_at (Union[Unset, GetV1ExtranetsIdResponse200PolicySourceSitesItemUpdatedAt]):
    """

    address: Union[Unset, str] = UNSET
    created_at: Union[Unset, "GetV1ExtranetsIdResponse200PolicySourceSitesItemCreatedAt"] = UNSET
    devices: Union[Unset, list["GetV1ExtranetsIdResponse200PolicySourceSitesItemDevicesItem"]] = UNSET
    edge_count: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    location: Union[Unset, "GetV1ExtranetsIdResponse200PolicySourceSitesItemLocation"] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    policy_reference_count: Union[Unset, str] = UNSET
    policy_tag: Union[Unset, "GetV1ExtranetsIdResponse200PolicySourceSitesItemPolicyTag"] = UNSET
    segment_count: Union[Unset, str] = UNSET
    site_list_reference_count: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    updated_at: Union[Unset, "GetV1ExtranetsIdResponse200PolicySourceSitesItemUpdatedAt"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        edge_count = self.edge_count

        id = self.id

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        name = self.name

        notes = self.notes

        policy_reference_count = self.policy_reference_count

        policy_tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy_tag, Unset):
            policy_tag = self.policy_tag.to_dict()

        segment_count = self.segment_count

        site_list_reference_count = self.site_list_reference_count

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if devices is not UNSET:
            field_dict["devices"] = devices
        if edge_count is not UNSET:
            field_dict["edgeCount"] = edge_count
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if policy_reference_count is not UNSET:
            field_dict["policyReferenceCount"] = policy_reference_count
        if policy_tag is not UNSET:
            field_dict["policyTag"] = policy_tag
        if segment_count is not UNSET:
            field_dict["segmentCount"] = segment_count
        if site_list_reference_count is not UNSET:
            field_dict["siteListReferenceCount"] = site_list_reference_count
        if tags is not UNSET:
            field_dict["tags"] = tags
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_created_at import (
            GetV1ExtranetsIdResponse200PolicySourceSitesItemCreatedAt,
        )
        from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_devices_item import (
            GetV1ExtranetsIdResponse200PolicySourceSitesItemDevicesItem,
        )
        from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_location import (
            GetV1ExtranetsIdResponse200PolicySourceSitesItemLocation,
        )
        from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_policy_tag import (
            GetV1ExtranetsIdResponse200PolicySourceSitesItemPolicyTag,
        )
        from ..models.get_v1_extranets_id_response_200_policy_source_sites_item_updated_at import (
            GetV1ExtranetsIdResponse200PolicySourceSitesItemUpdatedAt,
        )

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1ExtranetsIdResponse200PolicySourceSitesItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1ExtranetsIdResponse200PolicySourceSitesItemCreatedAt.from_dict(_created_at)

        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = GetV1ExtranetsIdResponse200PolicySourceSitesItemDevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        edge_count = d.pop("edgeCount", UNSET)

        id = d.pop("id", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, GetV1ExtranetsIdResponse200PolicySourceSitesItemLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = GetV1ExtranetsIdResponse200PolicySourceSitesItemLocation.from_dict(_location)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        policy_reference_count = d.pop("policyReferenceCount", UNSET)

        _policy_tag = d.pop("policyTag", UNSET)
        policy_tag: Union[Unset, GetV1ExtranetsIdResponse200PolicySourceSitesItemPolicyTag]
        if isinstance(_policy_tag, Unset):
            policy_tag = UNSET
        else:
            policy_tag = GetV1ExtranetsIdResponse200PolicySourceSitesItemPolicyTag.from_dict(_policy_tag)

        segment_count = d.pop("segmentCount", UNSET)

        site_list_reference_count = d.pop("siteListReferenceCount", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, GetV1ExtranetsIdResponse200PolicySourceSitesItemUpdatedAt]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = GetV1ExtranetsIdResponse200PolicySourceSitesItemUpdatedAt.from_dict(_updated_at)

        get_v1_extranets_id_response_200_policy_source_sites_item = cls(
            address=address,
            created_at=created_at,
            devices=devices,
            edge_count=edge_count,
            id=id,
            location=location,
            name=name,
            notes=notes,
            policy_reference_count=policy_reference_count,
            policy_tag=policy_tag,
            segment_count=segment_count,
            site_list_reference_count=site_list_reference_count,
            tags=tags,
            updated_at=updated_at,
        )

        get_v1_extranets_id_response_200_policy_source_sites_item.additional_properties = d
        return get_v1_extranets_id_response_200_policy_source_sites_item

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
