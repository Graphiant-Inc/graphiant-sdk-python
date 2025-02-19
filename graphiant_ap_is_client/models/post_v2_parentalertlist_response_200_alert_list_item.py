from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_parentalertlist_response_200_alert_list_item_children_alert_list import (
        PostV2ParentalertlistResponse200AlertListItemChildrenAlertList,
    )


T = TypeVar("T", bound="PostV2ParentalertlistResponse200AlertListItem")


@_attrs_define
class PostV2ParentalertlistResponse200AlertListItem:
    """
    Attributes:
        acknowledged_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        acknowledgement_reason (Union[Unset, str]):  Example: TYPE_STRING.
        alert_body (Union[Unset, str]):  Example: TYPE_STRING.
        alert_id (Union[Unset, str]):  Example: TYPE_STRING.
        allow_listed (Union[Unset, str]):  Example: TYPE_BOOL.
        children_alert_list (Union[Unset, PostV2ParentalertlistResponse200AlertListItemChildrenAlertList]):
        descendant_present (Union[Unset, str]):  Example: TYPE_BOOL.
        device_id (Union[Unset, str]):  Example: TYPE_STRING.
        end_time (Union[Unset, str]):  Example: TYPE_UINT64.
        enterprise_id (Union[Unset, str]):  Example: TYPE_STRING.
        entity (Union[Unset, str]):  Example: TYPE_STRING.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        mute_listed (Union[Unset, str]):  Example: TYPE_BOOL.
        notification_created (Union[Unset, str]):  Example: TYPE_BOOL.
        occurrences (Union[Unset, str]):  Example: TYPE_UINT64.
        peer_device_id (Union[Unset, str]):  Example: TYPE_STRING.
        peer_interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        peer_name (Union[Unset, str]):  Example: TYPE_STRING.
        plane (Union[Unset, str]):  Example: TYPE_ENUM.
        reason (Union[Unset, str]):  Example: TYPE_STRING.
        recommendation (Union[Unset, str]):  Example: TYPE_STRING.
        rule_id (Union[Unset, str]):  Example: TYPE_STRING.
        severity (Union[Unset, str]):  Example: Low.
        site_id (Union[Unset, str]):  Example: TYPE_STRING.
        start_time (Union[Unset, str]):  Example: TYPE_UINT64.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        troubleshooting_disabled_reason (Union[Unset, str]):  Example: TYPE_STRING.
        troubleshooting_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        tunnel_interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_STRING.
    """

    acknowledged_list: Union[Unset, list[str]] = UNSET
    acknowledgement_reason: Union[Unset, str] = UNSET
    alert_body: Union[Unset, str] = UNSET
    alert_id: Union[Unset, str] = UNSET
    allow_listed: Union[Unset, str] = UNSET
    children_alert_list: Union[Unset, "PostV2ParentalertlistResponse200AlertListItemChildrenAlertList"] = UNSET
    descendant_present: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    end_time: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    entity: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    mute_listed: Union[Unset, str] = UNSET
    notification_created: Union[Unset, str] = UNSET
    occurrences: Union[Unset, str] = UNSET
    peer_device_id: Union[Unset, str] = UNSET
    peer_interface_name: Union[Unset, str] = UNSET
    peer_name: Union[Unset, str] = UNSET
    plane: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    recommendation: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    start_time: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    troubleshooting_disabled_reason: Union[Unset, str] = UNSET
    troubleshooting_enabled: Union[Unset, str] = UNSET
    tunnel_interface_name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledged_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.acknowledged_list, Unset):
            acknowledged_list = self.acknowledged_list

        acknowledgement_reason = self.acknowledgement_reason

        alert_body = self.alert_body

        alert_id = self.alert_id

        allow_listed = self.allow_listed

        children_alert_list: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.children_alert_list, Unset):
            children_alert_list = self.children_alert_list.to_dict()

        descendant_present = self.descendant_present

        device_id = self.device_id

        end_time = self.end_time

        enterprise_id = self.enterprise_id

        entity = self.entity

        interface_name = self.interface_name

        mute_listed = self.mute_listed

        notification_created = self.notification_created

        occurrences = self.occurrences

        peer_device_id = self.peer_device_id

        peer_interface_name = self.peer_interface_name

        peer_name = self.peer_name

        plane = self.plane

        reason = self.reason

        recommendation = self.recommendation

        rule_id = self.rule_id

        severity = self.severity

        site_id = self.site_id

        start_time = self.start_time

        status = self.status

        troubleshooting_disabled_reason = self.troubleshooting_disabled_reason

        troubleshooting_enabled = self.troubleshooting_enabled

        tunnel_interface_name = self.tunnel_interface_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledged_list is not UNSET:
            field_dict["acknowledgedList"] = acknowledged_list
        if acknowledgement_reason is not UNSET:
            field_dict["acknowledgementReason"] = acknowledgement_reason
        if alert_body is not UNSET:
            field_dict["alertBody"] = alert_body
        if alert_id is not UNSET:
            field_dict["alertId"] = alert_id
        if allow_listed is not UNSET:
            field_dict["allowListed"] = allow_listed
        if children_alert_list is not UNSET:
            field_dict["childrenAlertList"] = children_alert_list
        if descendant_present is not UNSET:
            field_dict["descendantPresent"] = descendant_present
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if mute_listed is not UNSET:
            field_dict["muteListed"] = mute_listed
        if notification_created is not UNSET:
            field_dict["notificationCreated"] = notification_created
        if occurrences is not UNSET:
            field_dict["occurrences"] = occurrences
        if peer_device_id is not UNSET:
            field_dict["peerDeviceId"] = peer_device_id
        if peer_interface_name is not UNSET:
            field_dict["peerInterfaceName"] = peer_interface_name
        if peer_name is not UNSET:
            field_dict["peerName"] = peer_name
        if plane is not UNSET:
            field_dict["plane"] = plane
        if reason is not UNSET:
            field_dict["reason"] = reason
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if troubleshooting_disabled_reason is not UNSET:
            field_dict["troubleshootingDisabledReason"] = troubleshooting_disabled_reason
        if troubleshooting_enabled is not UNSET:
            field_dict["troubleshootingEnabled"] = troubleshooting_enabled
        if tunnel_interface_name is not UNSET:
            field_dict["tunnelInterfaceName"] = tunnel_interface_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_parentalertlist_response_200_alert_list_item_children_alert_list import (
            PostV2ParentalertlistResponse200AlertListItemChildrenAlertList,
        )

        d = src_dict.copy()
        acknowledged_list = cast(list[str], d.pop("acknowledgedList", UNSET))

        acknowledgement_reason = d.pop("acknowledgementReason", UNSET)

        alert_body = d.pop("alertBody", UNSET)

        alert_id = d.pop("alertId", UNSET)

        allow_listed = d.pop("allowListed", UNSET)

        _children_alert_list = d.pop("childrenAlertList", UNSET)
        children_alert_list: Union[Unset, PostV2ParentalertlistResponse200AlertListItemChildrenAlertList]
        if isinstance(_children_alert_list, Unset):
            children_alert_list = UNSET
        else:
            children_alert_list = PostV2ParentalertlistResponse200AlertListItemChildrenAlertList.from_dict(
                _children_alert_list
            )

        descendant_present = d.pop("descendantPresent", UNSET)

        device_id = d.pop("deviceId", UNSET)

        end_time = d.pop("endTime", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        entity = d.pop("entity", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        mute_listed = d.pop("muteListed", UNSET)

        notification_created = d.pop("notificationCreated", UNSET)

        occurrences = d.pop("occurrences", UNSET)

        peer_device_id = d.pop("peerDeviceId", UNSET)

        peer_interface_name = d.pop("peerInterfaceName", UNSET)

        peer_name = d.pop("peerName", UNSET)

        plane = d.pop("plane", UNSET)

        reason = d.pop("reason", UNSET)

        recommendation = d.pop("recommendation", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        severity = d.pop("severity", UNSET)

        site_id = d.pop("siteId", UNSET)

        start_time = d.pop("startTime", UNSET)

        status = d.pop("status", UNSET)

        troubleshooting_disabled_reason = d.pop("troubleshootingDisabledReason", UNSET)

        troubleshooting_enabled = d.pop("troubleshootingEnabled", UNSET)

        tunnel_interface_name = d.pop("tunnelInterfaceName", UNSET)

        type_ = d.pop("type", UNSET)

        post_v2_parentalertlist_response_200_alert_list_item = cls(
            acknowledged_list=acknowledged_list,
            acknowledgement_reason=acknowledgement_reason,
            alert_body=alert_body,
            alert_id=alert_id,
            allow_listed=allow_listed,
            children_alert_list=children_alert_list,
            descendant_present=descendant_present,
            device_id=device_id,
            end_time=end_time,
            enterprise_id=enterprise_id,
            entity=entity,
            interface_name=interface_name,
            mute_listed=mute_listed,
            notification_created=notification_created,
            occurrences=occurrences,
            peer_device_id=peer_device_id,
            peer_interface_name=peer_interface_name,
            peer_name=peer_name,
            plane=plane,
            reason=reason,
            recommendation=recommendation,
            rule_id=rule_id,
            severity=severity,
            site_id=site_id,
            start_time=start_time,
            status=status,
            troubleshooting_disabled_reason=troubleshooting_disabled_reason,
            troubleshooting_enabled=troubleshooting_enabled,
            tunnel_interface_name=tunnel_interface_name,
            type_=type_,
        )

        post_v2_parentalertlist_response_200_alert_list_item.additional_properties = d
        return post_v2_parentalertlist_response_200_alert_list_item

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
