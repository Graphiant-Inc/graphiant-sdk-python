from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprises_managed_response_200_counts import GetV1EnterprisesManagedResponse200Counts
    from ..models.get_v1_enterprises_managed_response_200_enterprises_item import (
        GetV1EnterprisesManagedResponse200EnterprisesItem,
    )


T = TypeVar("T", bound="GetV1EnterprisesManagedResponse200")


@_attrs_define
class GetV1EnterprisesManagedResponse200:
    """
    Attributes:
        counts (Union[Unset, GetV1EnterprisesManagedResponse200Counts]):
        enterprises (Union[Unset, list['GetV1EnterprisesManagedResponse200EnterprisesItem']]):
    """

    counts: Union[Unset, "GetV1EnterprisesManagedResponse200Counts"] = UNSET
    enterprises: Union[Unset, list["GetV1EnterprisesManagedResponse200EnterprisesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        enterprises: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enterprises, Unset):
            enterprises = []
            for enterprises_item_data in self.enterprises:
                enterprises_item = enterprises_item_data.to_dict()
                enterprises.append(enterprises_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counts is not UNSET:
            field_dict["counts"] = counts
        if enterprises is not UNSET:
            field_dict["enterprises"] = enterprises

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprises_managed_response_200_counts import GetV1EnterprisesManagedResponse200Counts
        from ..models.get_v1_enterprises_managed_response_200_enterprises_item import (
            GetV1EnterprisesManagedResponse200EnterprisesItem,
        )

        d = src_dict.copy()
        _counts = d.pop("counts", UNSET)
        counts: Union[Unset, GetV1EnterprisesManagedResponse200Counts]
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = GetV1EnterprisesManagedResponse200Counts.from_dict(_counts)

        enterprises = []
        _enterprises = d.pop("enterprises", UNSET)
        for enterprises_item_data in _enterprises or []:
            enterprises_item = GetV1EnterprisesManagedResponse200EnterprisesItem.from_dict(enterprises_item_data)

            enterprises.append(enterprises_item)

        get_v1_enterprises_managed_response_200 = cls(
            counts=counts,
            enterprises=enterprises,
        )

        get_v1_enterprises_managed_response_200.additional_properties = d
        return get_v1_enterprises_managed_response_200

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
