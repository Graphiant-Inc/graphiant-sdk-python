from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_portal_apikeys_response_200_api_key_info_item_expiry_ts import (
        GetV1PortalApikeysResponse200ApiKeyInfoItemExpiryTs,
    )


T = TypeVar("T", bound="GetV1PortalApikeysResponse200ApiKeyInfoItem")


@_attrs_define
class GetV1PortalApikeysResponse200ApiKeyInfoItem:
    """
    Attributes:
        expiry_ts (Union[Unset, GetV1PortalApikeysResponse200ApiKeyInfoItemExpiryTs]):
        gcs_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    expiry_ts: Union[Unset, "GetV1PortalApikeysResponse200ApiKeyInfoItemExpiryTs"] = UNSET
    gcs_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.expiry_ts, Unset):
            expiry_ts = self.expiry_ts.to_dict()

        gcs_name = self.gcs_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiry_ts is not UNSET:
            field_dict["expiryTs"] = expiry_ts
        if gcs_name is not UNSET:
            field_dict["gcsName"] = gcs_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_portal_apikeys_response_200_api_key_info_item_expiry_ts import (
            GetV1PortalApikeysResponse200ApiKeyInfoItemExpiryTs,
        )

        d = src_dict.copy()
        _expiry_ts = d.pop("expiryTs", UNSET)
        expiry_ts: Union[Unset, GetV1PortalApikeysResponse200ApiKeyInfoItemExpiryTs]
        if isinstance(_expiry_ts, Unset):
            expiry_ts = UNSET
        else:
            expiry_ts = GetV1PortalApikeysResponse200ApiKeyInfoItemExpiryTs.from_dict(_expiry_ts)

        gcs_name = d.pop("gcsName", UNSET)

        get_v1_portal_apikeys_response_200_api_key_info_item = cls(
            expiry_ts=expiry_ts,
            gcs_name=gcs_name,
        )

        get_v1_portal_apikeys_response_200_api_key_info_item.additional_properties = d
        return get_v1_portal_apikeys_response_200_api_key_info_item

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
