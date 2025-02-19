from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_alarms_list_response_200_alarms_item_created import GetV1AlarmsListResponse200AlarmsItemCreated
    from ..models.get_v1_alarms_list_response_200_alarms_item_last_changed import (
        GetV1AlarmsListResponse200AlarmsItemLastChanged,
    )
    from ..models.get_v1_alarms_list_response_200_alarms_item_last_raised import (
        GetV1AlarmsListResponse200AlarmsItemLastRaised,
    )


T = TypeVar("T", bound="GetV1AlarmsListResponse200AlarmsItem")


@_attrs_define
class GetV1AlarmsListResponse200AlarmsItem:
    """
    Attributes:
        acknowledged_by (Union[Unset, str]):  Example: 8a2ec658-f25b-11ec-b939-0242ac120002.
        alarm_id (Union[Unset, str]):  Example: 10000.
        alarm_type_id (Union[Unset, str]):  Example: graphnos-systemd:systemd-unit-state-change.
        alarm_type_qualifier (Union[Unset, str]):  Example: TYPE_STRING.
        alt_component (Union[Unset, str]):  Example: TYPE_STRING.
        boot_id (Union[Unset, str]):  Example: 8a2ec658-f25b-11ec-b939-0242ac120002.
        component (Union[Unset, str]):  Example: graphnos-ntp-mgr.service.
        created (Union[Unset, GetV1AlarmsListResponse200AlarmsItemCreated]):
        description (Union[Unset, str]):  Example: Unit is now active.
        is_cleared (Union[Unset, str]):  Example: false.
        is_resolved (Union[Unset, str]):  Example: false.
        last_changed (Union[Unset, GetV1AlarmsListResponse200AlarmsItemLastChanged]):
        last_raised (Union[Unset, GetV1AlarmsListResponse200AlarmsItemLastRaised]):
        perceived_severity (Union[Unset, str]):  Example: warning.
        resolved_by (Union[Unset, str]):  Example: 8a2ec658-f25b-11ec-b939-0242ac120002.
        sequence_number (Union[Unset, str]):  Example: 10.
        where (Union[Unset, str]):  Example: edge-32.
    """

    acknowledged_by: Union[Unset, str] = UNSET
    alarm_id: Union[Unset, str] = UNSET
    alarm_type_id: Union[Unset, str] = UNSET
    alarm_type_qualifier: Union[Unset, str] = UNSET
    alt_component: Union[Unset, str] = UNSET
    boot_id: Union[Unset, str] = UNSET
    component: Union[Unset, str] = UNSET
    created: Union[Unset, "GetV1AlarmsListResponse200AlarmsItemCreated"] = UNSET
    description: Union[Unset, str] = UNSET
    is_cleared: Union[Unset, str] = UNSET
    is_resolved: Union[Unset, str] = UNSET
    last_changed: Union[Unset, "GetV1AlarmsListResponse200AlarmsItemLastChanged"] = UNSET
    last_raised: Union[Unset, "GetV1AlarmsListResponse200AlarmsItemLastRaised"] = UNSET
    perceived_severity: Union[Unset, str] = UNSET
    resolved_by: Union[Unset, str] = UNSET
    sequence_number: Union[Unset, str] = UNSET
    where: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledged_by = self.acknowledged_by

        alarm_id = self.alarm_id

        alarm_type_id = self.alarm_type_id

        alarm_type_qualifier = self.alarm_type_qualifier

        alt_component = self.alt_component

        boot_id = self.boot_id

        component = self.component

        created: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        description = self.description

        is_cleared = self.is_cleared

        is_resolved = self.is_resolved

        last_changed: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_changed, Unset):
            last_changed = self.last_changed.to_dict()

        last_raised: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_raised, Unset):
            last_raised = self.last_raised.to_dict()

        perceived_severity = self.perceived_severity

        resolved_by = self.resolved_by

        sequence_number = self.sequence_number

        where = self.where

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledged_by is not UNSET:
            field_dict["acknowledgedBy"] = acknowledged_by
        if alarm_id is not UNSET:
            field_dict["alarmId"] = alarm_id
        if alarm_type_id is not UNSET:
            field_dict["alarmTypeId"] = alarm_type_id
        if alarm_type_qualifier is not UNSET:
            field_dict["alarmTypeQualifier"] = alarm_type_qualifier
        if alt_component is not UNSET:
            field_dict["altComponent"] = alt_component
        if boot_id is not UNSET:
            field_dict["bootId"] = boot_id
        if component is not UNSET:
            field_dict["component"] = component
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if is_cleared is not UNSET:
            field_dict["isCleared"] = is_cleared
        if is_resolved is not UNSET:
            field_dict["isResolved"] = is_resolved
        if last_changed is not UNSET:
            field_dict["lastChanged"] = last_changed
        if last_raised is not UNSET:
            field_dict["lastRaised"] = last_raised
        if perceived_severity is not UNSET:
            field_dict["perceivedSeverity"] = perceived_severity
        if resolved_by is not UNSET:
            field_dict["resolvedBy"] = resolved_by
        if sequence_number is not UNSET:
            field_dict["sequenceNumber"] = sequence_number
        if where is not UNSET:
            field_dict["where"] = where

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_alarms_list_response_200_alarms_item_created import (
            GetV1AlarmsListResponse200AlarmsItemCreated,
        )
        from ..models.get_v1_alarms_list_response_200_alarms_item_last_changed import (
            GetV1AlarmsListResponse200AlarmsItemLastChanged,
        )
        from ..models.get_v1_alarms_list_response_200_alarms_item_last_raised import (
            GetV1AlarmsListResponse200AlarmsItemLastRaised,
        )

        d = src_dict.copy()
        acknowledged_by = d.pop("acknowledgedBy", UNSET)

        alarm_id = d.pop("alarmId", UNSET)

        alarm_type_id = d.pop("alarmTypeId", UNSET)

        alarm_type_qualifier = d.pop("alarmTypeQualifier", UNSET)

        alt_component = d.pop("altComponent", UNSET)

        boot_id = d.pop("bootId", UNSET)

        component = d.pop("component", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, GetV1AlarmsListResponse200AlarmsItemCreated]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = GetV1AlarmsListResponse200AlarmsItemCreated.from_dict(_created)

        description = d.pop("description", UNSET)

        is_cleared = d.pop("isCleared", UNSET)

        is_resolved = d.pop("isResolved", UNSET)

        _last_changed = d.pop("lastChanged", UNSET)
        last_changed: Union[Unset, GetV1AlarmsListResponse200AlarmsItemLastChanged]
        if isinstance(_last_changed, Unset):
            last_changed = UNSET
        else:
            last_changed = GetV1AlarmsListResponse200AlarmsItemLastChanged.from_dict(_last_changed)

        _last_raised = d.pop("lastRaised", UNSET)
        last_raised: Union[Unset, GetV1AlarmsListResponse200AlarmsItemLastRaised]
        if isinstance(_last_raised, Unset):
            last_raised = UNSET
        else:
            last_raised = GetV1AlarmsListResponse200AlarmsItemLastRaised.from_dict(_last_raised)

        perceived_severity = d.pop("perceivedSeverity", UNSET)

        resolved_by = d.pop("resolvedBy", UNSET)

        sequence_number = d.pop("sequenceNumber", UNSET)

        where = d.pop("where", UNSET)

        get_v1_alarms_list_response_200_alarms_item = cls(
            acknowledged_by=acknowledged_by,
            alarm_id=alarm_id,
            alarm_type_id=alarm_type_id,
            alarm_type_qualifier=alarm_type_qualifier,
            alt_component=alt_component,
            boot_id=boot_id,
            component=component,
            created=created,
            description=description,
            is_cleared=is_cleared,
            is_resolved=is_resolved,
            last_changed=last_changed,
            last_raised=last_raised,
            perceived_severity=perceived_severity,
            resolved_by=resolved_by,
            sequence_number=sequence_number,
            where=where,
        )

        get_v1_alarms_list_response_200_alarms_item.additional_properties = d
        return get_v1_alarms_list_response_200_alarms_item

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
