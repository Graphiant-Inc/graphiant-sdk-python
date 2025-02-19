from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_bwtracker_enterprise_csv_response_200_bwusage_csv_details_bwusage_csv_record_item import (
        PostV1BwtrackerEnterpriseCsvResponse200BwusageCsvDetailsBwusageCsvRecordItem,
    )


T = TypeVar("T", bound="PostV1BwtrackerEnterpriseCsvResponse200BwusageCsvDetails")


@_attrs_define
class PostV1BwtrackerEnterpriseCsvResponse200BwusageCsvDetails:
    """
    Attributes:
        bwusage_csv_record (Union[Unset,
            list['PostV1BwtrackerEnterpriseCsvResponse200BwusageCsvDetailsBwusageCsvRecordItem']]):
    """

    bwusage_csv_record: Union[
        Unset, list["PostV1BwtrackerEnterpriseCsvResponse200BwusageCsvDetailsBwusageCsvRecordItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bwusage_csv_record: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bwusage_csv_record, Unset):
            bwusage_csv_record = []
            for bwusage_csv_record_item_data in self.bwusage_csv_record:
                bwusage_csv_record_item = bwusage_csv_record_item_data.to_dict()
                bwusage_csv_record.append(bwusage_csv_record_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bwusage_csv_record is not UNSET:
            field_dict["bwusageCsvRecord"] = bwusage_csv_record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_bwtracker_enterprise_csv_response_200_bwusage_csv_details_bwusage_csv_record_item import (
            PostV1BwtrackerEnterpriseCsvResponse200BwusageCsvDetailsBwusageCsvRecordItem,
        )

        d = src_dict.copy()
        bwusage_csv_record = []
        _bwusage_csv_record = d.pop("bwusageCsvRecord", UNSET)
        for bwusage_csv_record_item_data in _bwusage_csv_record or []:
            bwusage_csv_record_item = (
                PostV1BwtrackerEnterpriseCsvResponse200BwusageCsvDetailsBwusageCsvRecordItem.from_dict(
                    bwusage_csv_record_item_data
                )
            )

            bwusage_csv_record.append(bwusage_csv_record_item)

        post_v1_bwtracker_enterprise_csv_response_200_bwusage_csv_details = cls(
            bwusage_csv_record=bwusage_csv_record,
        )

        post_v1_bwtracker_enterprise_csv_response_200_bwusage_csv_details.additional_properties = d
        return post_v1_bwtracker_enterprise_csv_response_200_bwusage_csv_details

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
