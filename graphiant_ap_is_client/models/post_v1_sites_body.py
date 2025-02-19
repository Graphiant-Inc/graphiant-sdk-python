from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_sites_body_site import PostV1SitesBodySite


T = TypeVar("T", bound="PostV1SitesBody")


@_attrs_define
class PostV1SitesBody:
    """
    Attributes:
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        site (Union[Unset, PostV1SitesBodySite]):
    """

    enterprise_id: Union[Unset, str] = UNSET
    site: Union[Unset, "PostV1SitesBodySite"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enterprise_id = self.enterprise_id

        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if site is not UNSET:
            field_dict["site"] = site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_sites_body_site import PostV1SitesBodySite

        d = src_dict.copy()
        enterprise_id = d.pop("enterpriseId", UNSET)

        _site = d.pop("site", UNSET)
        site: Union[Unset, PostV1SitesBodySite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = PostV1SitesBodySite.from_dict(_site)

        post_v1_sites_body = cls(
            enterprise_id=enterprise_id,
            site=site,
        )

        post_v1_sites_body.additional_properties = d
        return post_v1_sites_body

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
