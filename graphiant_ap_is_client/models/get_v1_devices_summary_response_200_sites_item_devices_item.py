from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_summary_response_200_sites_item_devices_item_override_region import (
        GetV1DevicesSummaryResponse200SitesItemDevicesItemOverrideRegion,
    )
    from ..models.get_v1_devices_summary_response_200_sites_item_devices_item_region import (
        GetV1DevicesSummaryResponse200SitesItemDevicesItemRegion,
    )


T = TypeVar("T", bound="GetV1DevicesSummaryResponse200SitesItemDevicesItem")


@_attrs_define
class GetV1DevicesSummaryResponse200SitesItemDevicesItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        is_virtual (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        override_region (Union[Unset, GetV1DevicesSummaryResponse200SitesItemDevicesItemOverrideRegion]):
        platform_name (Union[Unset, str]):  Example: TYPE_STRING.
        region (Union[Unset, GetV1DevicesSummaryResponse200SitesItemDevicesItemRegion]):
        role (Union[Unset, str]):  Example: TYPE_ENUM.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    id: Union[Unset, str] = UNSET
    is_virtual: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    override_region: Union[Unset, "GetV1DevicesSummaryResponse200SitesItemDevicesItemOverrideRegion"] = UNSET
    platform_name: Union[Unset, str] = UNSET
    region: Union[Unset, "GetV1DevicesSummaryResponse200SitesItemDevicesItemRegion"] = UNSET
    role: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_virtual = self.is_virtual

        name = self.name

        override_region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override_region, Unset):
            override_region = self.override_region.to_dict()

        platform_name = self.platform_name

        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        role = self.role

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_virtual is not UNSET:
            field_dict["isVirtual"] = is_virtual
        if name is not UNSET:
            field_dict["name"] = name
        if override_region is not UNSET:
            field_dict["overrideRegion"] = override_region
        if platform_name is not UNSET:
            field_dict["platformName"] = platform_name
        if region is not UNSET:
            field_dict["region"] = region
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_summary_response_200_sites_item_devices_item_override_region import (
            GetV1DevicesSummaryResponse200SitesItemDevicesItemOverrideRegion,
        )
        from ..models.get_v1_devices_summary_response_200_sites_item_devices_item_region import (
            GetV1DevicesSummaryResponse200SitesItemDevicesItemRegion,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_virtual = d.pop("isVirtual", UNSET)

        name = d.pop("name", UNSET)

        _override_region = d.pop("overrideRegion", UNSET)
        override_region: Union[Unset, GetV1DevicesSummaryResponse200SitesItemDevicesItemOverrideRegion]
        if isinstance(_override_region, Unset):
            override_region = UNSET
        else:
            override_region = GetV1DevicesSummaryResponse200SitesItemDevicesItemOverrideRegion.from_dict(
                _override_region
            )

        platform_name = d.pop("platformName", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, GetV1DevicesSummaryResponse200SitesItemDevicesItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = GetV1DevicesSummaryResponse200SitesItemDevicesItemRegion.from_dict(_region)

        role = d.pop("role", UNSET)

        status = d.pop("status", UNSET)

        get_v1_devices_summary_response_200_sites_item_devices_item = cls(
            id=id,
            is_virtual=is_virtual,
            name=name,
            override_region=override_region,
            platform_name=platform_name,
            region=region,
            role=role,
            status=status,
        )

        get_v1_devices_summary_response_200_sites_item_devices_item.additional_properties = d
        return get_v1_devices_summary_response_200_sites_item_devices_item

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
