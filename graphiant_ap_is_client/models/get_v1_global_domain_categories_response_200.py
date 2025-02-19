from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_domain_categories_response_200_domain_categories_item import (
        GetV1GlobalDomainCategoriesResponse200DomainCategoriesItem,
    )


T = TypeVar("T", bound="GetV1GlobalDomainCategoriesResponse200")


@_attrs_define
class GetV1GlobalDomainCategoriesResponse200:
    """
    Attributes:
        domain_categories (Union[Unset, list['GetV1GlobalDomainCategoriesResponse200DomainCategoriesItem']]):
    """

    domain_categories: Union[Unset, list["GetV1GlobalDomainCategoriesResponse200DomainCategoriesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_categories: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.domain_categories, Unset):
            domain_categories = []
            for domain_categories_item_data in self.domain_categories:
                domain_categories_item = domain_categories_item_data.to_dict()
                domain_categories.append(domain_categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_categories is not UNSET:
            field_dict["domainCategories"] = domain_categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_domain_categories_response_200_domain_categories_item import (
            GetV1GlobalDomainCategoriesResponse200DomainCategoriesItem,
        )

        d = src_dict.copy()
        domain_categories = []
        _domain_categories = d.pop("domainCategories", UNSET)
        for domain_categories_item_data in _domain_categories or []:
            domain_categories_item = GetV1GlobalDomainCategoriesResponse200DomainCategoriesItem.from_dict(
                domain_categories_item_data
            )

            domain_categories.append(domain_categories_item)

        get_v1_global_domain_categories_response_200 = cls(
            domain_categories=domain_categories,
        )

        get_v1_global_domain_categories_response_200.additional_properties = d
        return get_v1_global_domain_categories_response_200

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
