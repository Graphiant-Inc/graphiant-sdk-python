from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_oauth_redirect_response_200_onboarding_redirection import (
        GetV1DevicesOauthRedirectResponse200OnboardingRedirection,
    )


T = TypeVar("T", bound="GetV1DevicesOauthRedirectResponse200")


@_attrs_define
class GetV1DevicesOauthRedirectResponse200:
    """
    Attributes:
        onboarding_redirection (Union[Unset, GetV1DevicesOauthRedirectResponse200OnboardingRedirection]):
    """

    onboarding_redirection: Union[Unset, "GetV1DevicesOauthRedirectResponse200OnboardingRedirection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        onboarding_redirection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.onboarding_redirection, Unset):
            onboarding_redirection = self.onboarding_redirection.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if onboarding_redirection is not UNSET:
            field_dict["onboardingRedirection"] = onboarding_redirection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_oauth_redirect_response_200_onboarding_redirection import (
            GetV1DevicesOauthRedirectResponse200OnboardingRedirection,
        )

        d = src_dict.copy()
        _onboarding_redirection = d.pop("onboardingRedirection", UNSET)
        onboarding_redirection: Union[Unset, GetV1DevicesOauthRedirectResponse200OnboardingRedirection]
        if isinstance(_onboarding_redirection, Unset):
            onboarding_redirection = UNSET
        else:
            onboarding_redirection = GetV1DevicesOauthRedirectResponse200OnboardingRedirection.from_dict(
                _onboarding_redirection
            )

        get_v1_devices_oauth_redirect_response_200 = cls(
            onboarding_redirection=onboarding_redirection,
        )

        get_v1_devices_oauth_redirect_response_200.additional_properties = d
        return get_v1_devices_oauth_redirect_response_200

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
