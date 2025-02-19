from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1SitesResponse200PageInfo")


@_attrs_define
class GetV1SitesResponse200PageInfo:
    """
    Attributes:
        current_page (Union[Unset, str]):  Example: 1.
        end_cursor (Union[Unset, str]):  Example: xxxxxxy.
        has_next_page (Union[Unset, str]):  Example: false.
        has_prev_page (Union[Unset, str]):  Example: true.
        start_cursor (Union[Unset, str]):  Example: xxxxxx.
        total_pages (Union[Unset, str]):  Example: 4.
        total_records (Union[Unset, str]):  Example: 400.
    """

    current_page: Union[Unset, str] = UNSET
    end_cursor: Union[Unset, str] = UNSET
    has_next_page: Union[Unset, str] = UNSET
    has_prev_page: Union[Unset, str] = UNSET
    start_cursor: Union[Unset, str] = UNSET
    total_pages: Union[Unset, str] = UNSET
    total_records: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        end_cursor = self.end_cursor

        has_next_page = self.has_next_page

        has_prev_page = self.has_prev_page

        start_cursor = self.start_cursor

        total_pages = self.total_pages

        total_records = self.total_records

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if end_cursor is not UNSET:
            field_dict["endCursor"] = end_cursor
        if has_next_page is not UNSET:
            field_dict["hasNextPage"] = has_next_page
        if has_prev_page is not UNSET:
            field_dict["hasPrevPage"] = has_prev_page
        if start_cursor is not UNSET:
            field_dict["startCursor"] = start_cursor
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if total_records is not UNSET:
            field_dict["totalRecords"] = total_records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        current_page = d.pop("currentPage", UNSET)

        end_cursor = d.pop("endCursor", UNSET)

        has_next_page = d.pop("hasNextPage", UNSET)

        has_prev_page = d.pop("hasPrevPage", UNSET)

        start_cursor = d.pop("startCursor", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        total_records = d.pop("totalRecords", UNSET)

        get_v1_sites_response_200_page_info = cls(
            current_page=current_page,
            end_cursor=end_cursor,
            has_next_page=has_next_page,
            has_prev_page=has_prev_page,
            start_cursor=start_cursor,
            total_pages=total_pages,
            total_records=total_records,
        )

        get_v1_sites_response_200_page_info.additional_properties = d
        return get_v1_sites_response_200_page_info

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
