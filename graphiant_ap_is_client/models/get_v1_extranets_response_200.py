from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_response_200_page_info import GetV1ExtranetsResponse200PageInfo
    from ..models.get_v1_extranets_response_200_policies_item import GetV1ExtranetsResponse200PoliciesItem


T = TypeVar("T", bound="GetV1ExtranetsResponse200")


@_attrs_define
class GetV1ExtranetsResponse200:
    """
    Attributes:
        page_info (Union[Unset, GetV1ExtranetsResponse200PageInfo]):
        policies (Union[Unset, list['GetV1ExtranetsResponse200PoliciesItem']]):
    """

    page_info: Union[Unset, "GetV1ExtranetsResponse200PageInfo"] = UNSET
    policies: Union[Unset, list["GetV1ExtranetsResponse200PoliciesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info
        if policies is not UNSET:
            field_dict["policies"] = policies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_response_200_page_info import GetV1ExtranetsResponse200PageInfo
        from ..models.get_v1_extranets_response_200_policies_item import GetV1ExtranetsResponse200PoliciesItem

        d = src_dict.copy()
        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1ExtranetsResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1ExtranetsResponse200PageInfo.from_dict(_page_info)

        policies = []
        _policies = d.pop("policies", UNSET)
        for policies_item_data in _policies or []:
            policies_item = GetV1ExtranetsResponse200PoliciesItem.from_dict(policies_item_data)

            policies.append(policies_item)

        get_v1_extranets_response_200 = cls(
            page_info=page_info,
            policies=policies,
        )

        get_v1_extranets_response_200.additional_properties = d
        return get_v1_extranets_response_200

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
