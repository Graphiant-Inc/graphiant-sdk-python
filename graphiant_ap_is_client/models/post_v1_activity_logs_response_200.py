from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_activity_logs_response_200_details_item import PostV1ActivityLogsResponse200DetailsItem


T = TypeVar("T", bound="PostV1ActivityLogsResponse200")


@_attrs_define
class PostV1ActivityLogsResponse200:
    """
    Attributes:
        cursor_ref (Union[Unset, str]):  Example: TYPE_STRING.
        details (Union[Unset, list['PostV1ActivityLogsResponse200DetailsItem']]):
        total_logs (Union[Unset, str]):  Example: TYPE_UINT64.
    """

    cursor_ref: Union[Unset, str] = UNSET
    details: Union[Unset, list["PostV1ActivityLogsResponse200DetailsItem"]] = UNSET
    total_logs: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor_ref = self.cursor_ref

        details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        total_logs = self.total_logs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor_ref is not UNSET:
            field_dict["cursorRef"] = cursor_ref
        if details is not UNSET:
            field_dict["details"] = details
        if total_logs is not UNSET:
            field_dict["totalLogs"] = total_logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_activity_logs_response_200_details_item import PostV1ActivityLogsResponse200DetailsItem

        d = src_dict.copy()
        cursor_ref = d.pop("cursorRef", UNSET)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = PostV1ActivityLogsResponse200DetailsItem.from_dict(details_item_data)

            details.append(details_item)

        total_logs = d.pop("totalLogs", UNSET)

        post_v1_activity_logs_response_200 = cls(
            cursor_ref=cursor_ref,
            details=details,
            total_logs=total_logs,
        )

        post_v1_activity_logs_response_200.additional_properties = d
        return post_v1_activity_logs_response_200

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
