from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_response_200_device_traffic_policy_traffic_rulesets_item_rules_item import (
        GetV1DevicesDeviceIdResponse200DeviceTrafficPolicyTrafficRulesetsItemRulesItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdResponse200DeviceTrafficPolicyTrafficRulesetsItem")


@_attrs_define
class GetV1DevicesDeviceIdResponse200DeviceTrafficPolicyTrafficRulesetsItem:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        error_message (Union[Unset, str]):  Example: TYPE_STRING.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        index (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        rules (Union[Unset, list['GetV1DevicesDeviceIdResponse200DeviceTrafficPolicyTrafficRulesetsItemRulesItem']]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    description: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    index: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rules: Union[Unset, list["GetV1DevicesDeviceIdResponse200DeviceTrafficPolicyTrafficRulesetsItemRulesItem"]] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        error_message = self.error_message

        global_id = self.global_id

        id = self.id

        index = self.index

        name = self.name

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name
        if rules is not UNSET:
            field_dict["rules"] = rules
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_response_200_device_traffic_policy_traffic_rulesets_item_rules_item import (
            GetV1DevicesDeviceIdResponse200DeviceTrafficPolicyTrafficRulesetsItemRulesItem,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        global_id = d.pop("globalId", UNSET)

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = GetV1DevicesDeviceIdResponse200DeviceTrafficPolicyTrafficRulesetsItemRulesItem.from_dict(
                rules_item_data
            )

            rules.append(rules_item)

        status = d.pop("status", UNSET)

        get_v1_devices_device_id_response_200_device_traffic_policy_traffic_rulesets_item = cls(
            description=description,
            error_message=error_message,
            global_id=global_id,
            id=id,
            index=index,
            name=name,
            rules=rules,
            status=status,
        )

        get_v1_devices_device_id_response_200_device_traffic_policy_traffic_rulesets_item.additional_properties = d
        return get_v1_devices_device_id_response_200_device_traffic_policy_traffic_rulesets_item

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
