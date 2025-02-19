from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_syslogs_device_response_200_collectors_item import (
        GetV1GlobalSyslogsDeviceResponse200CollectorsItem,
    )


T = TypeVar("T", bound="GetV1GlobalSyslogsDeviceResponse200")


@_attrs_define
class GetV1GlobalSyslogsDeviceResponse200:
    """
    Attributes:
        collectors (Union[Unset, list['GetV1GlobalSyslogsDeviceResponse200CollectorsItem']]):
    """

    collectors: Union[Unset, list["GetV1GlobalSyslogsDeviceResponse200CollectorsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collectors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.collectors, Unset):
            collectors = []
            for collectors_item_data in self.collectors:
                collectors_item = collectors_item_data.to_dict()
                collectors.append(collectors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collectors is not UNSET:
            field_dict["collectors"] = collectors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_syslogs_device_response_200_collectors_item import (
            GetV1GlobalSyslogsDeviceResponse200CollectorsItem,
        )

        d = src_dict.copy()
        collectors = []
        _collectors = d.pop("collectors", UNSET)
        for collectors_item_data in _collectors or []:
            collectors_item = GetV1GlobalSyslogsDeviceResponse200CollectorsItem.from_dict(collectors_item_data)

            collectors.append(collectors_item)

        get_v1_global_syslogs_device_response_200 = cls(
            collectors=collectors,
        )

        get_v1_global_syslogs_device_response_200.additional_properties = d
        return get_v1_global_syslogs_device_response_200

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
