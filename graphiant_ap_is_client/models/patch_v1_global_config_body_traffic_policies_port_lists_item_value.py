from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_traffic_policies_port_lists_item_value_list import (
        PatchV1GlobalConfigBodyTrafficPoliciesPortListsItemValueList,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyTrafficPoliciesPortListsItemValue")


@_attrs_define
class PatchV1GlobalConfigBodyTrafficPoliciesPortListsItemValue:
    """
    Attributes:
        list_ (Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesPortListsItemValueList]):
    """

    list_: Union[Unset, "PatchV1GlobalConfigBodyTrafficPoliciesPortListsItemValueList"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.list_, Unset):
            list_ = self.list_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if list_ is not UNSET:
            field_dict["list"] = list_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_traffic_policies_port_lists_item_value_list import (
            PatchV1GlobalConfigBodyTrafficPoliciesPortListsItemValueList,
        )

        d = src_dict.copy()
        _list_ = d.pop("list", UNSET)
        list_: Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesPortListsItemValueList]
        if isinstance(_list_, Unset):
            list_ = UNSET
        else:
            list_ = PatchV1GlobalConfigBodyTrafficPoliciesPortListsItemValueList.from_dict(_list_)

        patch_v1_global_config_body_traffic_policies_port_lists_item_value = cls(
            list_=list_,
        )

        patch_v1_global_config_body_traffic_policies_port_lists_item_value.additional_properties = d
        return patch_v1_global_config_body_traffic_policies_port_lists_item_value

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
