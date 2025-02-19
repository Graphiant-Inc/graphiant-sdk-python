from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_prefix_sets_item_entries_item import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemEntriesItem,
    )
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_prefix_sets_item_policies_item import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemPoliciesItem,
    )


T = TypeVar("T", bound="GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItem")


@_attrs_define
class GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItem:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        entries (Union[Unset,
            list['GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemEntriesItem']]):
        error_message (Union[Unset, str]):  Example: TYPE_STRING.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        mode (Union[Unset, str]):  Example: TYPE_ENUM.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        policies (Union[Unset,
            list['GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemPoliciesItem']]):
        policy_count (Union[Unset, str]):  Example: TYPE_UINT32.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    description: Union[Unset, str] = UNSET
    entries: Union[Unset, list["GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemEntriesItem"]] = (
        UNSET
    )
    error_message: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    policies: Union[
        Unset, list["GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemPoliciesItem"]
    ] = UNSET
    policy_count: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        error_message = self.error_message

        global_id = self.global_id

        id = self.id

        mode = self.mode

        name = self.name

        policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        policy_count = self.policy_count

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if entries is not UNSET:
            field_dict["entries"] = entries
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if id is not UNSET:
            field_dict["id"] = id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if policies is not UNSET:
            field_dict["policies"] = policies
        if policy_count is not UNSET:
            field_dict["policyCount"] = policy_count
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_prefix_sets_item_entries_item import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemEntriesItem,
        )
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_prefix_sets_item_policies_item import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemPoliciesItem,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemEntriesItem.from_dict(
                entries_item_data
            )

            entries.append(entries_item)

        error_message = d.pop("errorMessage", UNSET)

        global_id = d.pop("globalId", UNSET)

        id = d.pop("id", UNSET)

        mode = d.pop("mode", UNSET)

        name = d.pop("name", UNSET)

        policies = []
        _policies = d.pop("policies", UNSET)
        for policies_item_data in _policies or []:
            policies_item = (
                GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemPrefixSetsItemPoliciesItem.from_dict(
                    policies_item_data
                )
            )

            policies.append(policies_item)

        policy_count = d.pop("policyCount", UNSET)

        status = d.pop("status", UNSET)

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_prefix_sets_item = cls(
            description=description,
            entries=entries,
            error_message=error_message,
            global_id=global_id,
            id=id,
            mode=mode,
            name=name,
            policies=policies,
            policy_count=policy_count,
            status=status,
        )

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_prefix_sets_item.additional_properties = d
        return get_v1_enterprise_enterprise_id_devices_response_200_devices_item_prefix_sets_item

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
