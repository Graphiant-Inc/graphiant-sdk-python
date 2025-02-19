from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_count_response_200_circuits_item import PostV1AppsCountResponse200CircuitsItem


T = TypeVar("T", bound="PostV1AppsCountResponse200")


@_attrs_define
class PostV1AppsCountResponse200:
    """
    Attributes:
        apps_count (Union[Unset, str]):  Example: TYPE_UINT32.
        circuits (Union[Unset, list['PostV1AppsCountResponse200CircuitsItem']]):
    """

    apps_count: Union[Unset, str] = UNSET
    circuits: Union[Unset, list["PostV1AppsCountResponse200CircuitsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps_count = self.apps_count

        circuits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits, Unset):
            circuits = []
            for circuits_item_data in self.circuits:
                circuits_item = circuits_item_data.to_dict()
                circuits.append(circuits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps_count is not UNSET:
            field_dict["appsCount"] = apps_count
        if circuits is not UNSET:
            field_dict["circuits"] = circuits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_count_response_200_circuits_item import PostV1AppsCountResponse200CircuitsItem

        d = src_dict.copy()
        apps_count = d.pop("appsCount", UNSET)

        circuits = []
        _circuits = d.pop("circuits", UNSET)
        for circuits_item_data in _circuits or []:
            circuits_item = PostV1AppsCountResponse200CircuitsItem.from_dict(circuits_item_data)

            circuits.append(circuits_item)

        post_v1_apps_count_response_200 = cls(
            apps_count=apps_count,
            circuits=circuits,
        )

        post_v1_apps_count_response_200.additional_properties = d
        return post_v1_apps_count_response_200

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
