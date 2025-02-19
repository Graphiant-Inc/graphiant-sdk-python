from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_client_session_details_response_200_session import (
        PostV2AssuranceTopologyClientSessionDetailsResponse200Session,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyClientSessionDetailsResponse200")


@_attrs_define
class PostV2AssuranceTopologyClientSessionDetailsResponse200:
    """
    Attributes:
        session (Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200Session]):
    """

    session: Union[Unset, "PostV2AssuranceTopologyClientSessionDetailsResponse200Session"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.session, Unset):
            session = self.session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_client_session_details_response_200_session import (
            PostV2AssuranceTopologyClientSessionDetailsResponse200Session,
        )

        d = src_dict.copy()
        _session = d.pop("session", UNSET)
        session: Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200Session]
        if isinstance(_session, Unset):
            session = UNSET
        else:
            session = PostV2AssuranceTopologyClientSessionDetailsResponse200Session.from_dict(_session)

        post_v2_assurance_topology_client_session_details_response_200 = cls(
            session=session,
        )

        post_v2_assurance_topology_client_session_details_response_200.additional_properties = d
        return post_v2_assurance_topology_client_session_details_response_200

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
