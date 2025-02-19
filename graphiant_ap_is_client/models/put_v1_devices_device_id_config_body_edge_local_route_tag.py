from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_local_route_tag_entry import (
        PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTagEntry,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTag")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTag:
    """
    Attributes:
        entry (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTagEntry]):
    """

    entry: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTagEntry"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_local_route_tag_entry import (
            PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTagEntry,
        )

        d = src_dict.copy()
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTagEntry]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = PutV1DevicesDeviceIdConfigBodyEdgeLocalRouteTagEntry.from_dict(_entry)

        put_v1_devices_device_id_config_body_edge_local_route_tag = cls(
            entry=entry,
        )

        put_v1_devices_device_id_config_body_edge_local_route_tag.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_local_route_tag

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
