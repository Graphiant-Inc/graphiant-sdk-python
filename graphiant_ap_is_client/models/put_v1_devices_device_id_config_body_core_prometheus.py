from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_core_prometheus_rule_groups_item import (
        PutV1DevicesDeviceIdConfigBodyCorePrometheusRuleGroupsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_prometheus_sink import (
        PutV1DevicesDeviceIdConfigBodyCorePrometheusSink,
    )
    from ..models.put_v1_devices_device_id_config_body_core_prometheus_sysdb_monitors_item import (
        PutV1DevicesDeviceIdConfigBodyCorePrometheusSysdbMonitorsItem,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCorePrometheus")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCorePrometheus:
    """
    Attributes:
        rule_groups (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCorePrometheusRuleGroupsItem']]):
        sink (Union[Unset, PutV1DevicesDeviceIdConfigBodyCorePrometheusSink]):
        sysdb_monitors (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCorePrometheusSysdbMonitorsItem']]):
    """

    rule_groups: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCorePrometheusRuleGroupsItem"]] = UNSET
    sink: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCorePrometheusSink"] = UNSET
    sysdb_monitors: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCorePrometheusSysdbMonitorsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rule_groups, Unset):
            rule_groups = []
            for rule_groups_item_data in self.rule_groups:
                rule_groups_item = rule_groups_item_data.to_dict()
                rule_groups.append(rule_groups_item)

        sink: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sink, Unset):
            sink = self.sink.to_dict()

        sysdb_monitors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sysdb_monitors, Unset):
            sysdb_monitors = []
            for sysdb_monitors_item_data in self.sysdb_monitors:
                sysdb_monitors_item = sysdb_monitors_item_data.to_dict()
                sysdb_monitors.append(sysdb_monitors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_groups is not UNSET:
            field_dict["ruleGroups"] = rule_groups
        if sink is not UNSET:
            field_dict["sink"] = sink
        if sysdb_monitors is not UNSET:
            field_dict["sysdbMonitors"] = sysdb_monitors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_core_prometheus_rule_groups_item import (
            PutV1DevicesDeviceIdConfigBodyCorePrometheusRuleGroupsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_prometheus_sink import (
            PutV1DevicesDeviceIdConfigBodyCorePrometheusSink,
        )
        from ..models.put_v1_devices_device_id_config_body_core_prometheus_sysdb_monitors_item import (
            PutV1DevicesDeviceIdConfigBodyCorePrometheusSysdbMonitorsItem,
        )

        d = src_dict.copy()
        rule_groups = []
        _rule_groups = d.pop("ruleGroups", UNSET)
        for rule_groups_item_data in _rule_groups or []:
            rule_groups_item = PutV1DevicesDeviceIdConfigBodyCorePrometheusRuleGroupsItem.from_dict(
                rule_groups_item_data
            )

            rule_groups.append(rule_groups_item)

        _sink = d.pop("sink", UNSET)
        sink: Union[Unset, PutV1DevicesDeviceIdConfigBodyCorePrometheusSink]
        if isinstance(_sink, Unset):
            sink = UNSET
        else:
            sink = PutV1DevicesDeviceIdConfigBodyCorePrometheusSink.from_dict(_sink)

        sysdb_monitors = []
        _sysdb_monitors = d.pop("sysdbMonitors", UNSET)
        for sysdb_monitors_item_data in _sysdb_monitors or []:
            sysdb_monitors_item = PutV1DevicesDeviceIdConfigBodyCorePrometheusSysdbMonitorsItem.from_dict(
                sysdb_monitors_item_data
            )

            sysdb_monitors.append(sysdb_monitors_item)

        put_v1_devices_device_id_config_body_core_prometheus = cls(
            rule_groups=rule_groups,
            sink=sink,
            sysdb_monitors=sysdb_monitors,
        )

        put_v1_devices_device_id_config_body_core_prometheus.additional_properties = d
        return put_v1_devices_device_id_config_body_core_prometheus

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
