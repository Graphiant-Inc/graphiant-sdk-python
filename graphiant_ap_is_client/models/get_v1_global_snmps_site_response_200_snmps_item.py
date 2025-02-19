from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_snmps_site_response_200_snmps_item_communities_item import (
        GetV1GlobalSnmpsSiteResponse200SnmpsItemCommunitiesItem,
    )
    from ..models.get_v1_global_snmps_site_response_200_snmps_item_engine_endpoints_item import (
        GetV1GlobalSnmpsSiteResponse200SnmpsItemEngineEndpointsItem,
    )
    from ..models.get_v1_global_snmps_site_response_200_snmps_item_notify_filter_profiles_item import (
        GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItem,
    )
    from ..models.get_v1_global_snmps_site_response_200_snmps_item_targets_item import (
        GetV1GlobalSnmpsSiteResponse200SnmpsItemTargetsItem,
    )
    from ..models.get_v1_global_snmps_site_response_200_snmps_item_usm_local_users_item import (
        GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmLocalUsersItem,
    )
    from ..models.get_v1_global_snmps_site_response_200_snmps_item_usm_remote_users_item import (
        GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmRemoteUsersItem,
    )
    from ..models.get_v1_global_snmps_site_response_200_snmps_item_vacm_groups_item import (
        GetV1GlobalSnmpsSiteResponse200SnmpsItemVacmGroupsItem,
    )


T = TypeVar("T", bound="GetV1GlobalSnmpsSiteResponse200SnmpsItem")


@_attrs_define
class GetV1GlobalSnmpsSiteResponse200SnmpsItem:
    """
    Attributes:
        communities (Union[Unset, list['GetV1GlobalSnmpsSiteResponse200SnmpsItemCommunitiesItem']]):
        engine_enable_authen_traps (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_enable_high_memory_traps (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_enable_high_cpu_traps (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_enable_local_acess_v4 (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_enable_local_acess_v6 (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_enable_user_hints (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_enable_user_validation (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        engine_endpoints (Union[Unset, list['GetV1GlobalSnmpsSiteResponse200SnmpsItemEngineEndpointsItem']]):
        engine_id_admin_octets (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_admin_text (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_ipv_4 (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_ipv_6 (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_mac (Union[Unset, str]):  Example: TYPE_STRING.
        engine_id_raw (Union[Unset, str]):  Example: TYPE_STRING.
        error_message (Union[Unset, str]):  Example: TYPE_STRING.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        notify_filter_profiles (Union[Unset, list['GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItem']]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        targets (Union[Unset, list['GetV1GlobalSnmpsSiteResponse200SnmpsItemTargetsItem']]):
        usm_local_users (Union[Unset, list['GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmLocalUsersItem']]):
        usm_remote_users (Union[Unset, list['GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmRemoteUsersItem']]):
        v_2_c_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        v_3_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        vacm_groups (Union[Unset, list['GetV1GlobalSnmpsSiteResponse200SnmpsItemVacmGroupsItem']]):
    """

    communities: Union[Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItemCommunitiesItem"]] = UNSET
    engine_enable_authen_traps: Union[Unset, str] = UNSET
    engine_enable_high_memory_traps: Union[Unset, str] = UNSET
    engine_enable_high_cpu_traps: Union[Unset, str] = UNSET
    engine_enable_local_acess_v4: Union[Unset, str] = UNSET
    engine_enable_local_acess_v6: Union[Unset, str] = UNSET
    engine_enable_user_hints: Union[Unset, str] = UNSET
    engine_enable_user_validation: Union[Unset, str] = UNSET
    engine_enabled: Union[Unset, str] = UNSET
    engine_endpoints: Union[Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItemEngineEndpointsItem"]] = UNSET
    engine_id_admin_octets: Union[Unset, str] = UNSET
    engine_id_admin_text: Union[Unset, str] = UNSET
    engine_id_ipv_4: Union[Unset, str] = UNSET
    engine_id_ipv_6: Union[Unset, str] = UNSET
    engine_id_mac: Union[Unset, str] = UNSET
    engine_id_raw: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notify_filter_profiles: Union[Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItem"]] = (
        UNSET
    )
    status: Union[Unset, str] = UNSET
    targets: Union[Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItemTargetsItem"]] = UNSET
    usm_local_users: Union[Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmLocalUsersItem"]] = UNSET
    usm_remote_users: Union[Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmRemoteUsersItem"]] = UNSET
    v_2_c_enabled: Union[Unset, str] = UNSET
    v_3_enabled: Union[Unset, str] = UNSET
    vacm_groups: Union[Unset, list["GetV1GlobalSnmpsSiteResponse200SnmpsItemVacmGroupsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        communities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.communities, Unset):
            communities = []
            for communities_item_data in self.communities:
                communities_item = communities_item_data.to_dict()
                communities.append(communities_item)

        engine_enable_authen_traps = self.engine_enable_authen_traps

        engine_enable_high_memory_traps = self.engine_enable_high_memory_traps

        engine_enable_high_cpu_traps = self.engine_enable_high_cpu_traps

        engine_enable_local_acess_v4 = self.engine_enable_local_acess_v4

        engine_enable_local_acess_v6 = self.engine_enable_local_acess_v6

        engine_enable_user_hints = self.engine_enable_user_hints

        engine_enable_user_validation = self.engine_enable_user_validation

        engine_enabled = self.engine_enabled

        engine_endpoints: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.engine_endpoints, Unset):
            engine_endpoints = []
            for engine_endpoints_item_data in self.engine_endpoints:
                engine_endpoints_item = engine_endpoints_item_data.to_dict()
                engine_endpoints.append(engine_endpoints_item)

        engine_id_admin_octets = self.engine_id_admin_octets

        engine_id_admin_text = self.engine_id_admin_text

        engine_id_ipv_4 = self.engine_id_ipv_4

        engine_id_ipv_6 = self.engine_id_ipv_6

        engine_id_mac = self.engine_id_mac

        engine_id_raw = self.engine_id_raw

        error_message = self.error_message

        global_id = self.global_id

        id = self.id

        name = self.name

        notify_filter_profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notify_filter_profiles, Unset):
            notify_filter_profiles = []
            for notify_filter_profiles_item_data in self.notify_filter_profiles:
                notify_filter_profiles_item = notify_filter_profiles_item_data.to_dict()
                notify_filter_profiles.append(notify_filter_profiles_item)

        status = self.status

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communities is not UNSET:
            field_dict["communities"] = communities
        if engine_enable_authen_traps is not UNSET:
            field_dict["engineEnableAuthenTraps"] = engine_enable_authen_traps
        if engine_enable_high_memory_traps is not UNSET:
            field_dict["engineEnableHighMemoryTraps"] = engine_enable_high_memory_traps
        if engine_enable_high_cpu_traps is not UNSET:
            field_dict["engineEnableHighCpuTraps"] = engine_enable_high_cpu_traps
        if engine_enable_local_acess_v4 is not UNSET:
            field_dict["engineEnableLocalAcessV4"] = engine_enable_local_acess_v4
        if engine_enable_local_acess_v6 is not UNSET:
            field_dict["engineEnableLocalAcessV6"] = engine_enable_local_acess_v6
        if engine_enable_user_hints is not UNSET:
            field_dict["engineEnableUserHints"] = engine_enable_user_hints
        if engine_enable_user_validation is not UNSET:
            field_dict["engineEnableUserValidation"] = engine_enable_user_validation
        if engine_enabled is not UNSET:
            field_dict["engineEnabled"] = engine_enabled
        if engine_endpoints is not UNSET:
            field_dict["engineEndpoints"] = engine_endpoints
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
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if notify_filter_profiles is not UNSET:
            field_dict["notifyFilterProfiles"] = notify_filter_profiles
        if status is not UNSET:
            field_dict["status"] = status
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_snmps_site_response_200_snmps_item_communities_item import (
            GetV1GlobalSnmpsSiteResponse200SnmpsItemCommunitiesItem,
        )
        from ..models.get_v1_global_snmps_site_response_200_snmps_item_engine_endpoints_item import (
            GetV1GlobalSnmpsSiteResponse200SnmpsItemEngineEndpointsItem,
        )
        from ..models.get_v1_global_snmps_site_response_200_snmps_item_notify_filter_profiles_item import (
            GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItem,
        )
        from ..models.get_v1_global_snmps_site_response_200_snmps_item_targets_item import (
            GetV1GlobalSnmpsSiteResponse200SnmpsItemTargetsItem,
        )
        from ..models.get_v1_global_snmps_site_response_200_snmps_item_usm_local_users_item import (
            GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmLocalUsersItem,
        )
        from ..models.get_v1_global_snmps_site_response_200_snmps_item_usm_remote_users_item import (
            GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmRemoteUsersItem,
        )
        from ..models.get_v1_global_snmps_site_response_200_snmps_item_vacm_groups_item import (
            GetV1GlobalSnmpsSiteResponse200SnmpsItemVacmGroupsItem,
        )

        d = src_dict.copy()
        communities = []
        _communities = d.pop("communities", UNSET)
        for communities_item_data in _communities or []:
            communities_item = GetV1GlobalSnmpsSiteResponse200SnmpsItemCommunitiesItem.from_dict(communities_item_data)

            communities.append(communities_item)

        engine_enable_authen_traps = d.pop("engineEnableAuthenTraps", UNSET)

        engine_enable_high_memory_traps = d.pop("engineEnableHighMemoryTraps", UNSET)

        engine_enable_high_cpu_traps = d.pop("engineEnableHighCpuTraps", UNSET)

        engine_enable_local_acess_v4 = d.pop("engineEnableLocalAcessV4", UNSET)

        engine_enable_local_acess_v6 = d.pop("engineEnableLocalAcessV6", UNSET)

        engine_enable_user_hints = d.pop("engineEnableUserHints", UNSET)

        engine_enable_user_validation = d.pop("engineEnableUserValidation", UNSET)

        engine_enabled = d.pop("engineEnabled", UNSET)

        engine_endpoints = []
        _engine_endpoints = d.pop("engineEndpoints", UNSET)
        for engine_endpoints_item_data in _engine_endpoints or []:
            engine_endpoints_item = GetV1GlobalSnmpsSiteResponse200SnmpsItemEngineEndpointsItem.from_dict(
                engine_endpoints_item_data
            )

            engine_endpoints.append(engine_endpoints_item)

        engine_id_admin_octets = d.pop("engineIdAdminOctets", UNSET)

        engine_id_admin_text = d.pop("engineIdAdminText", UNSET)

        engine_id_ipv_4 = d.pop("engineIdIpv4", UNSET)

        engine_id_ipv_6 = d.pop("engineIdIpv6", UNSET)

        engine_id_mac = d.pop("engineIdMac", UNSET)

        engine_id_raw = d.pop("engineIdRaw", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        global_id = d.pop("globalId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        notify_filter_profiles = []
        _notify_filter_profiles = d.pop("notifyFilterProfiles", UNSET)
        for notify_filter_profiles_item_data in _notify_filter_profiles or []:
            notify_filter_profiles_item = GetV1GlobalSnmpsSiteResponse200SnmpsItemNotifyFilterProfilesItem.from_dict(
                notify_filter_profiles_item_data
            )

            notify_filter_profiles.append(notify_filter_profiles_item)

        status = d.pop("status", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = GetV1GlobalSnmpsSiteResponse200SnmpsItemTargetsItem.from_dict(targets_item_data)

            targets.append(targets_item)

        usm_local_users = []
        _usm_local_users = d.pop("usmLocalUsers", UNSET)
        for usm_local_users_item_data in _usm_local_users or []:
            usm_local_users_item = GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmLocalUsersItem.from_dict(
                usm_local_users_item_data
            )

            usm_local_users.append(usm_local_users_item)

        usm_remote_users = []
        _usm_remote_users = d.pop("usmRemoteUsers", UNSET)
        for usm_remote_users_item_data in _usm_remote_users or []:
            usm_remote_users_item = GetV1GlobalSnmpsSiteResponse200SnmpsItemUsmRemoteUsersItem.from_dict(
                usm_remote_users_item_data
            )

            usm_remote_users.append(usm_remote_users_item)

        v_2_c_enabled = d.pop("v2cEnabled", UNSET)

        v_3_enabled = d.pop("v3Enabled", UNSET)

        vacm_groups = []
        _vacm_groups = d.pop("vacmGroups", UNSET)
        for vacm_groups_item_data in _vacm_groups or []:
            vacm_groups_item = GetV1GlobalSnmpsSiteResponse200SnmpsItemVacmGroupsItem.from_dict(vacm_groups_item_data)

            vacm_groups.append(vacm_groups_item)

        get_v1_global_snmps_site_response_200_snmps_item = cls(
            communities=communities,
            engine_enable_authen_traps=engine_enable_authen_traps,
            engine_enable_high_memory_traps=engine_enable_high_memory_traps,
            engine_enable_high_cpu_traps=engine_enable_high_cpu_traps,
            engine_enable_local_acess_v4=engine_enable_local_acess_v4,
            engine_enable_local_acess_v6=engine_enable_local_acess_v6,
            engine_enable_user_hints=engine_enable_user_hints,
            engine_enable_user_validation=engine_enable_user_validation,
            engine_enabled=engine_enabled,
            engine_endpoints=engine_endpoints,
            engine_id_admin_octets=engine_id_admin_octets,
            engine_id_admin_text=engine_id_admin_text,
            engine_id_ipv_4=engine_id_ipv_4,
            engine_id_ipv_6=engine_id_ipv_6,
            engine_id_mac=engine_id_mac,
            engine_id_raw=engine_id_raw,
            error_message=error_message,
            global_id=global_id,
            id=id,
            name=name,
            notify_filter_profiles=notify_filter_profiles,
            status=status,
            targets=targets,
            usm_local_users=usm_local_users,
            usm_remote_users=usm_remote_users,
            v_2_c_enabled=v_2_c_enabled,
            v_3_enabled=v_3_enabled,
            vacm_groups=vacm_groups,
        )

        get_v1_global_snmps_site_response_200_snmps_item.additional_properties = d
        return get_v1_global_snmps_site_response_200_snmps_item

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
