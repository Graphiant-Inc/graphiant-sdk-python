from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_applicationdetailsbyid_response_200_app_id_record import (
        PostV2AssuranceApplicationdetailsbyidResponse200AppIdRecord,
    )
    from ..models.post_v2_assurance_applicationdetailsbyid_response_200_app_name_record import (
        PostV2AssuranceApplicationdetailsbyidResponse200AppNameRecord,
    )


T = TypeVar("T", bound="PostV2AssuranceApplicationdetailsbyidResponse200")


@_attrs_define
class PostV2AssuranceApplicationdetailsbyidResponse200:
    """
    Attributes:
        app_id_record (Union[Unset, PostV2AssuranceApplicationdetailsbyidResponse200AppIdRecord]):
        app_name_record (Union[Unset, PostV2AssuranceApplicationdetailsbyidResponse200AppNameRecord]):
    """

    app_id_record: Union[Unset, "PostV2AssuranceApplicationdetailsbyidResponse200AppIdRecord"] = UNSET
    app_name_record: Union[Unset, "PostV2AssuranceApplicationdetailsbyidResponse200AppNameRecord"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id_record: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_id_record, Unset):
            app_id_record = self.app_id_record.to_dict()

        app_name_record: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_name_record, Unset):
            app_name_record = self.app_name_record.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id_record is not UNSET:
            field_dict["appIdRecord"] = app_id_record
        if app_name_record is not UNSET:
            field_dict["appNameRecord"] = app_name_record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_applicationdetailsbyid_response_200_app_id_record import (
            PostV2AssuranceApplicationdetailsbyidResponse200AppIdRecord,
        )
        from ..models.post_v2_assurance_applicationdetailsbyid_response_200_app_name_record import (
            PostV2AssuranceApplicationdetailsbyidResponse200AppNameRecord,
        )

        d = src_dict.copy()
        _app_id_record = d.pop("appIdRecord", UNSET)
        app_id_record: Union[Unset, PostV2AssuranceApplicationdetailsbyidResponse200AppIdRecord]
        if isinstance(_app_id_record, Unset):
            app_id_record = UNSET
        else:
            app_id_record = PostV2AssuranceApplicationdetailsbyidResponse200AppIdRecord.from_dict(_app_id_record)

        _app_name_record = d.pop("appNameRecord", UNSET)
        app_name_record: Union[Unset, PostV2AssuranceApplicationdetailsbyidResponse200AppNameRecord]
        if isinstance(_app_name_record, Unset):
            app_name_record = UNSET
        else:
            app_name_record = PostV2AssuranceApplicationdetailsbyidResponse200AppNameRecord.from_dict(_app_name_record)

        post_v2_assurance_applicationdetailsbyid_response_200 = cls(
            app_id_record=app_id_record,
            app_name_record=app_name_record,
        )

        post_v2_assurance_applicationdetailsbyid_response_200.additional_properties = d
        return post_v2_assurance_applicationdetailsbyid_response_200

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
