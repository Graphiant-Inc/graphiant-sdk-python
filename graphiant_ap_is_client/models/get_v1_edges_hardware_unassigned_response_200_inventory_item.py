from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_edges_hardware_unassigned_response_200_inventory_item_assigned_on import (
        GetV1EdgesHardwareUnassignedResponse200InventoryItemAssignedOn,
    )
    from ..models.get_v1_edges_hardware_unassigned_response_200_inventory_item_created_on import (
        GetV1EdgesHardwareUnassignedResponse200InventoryItemCreatedOn,
    )


T = TypeVar("T", bound="GetV1EdgesHardwareUnassignedResponse200InventoryItem")


@_attrs_define
class GetV1EdgesHardwareUnassignedResponse200InventoryItem:
    """
    Attributes:
        assigned_on (Union[Unset, GetV1EdgesHardwareUnassignedResponse200InventoryItemAssignedOn]):
        created_on (Union[Unset, GetV1EdgesHardwareUnassignedResponse200InventoryItemCreatedOn]):
        device_model (Union[Unset, str]):  Example: TYPE_STRING.
        device_serial (Union[Unset, str]):  Example: TYPE_STRING.
        ek_cert (Union[Unset, str]):  Example: TYPE_STRING.
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        enterprise_name (Union[Unset, str]):  Example: TYPE_STRING.
        gek_pub (Union[Unset, str]):  Example: TYPE_STRING.
        is_core (Union[Unset, str]):  Example: TYPE_BOOL.
        is_new (Union[Unset, str]):  Example: TYPE_BOOL.
        is_requested (Union[Unset, str]):  Example: TYPE_BOOL.
        parent_enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        parent_enterprise_name (Union[Unset, str]):  Example: TYPE_STRING.
        use_oauth (Union[Unset, str]):  Example: TYPE_BOOL.
        uuid (Union[Unset, str]):  Example: TYPE_STRING.
    """

    assigned_on: Union[Unset, "GetV1EdgesHardwareUnassignedResponse200InventoryItemAssignedOn"] = UNSET
    created_on: Union[Unset, "GetV1EdgesHardwareUnassignedResponse200InventoryItemCreatedOn"] = UNSET
    device_model: Union[Unset, str] = UNSET
    device_serial: Union[Unset, str] = UNSET
    ek_cert: Union[Unset, str] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    enterprise_name: Union[Unset, str] = UNSET
    gek_pub: Union[Unset, str] = UNSET
    is_core: Union[Unset, str] = UNSET
    is_new: Union[Unset, str] = UNSET
    is_requested: Union[Unset, str] = UNSET
    parent_enterprise_id: Union[Unset, str] = UNSET
    parent_enterprise_name: Union[Unset, str] = UNSET
    use_oauth: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_on: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assigned_on, Unset):
            assigned_on = self.assigned_on.to_dict()

        created_on: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.to_dict()

        device_model = self.device_model

        device_serial = self.device_serial

        ek_cert = self.ek_cert

        enterprise_id = self.enterprise_id

        enterprise_name = self.enterprise_name

        gek_pub = self.gek_pub

        is_core = self.is_core

        is_new = self.is_new

        is_requested = self.is_requested

        parent_enterprise_id = self.parent_enterprise_id

        parent_enterprise_name = self.parent_enterprise_name

        use_oauth = self.use_oauth

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_on is not UNSET:
            field_dict["assignedOn"] = assigned_on
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if device_serial is not UNSET:
            field_dict["deviceSerial"] = device_serial
        if ek_cert is not UNSET:
            field_dict["ekCert"] = ek_cert
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if enterprise_name is not UNSET:
            field_dict["enterpriseName"] = enterprise_name
        if gek_pub is not UNSET:
            field_dict["gekPub"] = gek_pub
        if is_core is not UNSET:
            field_dict["isCore"] = is_core
        if is_new is not UNSET:
            field_dict["isNew"] = is_new
        if is_requested is not UNSET:
            field_dict["isRequested"] = is_requested
        if parent_enterprise_id is not UNSET:
            field_dict["parentEnterpriseId"] = parent_enterprise_id
        if parent_enterprise_name is not UNSET:
            field_dict["parentEnterpriseName"] = parent_enterprise_name
        if use_oauth is not UNSET:
            field_dict["useOauth"] = use_oauth
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_edges_hardware_unassigned_response_200_inventory_item_assigned_on import (
            GetV1EdgesHardwareUnassignedResponse200InventoryItemAssignedOn,
        )
        from ..models.get_v1_edges_hardware_unassigned_response_200_inventory_item_created_on import (
            GetV1EdgesHardwareUnassignedResponse200InventoryItemCreatedOn,
        )

        d = src_dict.copy()
        _assigned_on = d.pop("assignedOn", UNSET)
        assigned_on: Union[Unset, GetV1EdgesHardwareUnassignedResponse200InventoryItemAssignedOn]
        if isinstance(_assigned_on, Unset):
            assigned_on = UNSET
        else:
            assigned_on = GetV1EdgesHardwareUnassignedResponse200InventoryItemAssignedOn.from_dict(_assigned_on)

        _created_on = d.pop("createdOn", UNSET)
        created_on: Union[Unset, GetV1EdgesHardwareUnassignedResponse200InventoryItemCreatedOn]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = GetV1EdgesHardwareUnassignedResponse200InventoryItemCreatedOn.from_dict(_created_on)

        device_model = d.pop("deviceModel", UNSET)

        device_serial = d.pop("deviceSerial", UNSET)

        ek_cert = d.pop("ekCert", UNSET)

        enterprise_id = d.pop("enterpriseId", UNSET)

        enterprise_name = d.pop("enterpriseName", UNSET)

        gek_pub = d.pop("gekPub", UNSET)

        is_core = d.pop("isCore", UNSET)

        is_new = d.pop("isNew", UNSET)

        is_requested = d.pop("isRequested", UNSET)

        parent_enterprise_id = d.pop("parentEnterpriseId", UNSET)

        parent_enterprise_name = d.pop("parentEnterpriseName", UNSET)

        use_oauth = d.pop("useOauth", UNSET)

        uuid = d.pop("uuid", UNSET)

        get_v1_edges_hardware_unassigned_response_200_inventory_item = cls(
            assigned_on=assigned_on,
            created_on=created_on,
            device_model=device_model,
            device_serial=device_serial,
            ek_cert=ek_cert,
            enterprise_id=enterprise_id,
            enterprise_name=enterprise_name,
            gek_pub=gek_pub,
            is_core=is_core,
            is_new=is_new,
            is_requested=is_requested,
            parent_enterprise_id=parent_enterprise_id,
            parent_enterprise_name=parent_enterprise_name,
            use_oauth=use_oauth,
            uuid=uuid,
        )

        get_v1_edges_hardware_unassigned_response_200_inventory_item.additional_properties = d
        return get_v1_edges_hardware_unassigned_response_200_inventory_item

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
