
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class UserClassUserPermissions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    super_admin: (bool | None) = Field(default=None, alias='SuperAdmin')
    system_config: (bool | None) = Field(default=None, alias='SystemConfig')
    class_config: (bool | None) = Field(default=None, alias='ClassConfig')
    create_tickets: (bool | None) = Field(default=None, alias='CreateTickets')
    shared_links: (bool | None) = Field(default=None, alias='SharedLinks')
    template_read: (bool | None) = Field(default=None, alias='TemplateRead')
    template_edit: (bool | None) = Field(default=None, alias='TemplateEdit')
    template_delete: (bool | None) = Field(default=None, alias='TemplateDelete')
    client_read: (bool | None) = Field(default=None, alias='ClientRead')
    client_edit: (bool | None) = Field(default=None, alias='ClientEdit')
    client_delete: (bool | None) = Field(default=None, alias='ClientDelete')
    report_read: (bool | None) = Field(default=None, alias='ReportRead')
    report_edit: (bool | None) = Field(default=None, alias='ReportEdit')
    report_delete: (bool | None) = Field(default=None, alias='ReportDelete')
    contact_read: (bool | None) = Field(default=None, alias='ContactRead')
    contact_edit: (bool | None) = Field(default=None, alias='ContactEdit')
    contact_delete: (bool | None) = Field(default=None, alias='ContactDelete')
    user_read: (bool | None) = Field(default=None, alias='UserRead')
    user_edit: (bool | None) = Field(default=None, alias='UserEdit')
    user_delete: (bool | None) = Field(default=None, alias='UserDelete')
    tool_read: (bool | None) = Field(default=None, alias='ToolRead')
    tool_edit: (bool | None) = Field(default=None, alias='ToolEdit')
    tool_delete: (bool | None) = Field(default=None, alias='ToolDelete')
    script_read: (bool | None) = Field(default=None, alias='ScriptRead')
    script_edit: (bool | None) = Field(default=None, alias='ScriptEdit')
    script_delete: (bool | None) = Field(default=None, alias='ScriptDelete')
    manage_groups: (bool | None) = Field(default=None, alias='ManageGroups')
    dash_ticketing: (bool | None) = Field(default=None, alias='DashTicketing')
    dash_time: (bool | None) = Field(default=None, alias='DashTime')
    dash_manage: (bool | None) = Field(default=None, alias='DashManage')
    dash_trending: (bool | None) = Field(default=None, alias='DashTrending')
    dash_overview: (bool | None) = Field(default=None, alias='DashOverview')
    hud_update: (bool | None) = Field(default=None, alias='HUDUpdate')
    hud_show_all: (bool | None) = Field(default=None, alias='HUDShowAll')
    data_view_update: (bool | None) = Field(default=None, alias='DataViewUpdate')
    data_view_delete: (bool | None) = Field(default=None, alias='DataViewDelete')
    data_view_show_all: (bool | None) = Field(default=None, alias='DataViewShowAll')
    users_show_all: (bool | None) = Field(default=None, alias='UsersShowAll')
    user_class_create: (bool | None) = Field(default=None, alias='UserClassCreate')
    user_class_update: (bool | None) = Field(default=None, alias='UserClassUpdate')
    patch_manager_config: (bool | None) = Field(default=None, alias='PatchManagerConfig')
    reports_create: (bool | None) = Field(default=None, alias='ReportsCreate')
    probe_template_execute: (bool | None) = Field(default=None, alias='ProbeTemplateExecute')
    scheduled_scripts_update: (bool | None) = Field(default=None, alias='ScheduledScriptsUpdate')
    clients_show_all: (bool | None) = Field(default=None, alias='ClientsShowAll')
    show_passwords: (bool | None) = Field(default=None, alias='ShowPasswords')
    locations_show_all: (bool | None) = Field(default=None, alias='LocationsShowAll')
    computers_create: (bool | None) = Field(default=None, alias='ComputersCreate')
    computers_update: (bool | None) = Field(default=None, alias='ComputersUpdate')
    computers_delete: (bool | None) = Field(default=None, alias='ComputersDelete')
    computers_show_all: (bool | None) = Field(default=None, alias='ComputersShowAll')
    computers_force_update: (bool | None) = Field(default=None, alias='ComputersForceUpdate')
    network_device_update: (bool | None) = Field(default=None, alias='NetworkDeviceUpdate')
    network_device_delete: (bool | None) = Field(default=None, alias='NetworkDeviceDelete')
    network_device_show_all: (bool | None) = Field(default=None, alias='NetworkDeviceShowAll')
    retired_assets_delete: (bool | None) = Field(default=None, alias='RetiredAssetsDelete')
    groups_create: (bool | None) = Field(default=None, alias='GroupsCreate')
    groups_delete: (bool | None) = Field(default=None, alias='GroupsDelete')
    groups_show_all: (bool | None) = Field(default=None, alias='GroupsShowAll')
    groups_schedule_script: (bool | None) = Field(default=None, alias='GroupsScheduleScript')
    group_monitors_update: (bool | None) = Field(default=None, alias='GroupMonitorsUpdate')
    group_info_update: (bool | None) = Field(default=None, alias='GroupInfoUpdate')
    group_managed_services: (bool | None) = Field(default=None, alias='GroupManagedServices')
    remote_monitors_create: (bool | None) = Field(default=None, alias='RemoteMonitorsCreate')
    remote_monitors_delete: (bool | None) = Field(default=None, alias='RemoteMonitorsDelete')
    internal_monitors_create: (bool | None) = Field(default=None, alias='InternalMonitorsCreate')
    internal_monitors_update: (bool | None) = Field(default=None, alias='InternalMonitorsUpdate')
    internal_monitors_delete: (bool | None) = Field(default=None, alias='InternalMonitorsDelete')
    alerts_update: (bool | None) = Field(default=None, alias='AlertsUpdate')
    alerts_delete_all: (bool | None) = Field(default=None, alias='AlertsDeleteAll')
    tickets_read: (bool | None) = Field(default=None, alias='TicketsRead')
    tickets_update: (bool | None) = Field(default=None, alias='TicketsUpdate')
    tickets_delete: (bool | None) = Field(default=None, alias='TicketsDelete')
    tickets_request: (bool | None) = Field(default=None, alias='TicketsRequest')
    searches_read: (bool | None) = Field(default=None, alias='SearchesRead')
    searches_update: (bool | None) = Field(default=None, alias='SearchesUpdate')
    searches_delete: (bool | None) = Field(default=None, alias='SearchesDelete')
    patch_manager_read: (bool | None) = Field(default=None, alias='PatchManagerRead')
    patch_manager_update: (bool | None) = Field(default=None, alias='PatchManagerUpdate')
    language_pack_editor: (bool | None) = Field(default=None, alias='LanguagePackEditor')
    managed_service_catalog: (bool | None) = Field(default=None, alias='ManagedServiceCatalog')
    navigation_menu_update: (bool | None) = Field(default=None, alias='NavigationMenuUpdate')
    rss_feed_read: (bool | None) = Field(default=None, alias='RSSFeedRead')
    rss_feed_update: (bool | None) = Field(default=None, alias='RSSFeedUpdate')
    links_delete: (bool | None) = Field(default=None, alias='LinksDelete')
    plugin_manager: (bool | None) = Field(default=None, alias='PluginManager')
    solution_center: (bool | None) = Field(default=None, alias='SolutionCenter')
    database_execute: (bool | None) = Field(default=None, alias='DatabaseExecute')
    server_status: (bool | None) = Field(default=None, alias='ServerStatus')
    manage_audits: (bool | None) = Field(default=None, alias='ManageAudits')
    manage_remote_commands: (bool | None) = Field(default=None, alias='ManageRemoteCommands')
    manage_service_logs: (bool | None) = Field(default=None, alias='ManageServiceLogs')
    manage_outdated: (bool | None) = Field(default=None, alias='ManageOutdated')
    manage_offline_computers: (bool | None) = Field(default=None, alias='ManageOfflineComputers')
    manage_schedule_client_scripts: (bool | None) = Field(default=None, alias='ManageScheduleClientScripts')
    dashboard_config: (bool | None) = Field(default=None, alias='DashboardConfig')
    config_application_list: (bool | None) = Field(default=None, alias='ConfigApplicationList')
    config_event_black_list: (bool | None) = Field(default=None, alias='ConfigEventBlackList')
    quick_connect: (bool | None) = Field(default=None, alias='QuickConnect')
    permissions_update: (bool | None) = Field(default=None, alias='PermissionsUpdate')
    user_class_read: (bool | None) = Field(default=None, alias='UserClassRead')
    user_class_delete: (bool | None) = Field(default=None, alias='UserClassDelete')

class ChangePasswordRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    old_password: (str | None) = Field(default=None, alias='OldPassword')
    new_password: (str | None) = Field(default=None, alias='NewPassword')

class UserPasswordResetRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    username: (str | None) = Field(default=None, alias='Username')
    password_reset_token: (str | None) = Field(default=None, alias='PasswordResetToken')
    new_password: (str | None) = Field(default=None, alias='NewPassword')

class UserAvatar(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    file_data: (str | None) = Field(default=None, alias='FileData')

class UserFolder(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_folder_id: (int | None) = Field(default=None, alias='UserFolderId')
    name: (str | None) = Field(default=None, alias='Name')
    is_sso_enabled: (bool | None) = Field(default=None, alias='IsSsoEnabled')

class UserSingleSignOnStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    sso_status_id: (int | None) = Field(default=None, alias='SsoStatusId')
    status_name: (str | None) = Field(default=None, alias='StatusName')

class UserLockoutInfo(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_name: (str | None) = Field(default=None, alias='UserName')
    user_id: (int | None) = Field(default=None, alias='UserId')
    last_ip_address: (str | None) = Field(default=None, alias='LastIPAddress')
    is_locked: (bool | None) = Field(default=None, alias='IsLocked')
    failed_login_count: (int | None) = Field(default=None, alias='FailedLoginCount')
    last_fail_date_utc: (datetime | None) = Field(default=None, alias='LastFailDateUtc')
    lock_out_expiration_date_utc: (datetime | None) = Field(default=None, alias='LockOutExpirationDateUtc')

class UserClass(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_class_id: (int | None) = Field(default=None, alias='UserClassId')
    name: (str | None) = Field(default=None, alias='Name')
    permissions: (UserClassUserPermissions | None) = Field(default=None, alias='Permissions')
    binary_extension_permissions: (list[Binary.BinaryExtensionPermission] | None) = Field(default=None, alias='BinaryExtensionPermissions')
    web_extension_claims: (list[WebExtensions.WebExtensionPermission] | None) = Field(default=None, alias='WebExtensionClaims')

class UserAccess(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: (int | None) = Field(default=None, alias='UserId')
    user_permissions: (list[str] | None) = Field(default=None, alias='UserPermissions')
    plugin_permissions: (list[Binary.UserBinaryExtensionPermission] | None) = Field(default=None, alias='PluginPermissions')
    web_extension_claims: (list[WebExtensions.UserExtensionClaimType] | None) = Field(default=None, alias='WebExtensionClaims')

class User(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: (int | None) = Field(default=None, alias='UserId')
    name: (str | None) = Field(default=None, alias='Name')
    first_name: (str | None) = Field(default=None, alias='FirstName')
    last_name: (str | None) = Field(default=None, alias='LastName')
    last_successful_login: (datetime | None) = Field(default=None, alias='LastSuccessfulLogin')
    password: (str | None) = Field(default=None, alias='Password')
    folder: (UserFolder | None) = Field(default=None, alias='Folder')
    email_address: (str | None) = Field(default=None, alias='EmailAddress')
    auditing_level: (int | None) = Field(default=None, alias='AuditingLevel')
    command_level: (int | None) = Field(default=None, alias='CommandLevel')
    uses_ticket_based_security: (bool | None) = Field(default=None, alias='UsesTicketBasedSecurity')
    new_ticket_display_limit: (int | None) = Field(default=None, alias='NewTicketDisplayLimit')
    open_ticket_limit: (int | None) = Field(default=None, alias='OpenTicketLimit')
    is_integrator: (bool | None) = Field(default=None, alias='IsIntegrator')
    is_locked: (bool | None) = Field(default=None, alias='IsLocked')
    is_ticket_router: (bool | None) = Field(default=None, alias='IsTicketRouter')
    is_ticket_supervisor: (bool | None) = Field(default=None, alias='IsTicketSupervisor')
    ticket_level: (Ticketing.TicketLevel | None) = Field(default=None, alias='TicketLevel')
    requires_login_report: (bool | None) = Field(default=None, alias='RequiresLoginReport')
    requires_logout_report: (bool | None) = Field(default=None, alias='RequiresLogoutReport')
    last_updated: (datetime | None) = Field(default=None, alias='LastUpdated')
    primary_clients: (list[Clients.Client] | None) = Field(default=None, alias='PrimaryClients')
    user_classes: (list[UserClass] | None) = Field(default=None, alias='UserClasses')
    associated_groups: (list[Groups.Group] | None) = Field(default=None, alias='AssociatedGroups')
    sso_status: (UserSingleSignOnStatus | None) = Field(default=None, alias='SsoStatus')
    sso_email: (str | None) = Field(default=None, alias='SsoEmail')
    allow_legacy_api_access: (bool | None) = Field(default=None, alias='AllowLegacyApiAccess')
from .SystemExtensions import Binary
from . import Clients, Groups, Ticketing, WebExtensions