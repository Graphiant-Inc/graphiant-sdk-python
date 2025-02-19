from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_troubleshooting_site_connectivity_status_response_200_connectivity_status_item import (
        GetV1TroubleshootingSiteConnectivityStatusResponse200ConnectivityStatusItem,
    )


T = TypeVar("T", bound="GetV1TroubleshootingSiteConnectivityStatusResponse200")


@_attrs_define
class GetV1TroubleshootingSiteConnectivityStatusResponse200:
    """
    Attributes:
        connectivity_status (Union[Unset,
            list['GetV1TroubleshootingSiteConnectivityStatusResponse200ConnectivityStatusItem']]):
    """

    connectivity_status: Union[
        Unset, list["GetV1TroubleshootingSiteConnectivityStatusResponse200ConnectivityStatusItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connectivity_status: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.connectivity_status, Unset):
            connectivity_status = []
            for connectivity_status_item_data in self.connectivity_status:
                connectivity_status_item = connectivity_status_item_data.to_dict()
                connectivity_status.append(connectivity_status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connectivity_status is not UNSET:
            field_dict["connectivityStatus"] = connectivity_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_troubleshooting_site_connectivity_status_response_200_connectivity_status_item import (
            GetV1TroubleshootingSiteConnectivityStatusResponse200ConnectivityStatusItem,
        )

        d = src_dict.copy()
        connectivity_status = []
        _connectivity_status = d.pop("connectivityStatus", UNSET)
        for connectivity_status_item_data in _connectivity_status or []:
            connectivity_status_item = (
                GetV1TroubleshootingSiteConnectivityStatusResponse200ConnectivityStatusItem.from_dict(
                    connectivity_status_item_data
                )
            )

            connectivity_status.append(connectivity_status_item)

        get_v1_troubleshooting_site_connectivity_status_response_200 = cls(
            connectivity_status=connectivity_status,
        )

        get_v1_troubleshooting_site_connectivity_status_response_200.additional_properties = d
        return get_v1_troubleshooting_site_connectivity_status_response_200

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
