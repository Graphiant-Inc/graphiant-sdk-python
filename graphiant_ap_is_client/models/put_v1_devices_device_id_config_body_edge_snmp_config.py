from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_communities_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigCommunitiesItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_engine_endpoints_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigEngineEndpointsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_notify_filter_profiles_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigNotifyFilterProfilesItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_targets_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigTargetsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_usm_local_users_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmLocalUsersItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_usm_remote_users_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmRemoteUsersItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_vacm_groups_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmGroupsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_vacm_views_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmViewsItem,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfig")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfig:
    """
    Attributes:
        communities (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigCommunitiesItem']]):
        engine_authen_traps (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_endpoints (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigEngineEndpointsItem']]):
        engine_high_cpu_traps (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_high_memory_traps (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_id_admin_octets (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_admin_text (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_ipv_4 (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_ipv_6 (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_mac (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_raw (Union[Unset, str]):  Example: TYPE_STRING.
        engine_local_acess_v4 (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_local_acess_v6 (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_user_hints (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_user_validation (Union[Unset, str]):  Example: TYPE_BOOL.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        is_global_sync (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        notify_filter_profiles (Union[Unset,
            list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigNotifyFilterProfilesItem']]):
        targets (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigTargetsItem']]):
        usm_local_users (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmLocalUsersItem']]):
        usm_remote_users (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmRemoteUsersItem']]):
        v_2_c_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        v_3_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        vacm_groups (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmGroupsItem']]):
        vacm_views (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmViewsItem']]):
    """

    communities: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigCommunitiesItem"]] = UNSET
    engine_authen_traps: Union[Unset, str] = UNSET
    engine_enabled: Union[Unset, str] = UNSET
    engine_endpoints: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigEngineEndpointsItem"]] = UNSET
    engine_high_cpu_traps: Union[Unset, str] = UNSET
    engine_high_memory_traps: Union[Unset, str] = UNSET
    engine_id_admin_octets: Union[Unset, str] = UNSET
    engine_id_admin_text: Union[Unset, str] = UNSET
    engine_id_ipv_4: Union[Unset, str] = UNSET
    engine_id_ipv_6: Union[Unset, str] = UNSET
    engine_id_mac: Union[Unset, str] = UNSET
    engine_id_raw: Union[Unset, str] = UNSET
    engine_local_acess_v4: Union[Unset, str] = UNSET
    engine_local_acess_v6: Union[Unset, str] = UNSET
    engine_user_hints: Union[Unset, str] = UNSET
    engine_user_validation: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    is_global_sync: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notify_filter_profiles: Union[
        Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigNotifyFilterProfilesItem"]
    ] = UNSET
    targets: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigTargetsItem"]] = UNSET
    usm_local_users: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmLocalUsersItem"]] = UNSET
    usm_remote_users: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmRemoteUsersItem"]] = UNSET
    v_2_c_enabled: Union[Unset, str] = UNSET
    v_3_enabled: Union[Unset, str] = UNSET
    vacm_groups: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmGroupsItem"]] = UNSET
    vacm_views: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmViewsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        communities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.communities, Unset):
            communities = []
            for communities_item_data in self.communities:
                communities_item = communities_item_data.to_dict()
                communities.append(communities_item)

        engine_authen_traps = self.engine_authen_traps

        engine_enabled = self.engine_enabled

        engine_endpoints: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.engine_endpoints, Unset):
            engine_endpoints = []
            for engine_endpoints_item_data in self.engine_endpoints:
                engine_endpoints_item = engine_endpoints_item_data.to_dict()
                engine_endpoints.append(engine_endpoints_item)

        engine_high_cpu_traps = self.engine_high_cpu_traps

        engine_high_memory_traps = self.engine_high_memory_traps

        engine_id_admin_octets = self.engine_id_admin_octets

        engine_id_admin_text = self.engine_id_admin_text

        engine_id_ipv_4 = self.engine_id_ipv_4

        engine_id_ipv_6 = self.engine_id_ipv_6

        engine_id_mac = self.engine_id_mac

        engine_id_raw = self.engine_id_raw

        engine_local_acess_v4 = self.engine_local_acess_v4

        engine_local_acess_v6 = self.engine_local_acess_v6

        engine_user_hints = self.engine_user_hints

        engine_user_validation = self.engine_user_validation

        global_id = self.global_id

        is_global_sync = self.is_global_sync

        name = self.name

        notify_filter_profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notify_filter_profiles, Unset):
            notify_filter_profiles = []
            for notify_filter_profiles_item_data in self.notify_filter_profiles:
                notify_filter_profiles_item = notify_filter_profiles_item_data.to_dict()
                notify_filter_profiles.append(notify_filter_profiles_item)

        targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        usm_local_users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.usm_local_users, Unset):
            usm_local_users = []
            for usm_local_users_item_data in self.usm_local_users:
                usm_local_users_item = usm_local_users_item_data.to_dict()
                usm_local_users.append(usm_local_users_item)

        usm_remote_users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.usm_remote_users, Unset):
            usm_remote_users = []
            for usm_remote_users_item_data in self.usm_remote_users:
                usm_remote_users_item = usm_remote_users_item_data.to_dict()
                usm_remote_users.append(usm_remote_users_item)

        v_2_c_enabled = self.v_2_c_enabled

        v_3_enabled = self.v_3_enabled

        vacm_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vacm_groups, Unset):
            vacm_groups = []
            for vacm_groups_item_data in self.vacm_groups:
                vacm_groups_item = vacm_groups_item_data.to_dict()
                vacm_groups.append(vacm_groups_item)

        vacm_views: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vacm_views, Unset):
            vacm_views = []
            for vacm_views_item_data in self.vacm_views:
                vacm_views_item = vacm_views_item_data.to_dict()
                vacm_views.append(vacm_views_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communities is not UNSET:
            field_dict["communities"] = communities
        if engine_authen_traps is not UNSET:
            field_dict["engineAuthenTraps"] = engine_authen_traps
        if engine_enabled is not UNSET:
            field_dict["engineEnabled"] = engine_enabled
        if engine_endpoints is not UNSET:
            field_dict["engineEndpoints"] = engine_endpoints
        if engine_high_cpu_traps is not UNSET:
            field_dict["engineHighCpuTraps"] = engine_high_cpu_traps
        if engine_high_memory_traps is not UNSET:
            field_dict["engineHighMemoryTraps"] = engine_high_memory_traps
        if engine_id_admin_octets is not UNSET:
            field_dict["engineIdAdminOctets"] = engine_id_admin_octets
        if engine_id_admin_text is not UNSET:
            field_dict["engineIdAdminText"] = engine_id_admin_text
        if engine_id_ipv_4 is not UNSET:
            field_dict["engineIdIpv4"] = engine_id_ipv_4
        if engine_id_ipv_6 is not UNSET:
            field_dict["engineIdIpv6"] = engine_id_ipv_6
        if engine_id_mac is not UNSET:
            field_dict["engineIdMac"] = engine_id_mac
        if engine_id_raw is not UNSET:
            field_dict["engineIdRaw"] = engine_id_raw
        if engine_local_acess_v4 is not UNSET:
            field_dict["engineLocalAcessV4"] = engine_local_acess_v4
        if engine_local_acess_v6 is not UNSET:
            field_dict["engineLocalAcessV6"] = engine_local_acess_v6
        if engine_user_hints is not UNSET:
            field_dict["engineUserHints"] = engine_user_hints
        if engine_user_validation is not UNSET:
            field_dict["engineUserValidation"] = engine_user_validation
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if is_global_sync is not UNSET:
            field_dict["isGlobalSync"] = is_global_sync
        if name is not UNSET:
            field_dict["name"] = name
        if notify_filter_profiles is not UNSET:
            field_dict["notifyFilterProfiles"] = notify_filter_profiles
        if targets is not UNSET:
            field_dict["targets"] = targets
        if usm_local_users is not UNSET:
            field_dict["usmLocalUsers"] = usm_local_users
        if usm_remote_users is not UNSET:
            field_dict["usmRemoteUsers"] = usm_remote_users
        if v_2_c_enabled is not UNSET:
            field_dict["v2cEnabled"] = v_2_c_enabled
        if v_3_enabled is not UNSET:
            field_dict["v3Enabled"] = v_3_enabled
        if vacm_groups is not UNSET:
            field_dict["vacmGroups"] = vacm_groups
        if vacm_views is not UNSET:
            field_dict["vacmViews"] = vacm_views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_communities_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigCommunitiesItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_engine_endpoints_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigEngineEndpointsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_notify_filter_profiles_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigNotifyFilterProfilesItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_targets_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigTargetsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_usm_local_users_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmLocalUsersItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_usm_remote_users_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmRemoteUsersItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_vacm_groups_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmGroupsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_config_vacm_views_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmViewsItem,
        )

        d = src_dict.copy()
        communities = []
        _communities = d.pop("communities", UNSET)
        for communities_item_data in _communities or []:
            communities_item = PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigCommunitiesItem.from_dict(
                communities_item_data
            )

            communities.append(communities_item)

        engine_authen_traps = d.pop("engineAuthenTraps", UNSET)

        engine_enabled = d.pop("engineEnabled", UNSET)

        engine_endpoints = []
        _engine_endpoints = d.pop("engineEndpoints", UNSET)
        for engine_endpoints_item_data in _engine_endpoints or []:
            engine_endpoints_item = PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigEngineEndpointsItem.from_dict(
                engine_endpoints_item_data
            )

            engine_endpoints.append(engine_endpoints_item)

        engine_high_cpu_traps = d.pop("engineHighCpuTraps", UNSET)

        engine_high_memory_traps = d.pop("engineHighMemoryTraps", UNSET)

        engine_id_admin_octets = d.pop("engineIdAdminOctets", UNSET)

        engine_id_admin_text = d.pop("engineIdAdminText", UNSET)

        engine_id_ipv_4 = d.pop("engineIdIpv4", UNSET)

        engine_id_ipv_6 = d.pop("engineIdIpv6", UNSET)

        engine_id_mac = d.pop("engineIdMac", UNSET)

        engine_id_raw = d.pop("engineIdRaw", UNSET)

        engine_local_acess_v4 = d.pop("engineLocalAcessV4", UNSET)

        engine_local_acess_v6 = d.pop("engineLocalAcessV6", UNSET)

        engine_user_hints = d.pop("engineUserHints", UNSET)

        engine_user_validation = d.pop("engineUserValidation", UNSET)

        global_id = d.pop("globalId", UNSET)

        is_global_sync = d.pop("isGlobalSync", UNSET)

        name = d.pop("name", UNSET)

        notify_filter_profiles = []
        _notify_filter_profiles = d.pop("notifyFilterProfiles", UNSET)
        for notify_filter_profiles_item_data in _notify_filter_profiles or []:
            notify_filter_profiles_item = (
                PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigNotifyFilterProfilesItem.from_dict(
                    notify_filter_profiles_item_data
                )
            )

            notify_filter_profiles.append(notify_filter_profiles_item)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigTargetsItem.from_dict(targets_item_data)

            targets.append(targets_item)

        usm_local_users = []
        _usm_local_users = d.pop("usmLocalUsers", UNSET)
        for usm_local_users_item_data in _usm_local_users or []:
            usm_local_users_item = PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmLocalUsersItem.from_dict(
                usm_local_users_item_data
            )

            usm_local_users.append(usm_local_users_item)

        usm_remote_users = []
        _usm_remote_users = d.pop("usmRemoteUsers", UNSET)
        for usm_remote_users_item_data in _usm_remote_users or []:
            usm_remote_users_item = PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigUsmRemoteUsersItem.from_dict(
                usm_remote_users_item_data
            )

            usm_remote_users.append(usm_remote_users_item)

        v_2_c_enabled = d.pop("v2cEnabled", UNSET)

        v_3_enabled = d.pop("v3Enabled", UNSET)

        vacm_groups = []
        _vacm_groups = d.pop("vacmGroups", UNSET)
        for vacm_groups_item_data in _vacm_groups or []:
            vacm_groups_item = PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmGroupsItem.from_dict(
                vacm_groups_item_data
            )

            vacm_groups.append(vacm_groups_item)

        vacm_views = []
        _vacm_views = d.pop("vacmViews", UNSET)
        for vacm_views_item_data in _vacm_views or []:
            vacm_views_item = PutV1DevicesDeviceIdConfigBodyEdgeSnmpConfigVacmViewsItem.from_dict(vacm_views_item_data)

            vacm_views.append(vacm_views_item)

        put_v1_devices_device_id_config_body_edge_snmp_config = cls(
            communities=communities,
            engine_authen_traps=engine_authen_traps,
            engine_enabled=engine_enabled,
            engine_endpoints=engine_endpoints,
            engine_high_cpu_traps=engine_high_cpu_traps,
            engine_high_memory_traps=engine_high_memory_traps,
            engine_id_admin_octets=engine_id_admin_octets,
            engine_id_admin_text=engine_id_admin_text,
            engine_id_ipv_4=engine_id_ipv_4,
            engine_id_ipv_6=engine_id_ipv_6,
            engine_id_mac=engine_id_mac,
            engine_id_raw=engine_id_raw,
            engine_local_acess_v4=engine_local_acess_v4,
            engine_local_acess_v6=engine_local_acess_v6,
            engine_user_hints=engine_user_hints,
            engine_user_validation=engine_user_validation,
            global_id=global_id,
            is_global_sync=is_global_sync,
            name=name,
            notify_filter_profiles=notify_filter_profiles,
            targets=targets,
            usm_local_users=usm_local_users,
            usm_remote_users=usm_remote_users,
            v_2_c_enabled=v_2_c_enabled,
            v_3_enabled=v_3_enabled,
            vacm_groups=vacm_groups,
            vacm_views=vacm_views,
        )

        put_v1_devices_device_id_config_body_edge_snmp_config.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_snmp_config

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
