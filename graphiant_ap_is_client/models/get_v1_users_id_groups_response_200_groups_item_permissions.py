from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1UsersIdGroupsResponse200GroupsItemPermissions")


@_attrs_define
class GetV1UsersIdGroupsResponse200GroupsItemPermissions:
    """
    Attributes:
        asset_manager (Union[Unset, str]):  Example: TYPE_ENUM.
        billing_and_invoicing (Union[Unset, str]):  Example: TYPE_ENUM.
        compliance (Union[Unset, str]):  Example: TYPE_ENUM.
        developer_tools (Union[Unset, str]):  Example: TYPE_ENUM.
        global_services (Union[Unset, str]):  Example: TYPE_ENUM.
        insights (Union[Unset, str]):  Example: TYPE_ENUM.
        licensing (Union[Unset, str]):  Example: TYPE_ENUM.
        logs (Union[Unset, str]):  Example: TYPE_ENUM.
        monitoring_and_troubleshooting (Union[Unset, str]):  Example: TYPE_ENUM.
        network_configuration (Union[Unset, str]):  Example: TYPE_ENUM.
        order_status (Union[Unset, str]):  Example: TYPE_ENUM.
        reports (Union[Unset, str]):  Example: TYPE_ENUM.
        safety_and_security (Union[Unset, str]):  Example: TYPE_ENUM.
        service_policies (Union[Unset, str]):  Example: TYPE_ENUM.
        support (Union[Unset, str]):  Example: TYPE_ENUM.
        user_and_tenant_management (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    asset_manager: Union[Unset, str] = UNSET
    billing_and_invoicing: Union[Unset, str] = UNSET
    compliance: Union[Unset, str] = UNSET
    developer_tools: Union[Unset, str] = UNSET
    global_services: Union[Unset, str] = UNSET
    insights: Union[Unset, str] = UNSET
    licensing: Union[Unset, str] = UNSET
    logs: Union[Unset, str] = UNSET
    monitoring_and_troubleshooting: Union[Unset, str] = UNSET
    network_configuration: Union[Unset, str] = UNSET
    order_status: Union[Unset, str] = UNSET
    reports: Union[Unset, str] = UNSET
    safety_and_security: Union[Unset, str] = UNSET
    service_policies: Union[Unset, str] = UNSET
    support: Union[Unset, str] = UNSET
    user_and_tenant_management: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_manager = self.asset_manager

        billing_and_invoicing = self.billing_and_invoicing

        compliance = self.compliance

        developer_tools = self.developer_tools

        global_services = self.global_services

        insights = self.insights

        licensing = self.licensing

        logs = self.logs

        monitoring_and_troubleshooting = self.monitoring_and_troubleshooting

        network_configuration = self.network_configuration

        order_status = self.order_status

        reports = self.reports

        safety_and_security = self.safety_and_security

        service_policies = self.service_policies

        support = self.support

        user_and_tenant_management = self.user_and_tenant_management

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_manager is not UNSET:
            field_dict["assetManager"] = asset_manager
        if billing_and_invoicing is not UNSET:
            field_dict["billingAndInvoicing"] = billing_and_invoicing
        if compliance is not UNSET:
            field_dict["compliance"] = compliance
        if developer_tools is not UNSET:
            field_dict["developerTools"] = developer_tools
        if global_services is not UNSET:
            field_dict["globalServices"] = global_services
        if insights is not UNSET:
            field_dict["insights"] = insights
        if licensing is not UNSET:
            field_dict["licensing"] = licensing
        if logs is not UNSET:
            field_dict["logs"] = logs
        if monitoring_and_troubleshooting is not UNSET:
            field_dict["monitoringAndTroubleshooting"] = monitoring_and_troubleshooting
        if network_configuration is not UNSET:
            field_dict["networkConfiguration"] = network_configuration
        if order_status is not UNSET:
            field_dict["orderStatus"] = order_status
        if reports is not UNSET:
            field_dict["reports"] = reports
        if safety_and_security is not UNSET:
            field_dict["safetyAndSecurity"] = safety_and_security
        if service_policies is not UNSET:
            field_dict["servicePolicies"] = service_policies
        if support is not UNSET:
            field_dict["support"] = support
        if user_and_tenant_management is not UNSET:
            field_dict["userAndTenantManagement"] = user_and_tenant_management

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_manager = d.pop("assetManager", UNSET)

        billing_and_invoicing = d.pop("billingAndInvoicing", UNSET)

        compliance = d.pop("compliance", UNSET)

        developer_tools = d.pop("developerTools", UNSET)

        global_services = d.pop("globalServices", UNSET)

        insights = d.pop("insights", UNSET)

        licensing = d.pop("licensing", UNSET)

        logs = d.pop("logs", UNSET)

        monitoring_and_troubleshooting = d.pop("monitoringAndTroubleshooting", UNSET)

        network_configuration = d.pop("networkConfiguration", UNSET)

        order_status = d.pop("orderStatus", UNSET)

        reports = d.pop("reports", UNSET)

        safety_and_security = d.pop("safetyAndSecurity", UNSET)

        service_policies = d.pop("servicePolicies", UNSET)

        support = d.pop("support", UNSET)

        user_and_tenant_management = d.pop("userAndTenantManagement", UNSET)

        get_v1_users_id_groups_response_200_groups_item_permissions = cls(
            asset_manager=asset_manager,
            billing_and_invoicing=billing_and_invoicing,
            compliance=compliance,
            developer_tools=developer_tools,
            global_services=global_services,
            insights=insights,
            licensing=licensing,
            logs=logs,
            monitoring_and_troubleshooting=monitoring_and_troubleshooting,
            network_configuration=network_configuration,
            order_status=order_status,
            reports=reports,
            safety_and_security=safety_and_security,
            service_policies=service_policies,
            support=support,
            user_and_tenant_management=user_and_tenant_management,
        )

        get_v1_users_id_groups_response_200_groups_item_permissions.additional_properties = d
        return get_v1_users_id_groups_response_200_groups_item_permissions

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
