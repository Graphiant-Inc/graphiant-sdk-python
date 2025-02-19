from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_alarms_response_200_alarms_item import GetV1AlarmsResponse200AlarmsItem
    from ..models.get_v1_alarms_response_200_page_info import GetV1AlarmsResponse200PageInfo


T = TypeVar("T", bound="GetV1AlarmsResponse200")


@_attrs_define
class GetV1AlarmsResponse200:
    """
    Attributes:
        alarms (Union[Unset, list['GetV1AlarmsResponse200AlarmsItem']]):
        page_info (Union[Unset, GetV1AlarmsResponse200PageInfo]):
    """

    alarms: Union[Unset, list["GetV1AlarmsResponse200AlarmsItem"]] = UNSET
    page_info: Union[Unset, "GetV1AlarmsResponse200PageInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alarms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.alarms, Unset):
            alarms = []
            for alarms_item_data in self.alarms:
                alarms_item = alarms_item_data.to_dict()
                alarms.append(alarms_item)

        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alarms is not UNSET:
            field_dict["alarms"] = alarms
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_alarms_response_200_alarms_item import GetV1AlarmsResponse200AlarmsItem
        from ..models.get_v1_alarms_response_200_page_info import GetV1AlarmsResponse200PageInfo

        d = src_dict.copy()
        alarms = []
        _alarms = d.pop("alarms", UNSET)
        for alarms_item_data in _alarms or []:
            alarms_item = GetV1AlarmsResponse200AlarmsItem.from_dict(alarms_item_data)

            alarms.append(alarms_item)

        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1AlarmsResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1AlarmsResponse200PageInfo.from_dict(_page_info)

        get_v1_alarms_response_200 = cls(
            alarms=alarms,
            page_info=page_info,
        )

        get_v1_alarms_response_200.additional_properties = d
        return get_v1_alarms_response_200

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
