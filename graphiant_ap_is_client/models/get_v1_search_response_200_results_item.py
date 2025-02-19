from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1SearchResponse200ResultsItem")


@_attrs_define
class GetV1SearchResponse200ResultsItem:
    """
    Attributes:
        context (Union[Unset, str]):  Example: 1.
        id (Union[Unset, str]):  Example: 1234.
        result (Union[Unset, str]):  Example: TYPE_STRING.
    """

    context: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context = self.context

        id = self.id

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if id is not UNSET:
            field_dict["id"] = id
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("context", UNSET)

        id = d.pop("id", UNSET)

        result = d.pop("result", UNSET)

        get_v1_search_response_200_results_item = cls(
            context=context,
            id=id,
            result=result,
        )

        get_v1_search_response_200_results_item.additional_properties = d
        return get_v1_search_response_200_results_item

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
