from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_producers_summary_response_200_info_item import (
        GetV1ExtranetsB2BProducersSummaryResponse200InfoItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BProducersSummaryResponse200")


@_attrs_define
class GetV1ExtranetsB2BProducersSummaryResponse200:
    """
    Attributes:
        info (Union[Unset, list['GetV1ExtranetsB2BProducersSummaryResponse200InfoItem']]):
    """

    info: Union[Unset, list["GetV1ExtranetsB2BProducersSummaryResponse200InfoItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.info, Unset):
            info = []
            for info_item_data in self.info:
                info_item = info_item_data.to_dict()
                info.append(info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_producers_summary_response_200_info_item import (
            GetV1ExtranetsB2BProducersSummaryResponse200InfoItem,
        )

        d = src_dict.copy()
        info = []
        _info = d.pop("info", UNSET)
        for info_item_data in _info or []:
            info_item = GetV1ExtranetsB2BProducersSummaryResponse200InfoItem.from_dict(info_item_data)

            info.append(info_item)

        get_v1_extranets_b2b_producers_summary_response_200 = cls(
            info=info,
        )

        get_v1_extranets_b2b_producers_summary_response_200.additional_properties = d
        return get_v1_extranets_b2b_producers_summary_response_200

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
