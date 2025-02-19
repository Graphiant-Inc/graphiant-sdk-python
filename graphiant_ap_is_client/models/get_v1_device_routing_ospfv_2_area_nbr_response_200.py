from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_2_area_nbr_response_200_nbrs_item import (
        GetV1DeviceRoutingOspfv2AreaNbrResponse200NbrsItem,
    )
    from ..models.get_v1_device_routing_ospfv_2_area_nbr_response_200_page_info import (
        GetV1DeviceRoutingOspfv2AreaNbrResponse200PageInfo,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2AreaNbrResponse200")


@_attrs_define
class GetV1DeviceRoutingOspfv2AreaNbrResponse200:
    """
    Attributes:
        nbrs (Union[Unset, list['GetV1DeviceRoutingOspfv2AreaNbrResponse200NbrsItem']]):
        page_info (Union[Unset, GetV1DeviceRoutingOspfv2AreaNbrResponse200PageInfo]):
        token (Union[Unset, str]):  Example: xxxxxxxxx.
    """

    nbrs: Union[Unset, list["GetV1DeviceRoutingOspfv2AreaNbrResponse200NbrsItem"]] = UNSET
    page_info: Union[Unset, "GetV1DeviceRoutingOspfv2AreaNbrResponse200PageInfo"] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nbrs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nbrs, Unset):
            nbrs = []
            for nbrs_item_data in self.nbrs:
                nbrs_item = nbrs_item_data.to_dict()
                nbrs.append(nbrs_item)

        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nbrs is not UNSET:
            field_dict["nbrs"] = nbrs
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_2_area_nbr_response_200_nbrs_item import (
            GetV1DeviceRoutingOspfv2AreaNbrResponse200NbrsItem,
        )
        from ..models.get_v1_device_routing_ospfv_2_area_nbr_response_200_page_info import (
            GetV1DeviceRoutingOspfv2AreaNbrResponse200PageInfo,
        )

        d = src_dict.copy()
        nbrs = []
        _nbrs = d.pop("nbrs", UNSET)
        for nbrs_item_data in _nbrs or []:
            nbrs_item = GetV1DeviceRoutingOspfv2AreaNbrResponse200NbrsItem.from_dict(nbrs_item_data)

            nbrs.append(nbrs_item)

        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1DeviceRoutingOspfv2AreaNbrResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1DeviceRoutingOspfv2AreaNbrResponse200PageInfo.from_dict(_page_info)

        token = d.pop("token", UNSET)

        get_v1_device_routing_ospfv_2_area_nbr_response_200 = cls(
            nbrs=nbrs,
            page_info=page_info,
            token=token,
        )

        get_v1_device_routing_ospfv_2_area_nbr_response_200.additional_properties = d
        return get_v1_device_routing_ospfv_2_area_nbr_response_200

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
