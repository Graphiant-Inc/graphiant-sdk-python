from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_upgrade_schedule_body_ts import PutV1DevicesUpgradeScheduleBodyTs
    from ..models.put_v1_devices_upgrade_schedule_body_version import PutV1DevicesUpgradeScheduleBodyVersion


T = TypeVar("T", bound="PutV1DevicesUpgradeScheduleBody")


@_attrs_define
class PutV1DevicesUpgradeScheduleBody:
    """
    Attributes:
        action (Union[Unset, str]):  Example: TYPE_ENUM.
        device_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        ts (Union[Unset, PutV1DevicesUpgradeScheduleBodyTs]):
        version (Union[Unset, PutV1DevicesUpgradeScheduleBodyVersion]):
    """

    action: Union[Unset, str] = UNSET
    device_ids: Union[Unset, list[str]] = UNSET
    ts: Union[Unset, "PutV1DevicesUpgradeScheduleBodyTs"] = UNSET
    version: Union[Unset, "PutV1DevicesUpgradeScheduleBodyVersion"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        device_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.device_ids, Unset):
            device_ids = self.device_ids

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if device_ids is not UNSET:
            field_dict["deviceIds"] = device_ids
        if ts is not UNSET:
            field_dict["ts"] = ts
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_upgrade_schedule_body_ts import PutV1DevicesUpgradeScheduleBodyTs
        from ..models.put_v1_devices_upgrade_schedule_body_version import PutV1DevicesUpgradeScheduleBodyVersion

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        device_ids = cast(list[str], d.pop("deviceIds", UNSET))

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PutV1DevicesUpgradeScheduleBodyTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PutV1DevicesUpgradeScheduleBodyTs.from_dict(_ts)

        _version = d.pop("version", UNSET)
        version: Union[Unset, PutV1DevicesUpgradeScheduleBodyVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = PutV1DevicesUpgradeScheduleBodyVersion.from_dict(_version)

        put_v1_devices_upgrade_schedule_body = cls(
            action=action,
            device_ids=device_ids,
            ts=ts,
            version=version,
        )

        put_v1_devices_upgrade_schedule_body.additional_properties = d
        return put_v1_devices_upgrade_schedule_body

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
