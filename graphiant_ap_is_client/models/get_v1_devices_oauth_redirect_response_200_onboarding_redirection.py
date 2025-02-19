from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesOauthRedirectResponse200OnboardingRedirection")


@_attrs_define
class GetV1DevicesOauthRedirectResponse200OnboardingRedirection:
    """
    Attributes:
        private_onboarding_gw_addr (Union[Unset, str]):  Example: TYPE_STRING.
        private_portal_url (Union[Unset, str]):  Example: TYPE_STRING.
        public_key (Union[Unset, str]):  Example: TYPE_STRING.
        root_ca (Union[Unset, str]):  Example: TYPE_STRING.
        signature (Union[Unset, str]):  Example: TYPE_STRING.
    """

    private_onboarding_gw_addr: Union[Unset, str] = UNSET
    private_portal_url: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    root_ca: Union[Unset, str] = UNSET
    signature: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_onboarding_gw_addr = self.private_onboarding_gw_addr

        private_portal_url = self.private_portal_url

        public_key = self.public_key

        root_ca = self.root_ca

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_onboarding_gw_addr is not UNSET:
            field_dict["privateOnboardingGwAddr"] = private_onboarding_gw_addr
        if private_portal_url is not UNSET:
            field_dict["privatePortalUrl"] = private_portal_url
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if root_ca is not UNSET:
            field_dict["rootCa"] = root_ca
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        private_onboarding_gw_addr = d.pop("privateOnboardingGwAddr", UNSET)

        private_portal_url = d.pop("privatePortalUrl", UNSET)

        public_key = d.pop("publicKey", UNSET)

        root_ca = d.pop("rootCa", UNSET)

        signature = d.pop("signature", UNSET)

        get_v1_devices_oauth_redirect_response_200_onboarding_redirection = cls(
            private_onboarding_gw_addr=private_onboarding_gw_addr,
            private_portal_url=private_portal_url,
            public_key=public_key,
            root_ca=root_ca,
            signature=signature,
        )

        get_v1_devices_oauth_redirect_response_200_onboarding_redirection.additional_properties = d
        return get_v1_devices_oauth_redirect_response_200_onboarding_redirection

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
