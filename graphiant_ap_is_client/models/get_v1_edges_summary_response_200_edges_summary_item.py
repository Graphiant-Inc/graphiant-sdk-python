from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_assigned_on import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemAssignedOn,
    )
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_first_appeared_on import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemFirstAppearedOn,
    )
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_last_booted_at import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemLastBootedAt,
    )
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_location import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemLocation,
    )
    from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary import (
        GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummary,
    )


T = TypeVar("T", bound="GetV1EdgesSummaryResponse200EdgesSummaryItem")


@_attrs_define
class GetV1EdgesSummaryResponse200EdgesSummaryItem:
    """
    Attributes:
        assigned_on (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemAssignedOn]):
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        discovered_location (Union[Unset, str]):  Example: TYPE_STRING.
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        enterprise_name (Union[Unset, str]):  Example: TYPE_STRING.
        first_appeared_on (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemFirstAppearedOn]):
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        ip_detected (Union[Unset, str]):  Example: TYPE_STRING.
        is_hardware (Union[Unset, str]):  Example: TYPE_BOOL.
        is_new (Union[Unset, str]):  Example: TYPE_BOOL.
        is_requested (Union[Unset, str]):  Example: TYPE_BOOL.
        last_booted_at (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemLastBootedAt]):
        location (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemLocation]):
        model (Union[Unset, str]):  Example: TYPE_STRING.
        override_region (Union[Unset, str]):  Example: TYPE_STRING.
        parent_enterprise_name (Union[Unset, str]):  Example: TYPE_STRING.
        portal_status (Union[Unset, str]):  Example: TYPE_ENUM.
        role (Union[Unset, str]):  Example: TYPE_ENUM.
        serial_num (Union[Unset, str]):  Example: TYPE_STRING.
        site (Union[Unset, str]):  Example: TYPE_STRING.
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        stale (Union[Unset, str]):  Example: TYPE_BOOL.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        sw_name (Union[Unset, str]):  Example: TYPE_STRING.
        sw_version (Union[Unset, str]):  Example: TYPE_STRING.
        tt_conn_count (Union[Unset, str]):  Example: TYPE_UINT32.
        upgrade_summary (Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummary]):
    """

    assigned_on: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemAssignedOn"] = UNSET
    device_id: Union[Unset, str] = UNSET
    discovered_location: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    enterprise_name: Union[Unset, str] = UNSET
    first_appeared_on: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemFirstAppearedOn"] = UNSET
    hostname: Union[Unset, str] = UNSET
    ip_detected: Union[Unset, str] = UNSET
    is_hardware: Union[Unset, str] = UNSET
    is_new: Union[Unset, str] = UNSET
    is_requested: Union[Unset, str] = UNSET
    last_booted_at: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemLastBootedAt"] = UNSET
    location: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemLocation"] = UNSET
    model: Union[Unset, str] = UNSET
    override_region: Union[Unset, str] = UNSET
    parent_enterprise_name: Union[Unset, str] = UNSET
    portal_status: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    serial_num: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    stale: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    sw_name: Union[Unset, str] = UNSET
    sw_version: Union[Unset, str] = UNSET
    tt_conn_count: Union[Unset, str] = UNSET
    upgrade_summary: Union[Unset, "GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummary"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_on: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assigned_on, Unset):
            assigned_on = self.assigned_on.to_dict()

        device_id = self.device_id

        discovered_location = self.discovered_location

        enterprise_id = self.enterprise_id

        enterprise_name = self.enterprise_name

        first_appeared_on: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_appeared_on, Unset):
            first_appeared_on = self.first_appeared_on.to_dict()

        hostname = self.hostname

        ip_detected = self.ip_detected

        is_hardware = self.is_hardware

        is_new = self.is_new

        is_requested = self.is_requested

        last_booted_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_booted_at, Unset):
            last_booted_at = self.last_booted_at.to_dict()

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        model = self.model

        override_region = self.override_region

        parent_enterprise_name = self.parent_enterprise_name

        portal_status = self.portal_status

        role = self.role

        serial_num = self.serial_num

        site = self.site

        site_id = self.site_id

        stale = self.stale

        status = self.status

        sw_name = self.sw_name

        sw_version = self.sw_version

        tt_conn_count = self.tt_conn_count

        upgrade_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.upgrade_summary, Unset):
            upgrade_summary = self.upgrade_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_on is not UNSET:
            field_dict["assignedOn"] = assigned_on
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if discovered_location is not UNSET:
            field_dict["discoveredLocation"] = discovered_location
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if enterprise_name is not UNSET:
            field_dict["enterpriseName"] = enterprise_name
        if first_appeared_on is not UNSET:
            field_dict["firstAppearedOn"] = first_appeared_on
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ip_detected is not UNSET:
            field_dict["ipDetected"] = ip_detected
        if is_hardware is not UNSET:
            field_dict["isHardware"] = is_hardware
        if is_new is not UNSET:
            field_dict["isNew"] = is_new
        if is_requested is not UNSET:
            field_dict["isRequested"] = is_requested
        if last_booted_at is not UNSET:
            field_dict["lastBootedAt"] = last_booted_at
        if location is not UNSET:
            field_dict["location"] = location
        if model is not UNSET:
            field_dict["model"] = model
        if override_region is not UNSET:
            field_dict["overrideRegion"] = override_region
        if parent_enterprise_name is not UNSET:
            field_dict["parentEnterpriseName"] = parent_enterprise_name
        if portal_status is not UNSET:
            field_dict["portalStatus"] = portal_status
        if role is not UNSET:
            field_dict["role"] = role
        if serial_num is not UNSET:
            field_dict["serialNum"] = serial_num
        if site is not UNSET:
            field_dict["site"] = site
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if stale is not UNSET:
            field_dict["stale"] = stale
        if status is not UNSET:
            field_dict["status"] = status
        if sw_name is not UNSET:
            field_dict["swName"] = sw_name
        if sw_version is not UNSET:
            field_dict["swVersion"] = sw_version
        if tt_conn_count is not UNSET:
            field_dict["ttConnCount"] = tt_conn_count
        if upgrade_summary is not UNSET:
            field_dict["upgradeSummary"] = upgrade_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_assigned_on import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemAssignedOn,
        )
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_first_appeared_on import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemFirstAppearedOn,
        )
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_last_booted_at import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemLastBootedAt,
        )
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_location import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemLocation,
        )
        from ..models.get_v1_edges_summary_response_200_edges_summary_item_upgrade_summary import (
            GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummary,
        )

        d = src_dict.copy()
        _assigned_on = d.pop("assignedOn", UNSET)
        assigned_on: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemAssignedOn]
        if isinstance(_assigned_on, Unset):
            assigned_on = UNSET
        else:
            assigned_on = GetV1EdgesSummaryResponse200EdgesSummaryItemAssignedOn.from_dict(_assigned_on)

        device_id = d.pop("deviceId", UNSET)

        discovered_location = d.pop("discoveredLocation", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        enterprise_name = d.pop("enterpriseName", UNSET)

        _first_appeared_on = d.pop("firstAppearedOn", UNSET)
        first_appeared_on: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemFirstAppearedOn]
        if isinstance(_first_appeared_on, Unset):
            first_appeared_on = UNSET
        else:
            first_appeared_on = GetV1EdgesSummaryResponse200EdgesSummaryItemFirstAppearedOn.from_dict(
                _first_appeared_on
            )

        hostname = d.pop("hostname", UNSET)

        ip_detected = d.pop("ipDetected", UNSET)

        is_hardware = d.pop("isHardware", UNSET)

        is_new = d.pop("isNew", UNSET)

        is_requested = d.pop("isRequested", UNSET)

        _last_booted_at = d.pop("lastBootedAt", UNSET)
        last_booted_at: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemLastBootedAt]
        if isinstance(_last_booted_at, Unset):
            last_booted_at = UNSET
        else:
            last_booted_at = GetV1EdgesSummaryResponse200EdgesSummaryItemLastBootedAt.from_dict(_last_booted_at)

        _location = d.pop("location", UNSET)
        location: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = GetV1EdgesSummaryResponse200EdgesSummaryItemLocation.from_dict(_location)

        model = d.pop("model", UNSET)

        override_region = d.pop("overrideRegion", UNSET)

        parent_enterprise_name = d.pop("parentEnterpriseName", UNSET)

        portal_status = d.pop("portalStatus", UNSET)

        role = d.pop("role", UNSET)

        serial_num = d.pop("serialNum", UNSET)

        site = d.pop("site", UNSET)

        site_id = d.pop("siteId", UNSET)

        stale = d.pop("stale", UNSET)

        status = d.pop("status", UNSET)

        sw_name = d.pop("swName", UNSET)

        sw_version = d.pop("swVersion", UNSET)

        tt_conn_count = d.pop("ttConnCount", UNSET)

        _upgrade_summary = d.pop("upgradeSummary", UNSET)
        upgrade_summary: Union[Unset, GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummary]
        if isinstance(_upgrade_summary, Unset):
            upgrade_summary = UNSET
        else:
            upgrade_summary = GetV1EdgesSummaryResponse200EdgesSummaryItemUpgradeSummary.from_dict(_upgrade_summary)

        get_v1_edges_summary_response_200_edges_summary_item = cls(
            assigned_on=assigned_on,
            device_id=device_id,
            discovered_location=discovered_location,
            enterprise_id=enterprise_id,
            enterprise_name=enterprise_name,
            first_appeared_on=first_appeared_on,
            hostname=hostname,
            ip_detected=ip_detected,
            is_hardware=is_hardware,
            is_new=is_new,
            is_requested=is_requested,
            last_booted_at=last_booted_at,
            location=location,
            model=model,
            override_region=override_region,
            parent_enterprise_name=parent_enterprise_name,
            portal_status=portal_status,
            role=role,
            serial_num=serial_num,
            site=site,
            site_id=site_id,
            stale=stale,
            status=status,
            sw_name=sw_name,
            sw_version=sw_version,
            tt_conn_count=tt_conn_count,
            upgrade_summary=upgrade_summary,
        )

        get_v1_edges_summary_response_200_edges_summary_item.additional_properties = d
        return get_v1_edges_summary_response_200_edges_summary_item

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
