from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_traffic_policies_dpi_applications_item_value_application import (
        PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItemValueApplication,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItemValue")


@_attrs_define
class PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItemValue:
    """
    Attributes:
        application (Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItemValueApplication]):
    """

    application: Union[Unset, "PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItemValueApplication"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application is not UNSET:
            field_dict["application"] = application

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_traffic_policies_dpi_applications_item_value_application import (
            PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItemValueApplication,
        )

        d = src_dict.copy()
        _application = d.pop("application", UNSET)
        application: Union[Unset, PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItemValueApplication]
        if isinstance(_application, Unset):
            application = UNSET
        else:
            application = PatchV1GlobalConfigBodyTrafficPoliciesDpiApplicationsItemValueApplication.from_dict(
                _application
            )

        patch_v1_global_config_body_traffic_policies_dpi_applications_item_value = cls(
            application=application,
        )

        patch_v1_global_config_body_traffic_policies_dpi_applications_item_value.additional_properties = d
        return patch_v1_global_config_body_traffic_policies_dpi_applications_item_value

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
