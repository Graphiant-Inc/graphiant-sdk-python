from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_portal_apikeys_response_200_api_key_info_item import (
        GetV1PortalApikeysResponse200ApiKeyInfoItem,
    )


T = TypeVar("T", bound="GetV1PortalApikeysResponse200")


@_attrs_define
class GetV1PortalApikeysResponse200:
    """
    Attributes:
        api_key_info (Union[Unset, list['GetV1PortalApikeysResponse200ApiKeyInfoItem']]):
    """

    api_key_info: Union[Unset, list["GetV1PortalApikeysResponse200ApiKeyInfoItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.api_key_info, Unset):
            api_key_info = []
            for api_key_info_item_data in self.api_key_info:
                api_key_info_item = api_key_info_item_data.to_dict()
                api_key_info.append(api_key_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_info is not UNSET:
            field_dict["apiKeyInfo"] = api_key_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_portal_apikeys_response_200_api_key_info_item import (
            GetV1PortalApikeysResponse200ApiKeyInfoItem,
        )

        d = src_dict.copy()
        api_key_info = []
        _api_key_info = d.pop("apiKeyInfo", UNSET)
        for api_key_info_item_data in _api_key_info or []:
            api_key_info_item = GetV1PortalApikeysResponse200ApiKeyInfoItem.from_dict(api_key_info_item_data)

            api_key_info.append(api_key_info_item)

        get_v1_portal_apikeys_response_200 = cls(
            api_key_info=api_key_info,
        )

        get_v1_portal_apikeys_response_200.additional_properties = d
        return get_v1_portal_apikeys_response_200

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
