from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1PortalPrivateBodyDetails")


@_attrs_define
class PostV1PortalPrivateBodyDetails:
    """
    Attributes:
        api_key (Union[Unset, str]):  Example: TYPE_STRING.
        is_disable (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        onboarding_gw_addr (Union[Unset, str]):  Example: TYPE_STRING.
        portal_url (Union[Unset, str]):  Example: TYPE_STRING.
        public_portal_url (Union[Unset, str]):  Example: TYPE_STRING.
        root_ca (Union[Unset, str]):  Example: TYPE_STRING.
    """

    api_key: Union[Unset, str] = UNSET
    is_disable: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    onboarding_gw_addr: Union[Unset, str] = UNSET
    portal_url: Union[Unset, str] = UNSET
    public_portal_url: Union[Unset, str] = UNSET
    root_ca: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        is_disable = self.is_disable

        name = self.name

        onboarding_gw_addr = self.onboarding_gw_addr

        portal_url = self.portal_url

        public_portal_url = self.public_portal_url

        root_ca = self.root_ca

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if is_disable is not UNSET:
            field_dict["isDisable"] = is_disable
        if name is not UNSET:
            field_dict["name"] = name
        if onboarding_gw_addr is not UNSET:
            field_dict["onboardingGwAddr"] = onboarding_gw_addr
        if portal_url is not UNSET:
            field_dict["portalUrl"] = portal_url
        if public_portal_url is not UNSET:
            field_dict["publicPortalUrl"] = public_portal_url
        if root_ca is not UNSET:
            field_dict["rootCa"] = root_ca

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key = d.pop("apiKey", UNSET)

        is_disable = d.pop("isDisable", UNSET)

        name = d.pop("name", UNSET)

        onboarding_gw_addr = d.pop("onboardingGwAddr", UNSET)

        portal_url = d.pop("portalUrl", UNSET)

        public_portal_url = d.pop("publicPortalUrl", UNSET)

        root_ca = d.pop("rootCa", UNSET)

        post_v1_portal_private_body_details = cls(
            api_key=api_key,
            is_disable=is_disable,
            name=name,
            onboarding_gw_addr=onboarding_gw_addr,
            portal_url=portal_url,
            public_portal_url=public_portal_url,
            root_ca=root_ca,
        )

        post_v1_portal_private_body_details.additional_properties = d
        return post_v1_portal_private_body_details

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
