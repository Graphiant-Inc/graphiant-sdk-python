from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_sites_site_id_response_200_site_created_at import PostV1SitesSiteIdResponse200SiteCreatedAt
    from ..models.post_v1_sites_site_id_response_200_site_devices_item import (
        PostV1SitesSiteIdResponse200SiteDevicesItem,
    )
    from ..models.post_v1_sites_site_id_response_200_site_location import PostV1SitesSiteIdResponse200SiteLocation
    from ..models.post_v1_sites_site_id_response_200_site_policy_tag import PostV1SitesSiteIdResponse200SitePolicyTag
    from ..models.post_v1_sites_site_id_response_200_site_updated_at import PostV1SitesSiteIdResponse200SiteUpdatedAt


T = TypeVar("T", bound="PostV1SitesSiteIdResponse200Site")


@_attrs_define
class PostV1SitesSiteIdResponse200Site:
    """
    Attributes:
        address (Union[Unset, str]):  Example: TYPE_STRING.
        created_at (Union[Unset, PostV1SitesSiteIdResponse200SiteCreatedAt]):
        devices (Union[Unset, list['PostV1SitesSiteIdResponse200SiteDevicesItem']]):
        edge_count (Union[Unset, str]):  Example: TYPE_UINT32.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        location (Union[Unset, PostV1SitesSiteIdResponse200SiteLocation]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        notes (Union[Unset, str]):  Example: TYPE_STRING.
        policy_reference_count (Union[Unset, str]):  Example: TYPE_UINT32.
        policy_tag (Union[Unset, PostV1SitesSiteIdResponse200SitePolicyTag]):
        segment_count (Union[Unset, str]):  Example: TYPE_UINT32.
        site_list_reference_count (Union[Unset, str]):  Example: TYPE_UINT32.
        tags (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        updated_at (Union[Unset, PostV1SitesSiteIdResponse200SiteUpdatedAt]):
    """

    address: Union[Unset, str] = UNSET
    created_at: Union[Unset, "PostV1SitesSiteIdResponse200SiteCreatedAt"] = UNSET
    devices: Union[Unset, list["PostV1SitesSiteIdResponse200SiteDevicesItem"]] = UNSET
    edge_count: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    location: Union[Unset, "PostV1SitesSiteIdResponse200SiteLocation"] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    policy_reference_count: Union[Unset, str] = UNSET
    policy_tag: Union[Unset, "PostV1SitesSiteIdResponse200SitePolicyTag"] = UNSET
    segment_count: Union[Unset, str] = UNSET
    site_list_reference_count: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    updated_at: Union[Unset, "PostV1SitesSiteIdResponse200SiteUpdatedAt"] = UNSET
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
        from ..models.post_v1_sites_site_id_response_200_site_created_at import (
            PostV1SitesSiteIdResponse200SiteCreatedAt,
        )
        from ..models.post_v1_sites_site_id_response_200_site_devices_item import (
            PostV1SitesSiteIdResponse200SiteDevicesItem,
        )
        from ..models.post_v1_sites_site_id_response_200_site_location import PostV1SitesSiteIdResponse200SiteLocation
        from ..models.post_v1_sites_site_id_response_200_site_policy_tag import (
            PostV1SitesSiteIdResponse200SitePolicyTag,
        )
        from ..models.post_v1_sites_site_id_response_200_site_updated_at import (
            PostV1SitesSiteIdResponse200SiteUpdatedAt,
        )

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, PostV1SitesSiteIdResponse200SiteCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = PostV1SitesSiteIdResponse200SiteCreatedAt.from_dict(_created_at)

        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = PostV1SitesSiteIdResponse200SiteDevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        edge_count = d.pop("edgeCount", UNSET)

        id = d.pop("id", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, PostV1SitesSiteIdResponse200SiteLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = PostV1SitesSiteIdResponse200SiteLocation.from_dict(_location)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        policy_reference_count = d.pop("policyReferenceCount", UNSET)

        _policy_tag = d.pop("policyTag", UNSET)
        policy_tag: Union[Unset, PostV1SitesSiteIdResponse200SitePolicyTag]
        if isinstance(_policy_tag, Unset):
            policy_tag = UNSET
        else:
            policy_tag = PostV1SitesSiteIdResponse200SitePolicyTag.from_dict(_policy_tag)

        segment_count = d.pop("segmentCount", UNSET)

        site_list_reference_count = d.pop("siteListReferenceCount", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, PostV1SitesSiteIdResponse200SiteUpdatedAt]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = PostV1SitesSiteIdResponse200SiteUpdatedAt.from_dict(_updated_at)

        post_v1_sites_site_id_response_200_site = cls(
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

        post_v1_sites_site_id_response_200_site.additional_properties = d
        return post_v1_sites_site_id_response_200_site

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
