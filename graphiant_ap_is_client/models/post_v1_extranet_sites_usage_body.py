from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranet_sites_usage_body_time_window import PostV1ExtranetSitesUsageBodyTimeWindow


T = TypeVar("T", bound="PostV1ExtranetSitesUsageBody")


@_attrs_define
class PostV1ExtranetSitesUsageBody:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        is_b2b (Union[Unset, str]):  Example: TYPE_BOOL.
        is_provider (Union[Unset, str]):  Example: TYPE_BOOL.
        service_id (Union[Unset, str]):  Example: TYPE_INT64.
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        time_window (Union[Unset, PostV1ExtranetSitesUsageBodyTimeWindow]):
        vrf_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    id: Union[Unset, str] = UNSET
    is_b2b: Union[Unset, str] = UNSET
    is_provider: Union[Unset, str] = UNSET
    service_id: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV1ExtranetSitesUsageBodyTimeWindow"] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_b2b = self.is_b2b

        is_provider = self.is_provider

        service_id = self.service_id

        site_id = self.site_id

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_b2b is not UNSET:
            field_dict["isB2B"] = is_b2b
        if is_provider is not UNSET:
            field_dict["isProvider"] = is_provider
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranet_sites_usage_body_time_window import PostV1ExtranetSitesUsageBodyTimeWindow

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_b2b = d.pop("isB2B", UNSET)

        is_provider = d.pop("isProvider", UNSET)

        service_id = d.pop("serviceId", UNSET)

        site_id = d.pop("siteId", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1ExtranetSitesUsageBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1ExtranetSitesUsageBodyTimeWindow.from_dict(_time_window)

        vrf_id = d.pop("vrfId", UNSET)

        post_v1_extranet_sites_usage_body = cls(
            id=id,
            is_b2b=is_b2b,
            is_provider=is_provider,
            service_id=service_id,
            site_id=site_id,
            time_window=time_window,
            vrf_id=vrf_id,
        )

        post_v1_extranet_sites_usage_body.additional_properties = d
        return post_v1_extranet_sites_usage_body

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
