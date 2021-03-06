# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AKS
    from ._models_py3 import AKSProperties
    from ._models_py3 import AksComputeSecrets
    from ._models_py3 import AksNetworkingConfiguration
    from ._models_py3 import AmlCompute
    from ._models_py3 import AmlComputeNodeInformation
    from ._models_py3 import AmlComputeNodesInformation
    from ._models_py3 import AmlComputeProperties
    from ._models_py3 import AmlUserFeature
    from ._models_py3 import ClusterUpdateParameters
    from ._models_py3 import ComponentsSgqdofSchemasIdentityPropertiesUserassignedidentitiesAdditionalproperties
    from ._models_py3 import Compute
    from ._models_py3 import ComputeInstance
    from ._models_py3 import ComputeInstanceApplication
    from ._models_py3 import ComputeInstanceConnectivityEndpoints
    from ._models_py3 import ComputeInstanceCreatedBy
    from ._models_py3 import ComputeInstanceLastOperation
    from ._models_py3 import ComputeInstanceProperties
    from ._models_py3 import ComputeInstanceSshSettings
    from ._models_py3 import ComputeNodesInformation
    from ._models_py3 import ComputeResource
    from ._models_py3 import ComputeSecrets
    from ._models_py3 import DataFactory
    from ._models_py3 import DataLakeAnalytics
    from ._models_py3 import DataLakeAnalyticsProperties
    from ._models_py3 import Databricks
    from ._models_py3 import DatabricksComputeSecrets
    from ._models_py3 import DatabricksProperties
    from ._models_py3 import EncryptionProperty
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import EstimatedVMPrice
    from ._models_py3 import EstimatedVMPrices
    from ._models_py3 import HDInsight
    from ._models_py3 import HDInsightProperties
    from ._models_py3 import Identity
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import ListAmlUserFeatureResult
    from ._models_py3 import ListUsagesResult
    from ._models_py3 import ListWorkspaceKeysResult
    from ._models_py3 import ListWorkspaceQuotas
    from ._models_py3 import MachineLearningServiceError
    from ._models_py3 import NodeStateCounts
    from ._models_py3 import NotebookListCredentialsResult
    from ._models_py3 import NotebookPreparationError
    from ._models_py3 import NotebookResourceInfo
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PaginatedComputeResourcesList
    from ._models_py3 import PaginatedWorkspaceConnectionsList
    from ._models_py3 import Password
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import QuotaBaseProperties
    from ._models_py3 import QuotaUpdateParameters
    from ._models_py3 import RegistryListCredentialsResult
    from ._models_py3 import Resource
    from ._models_py3 import ResourceId
    from ._models_py3 import ResourceName
    from ._models_py3 import ResourceQuota
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import ResourceSkuZoneDetails
    from ._models_py3 import Restriction
    from ._models_py3 import SKUCapability
    from ._models_py3 import ScaleSettings
    from ._models_py3 import ServicePrincipalCredentials
    from ._models_py3 import SharedPrivateLinkResource
    from ._models_py3 import Sku
    from ._models_py3 import SkuListResult
    from ._models_py3 import SkuSettings
    from ._models_py3 import SslConfiguration
    from ._models_py3 import SystemService
    from ._models_py3 import UpdateWorkspaceQuotas
    from ._models_py3 import UpdateWorkspaceQuotasResult
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import UserAccountCredentials
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineProperties
    from ._models_py3 import VirtualMachineSecrets
    from ._models_py3 import VirtualMachineSize
    from ._models_py3 import VirtualMachineSizeListResult
    from ._models_py3 import VirtualMachineSshCredentials
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceConnection
    from ._models_py3 import WorkspaceConnectionDto
    from ._models_py3 import WorkspaceListResult
    from ._models_py3 import WorkspaceSku
    from ._models_py3 import WorkspaceUpdateParameters
except (SyntaxError, ImportError):
    from ._models import AKS  # type: ignore
    from ._models import AKSProperties  # type: ignore
    from ._models import AksComputeSecrets  # type: ignore
    from ._models import AksNetworkingConfiguration  # type: ignore
    from ._models import AmlCompute  # type: ignore
    from ._models import AmlComputeNodeInformation  # type: ignore
    from ._models import AmlComputeNodesInformation  # type: ignore
    from ._models import AmlComputeProperties  # type: ignore
    from ._models import AmlUserFeature  # type: ignore
    from ._models import ClusterUpdateParameters  # type: ignore
    from ._models import ComponentsSgqdofSchemasIdentityPropertiesUserassignedidentitiesAdditionalproperties  # type: ignore
    from ._models import Compute  # type: ignore
    from ._models import ComputeInstance  # type: ignore
    from ._models import ComputeInstanceApplication  # type: ignore
    from ._models import ComputeInstanceConnectivityEndpoints  # type: ignore
    from ._models import ComputeInstanceCreatedBy  # type: ignore
    from ._models import ComputeInstanceLastOperation  # type: ignore
    from ._models import ComputeInstanceProperties  # type: ignore
    from ._models import ComputeInstanceSshSettings  # type: ignore
    from ._models import ComputeNodesInformation  # type: ignore
    from ._models import ComputeResource  # type: ignore
    from ._models import ComputeSecrets  # type: ignore
    from ._models import DataFactory  # type: ignore
    from ._models import DataLakeAnalytics  # type: ignore
    from ._models import DataLakeAnalyticsProperties  # type: ignore
    from ._models import Databricks  # type: ignore
    from ._models import DatabricksComputeSecrets  # type: ignore
    from ._models import DatabricksProperties  # type: ignore
    from ._models import EncryptionProperty  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import EstimatedVMPrice  # type: ignore
    from ._models import EstimatedVMPrices  # type: ignore
    from ._models import HDInsight  # type: ignore
    from ._models import HDInsightProperties  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import KeyVaultProperties  # type: ignore
    from ._models import ListAmlUserFeatureResult  # type: ignore
    from ._models import ListUsagesResult  # type: ignore
    from ._models import ListWorkspaceKeysResult  # type: ignore
    from ._models import ListWorkspaceQuotas  # type: ignore
    from ._models import MachineLearningServiceError  # type: ignore
    from ._models import NodeStateCounts  # type: ignore
    from ._models import NotebookListCredentialsResult  # type: ignore
    from ._models import NotebookPreparationError  # type: ignore
    from ._models import NotebookResourceInfo  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PaginatedComputeResourcesList  # type: ignore
    from ._models import PaginatedWorkspaceConnectionsList  # type: ignore
    from ._models import Password  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import QuotaBaseProperties  # type: ignore
    from ._models import QuotaUpdateParameters  # type: ignore
    from ._models import RegistryListCredentialsResult  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceId  # type: ignore
    from ._models import ResourceName  # type: ignore
    from ._models import ResourceQuota  # type: ignore
    from ._models import ResourceSkuLocationInfo  # type: ignore
    from ._models import ResourceSkuZoneDetails  # type: ignore
    from ._models import Restriction  # type: ignore
    from ._models import SKUCapability  # type: ignore
    from ._models import ScaleSettings  # type: ignore
    from ._models import ServicePrincipalCredentials  # type: ignore
    from ._models import SharedPrivateLinkResource  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SkuListResult  # type: ignore
    from ._models import SkuSettings  # type: ignore
    from ._models import SslConfiguration  # type: ignore
    from ._models import SystemService  # type: ignore
    from ._models import UpdateWorkspaceQuotas  # type: ignore
    from ._models import UpdateWorkspaceQuotasResult  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageName  # type: ignore
    from ._models import UserAccountCredentials  # type: ignore
    from ._models import VirtualMachine  # type: ignore
    from ._models import VirtualMachineProperties  # type: ignore
    from ._models import VirtualMachineSecrets  # type: ignore
    from ._models import VirtualMachineSize  # type: ignore
    from ._models import VirtualMachineSizeListResult  # type: ignore
    from ._models import VirtualMachineSshCredentials  # type: ignore
    from ._models import Workspace  # type: ignore
    from ._models import WorkspaceConnection  # type: ignore
    from ._models import WorkspaceConnectionDto  # type: ignore
    from ._models import WorkspaceListResult  # type: ignore
    from ._models import WorkspaceSku  # type: ignore
    from ._models import WorkspaceUpdateParameters  # type: ignore

from ._azure_machine_learning_workspaces_enums import (
    AllocationState,
    ApplicationSharingPolicy,
    BillingCurrency,
    ComputeInstanceState,
    ComputeType,
    EncryptionStatus,
    NodeState,
    OperationName,
    OperationStatus,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    QuotaUnit,
    ReasonCode,
    RemoteLoginPortPublicAccess,
    ResourceIdentityType,
    SshPublicAccess,
    SslConfigurationStatus,
    Status,
    UnderlyingResourceAction,
    UnitOfMeasure,
    UsageUnit,
    VMPriceOSType,
    VMTier,
    VmPriority,
)

__all__ = [
    'AKS',
    'AKSProperties',
    'AksComputeSecrets',
    'AksNetworkingConfiguration',
    'AmlCompute',
    'AmlComputeNodeInformation',
    'AmlComputeNodesInformation',
    'AmlComputeProperties',
    'AmlUserFeature',
    'ClusterUpdateParameters',
    'ComponentsSgqdofSchemasIdentityPropertiesUserassignedidentitiesAdditionalproperties',
    'Compute',
    'ComputeInstance',
    'ComputeInstanceApplication',
    'ComputeInstanceConnectivityEndpoints',
    'ComputeInstanceCreatedBy',
    'ComputeInstanceLastOperation',
    'ComputeInstanceProperties',
    'ComputeInstanceSshSettings',
    'ComputeNodesInformation',
    'ComputeResource',
    'ComputeSecrets',
    'DataFactory',
    'DataLakeAnalytics',
    'DataLakeAnalyticsProperties',
    'Databricks',
    'DatabricksComputeSecrets',
    'DatabricksProperties',
    'EncryptionProperty',
    'ErrorDetail',
    'ErrorResponse',
    'EstimatedVMPrice',
    'EstimatedVMPrices',
    'HDInsight',
    'HDInsightProperties',
    'Identity',
    'KeyVaultProperties',
    'ListAmlUserFeatureResult',
    'ListUsagesResult',
    'ListWorkspaceKeysResult',
    'ListWorkspaceQuotas',
    'MachineLearningServiceError',
    'NodeStateCounts',
    'NotebookListCredentialsResult',
    'NotebookPreparationError',
    'NotebookResourceInfo',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PaginatedComputeResourcesList',
    'PaginatedWorkspaceConnectionsList',
    'Password',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'QuotaBaseProperties',
    'QuotaUpdateParameters',
    'RegistryListCredentialsResult',
    'Resource',
    'ResourceId',
    'ResourceName',
    'ResourceQuota',
    'ResourceSkuLocationInfo',
    'ResourceSkuZoneDetails',
    'Restriction',
    'SKUCapability',
    'ScaleSettings',
    'ServicePrincipalCredentials',
    'SharedPrivateLinkResource',
    'Sku',
    'SkuListResult',
    'SkuSettings',
    'SslConfiguration',
    'SystemService',
    'UpdateWorkspaceQuotas',
    'UpdateWorkspaceQuotasResult',
    'Usage',
    'UsageName',
    'UserAccountCredentials',
    'VirtualMachine',
    'VirtualMachineProperties',
    'VirtualMachineSecrets',
    'VirtualMachineSize',
    'VirtualMachineSizeListResult',
    'VirtualMachineSshCredentials',
    'Workspace',
    'WorkspaceConnection',
    'WorkspaceConnectionDto',
    'WorkspaceListResult',
    'WorkspaceSku',
    'WorkspaceUpdateParameters',
    'AllocationState',
    'ApplicationSharingPolicy',
    'BillingCurrency',
    'ComputeInstanceState',
    'ComputeType',
    'EncryptionStatus',
    'NodeState',
    'OperationName',
    'OperationStatus',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ProvisioningState',
    'QuotaUnit',
    'ReasonCode',
    'RemoteLoginPortPublicAccess',
    'ResourceIdentityType',
    'SshPublicAccess',
    'SslConfigurationStatus',
    'Status',
    'UnderlyingResourceAction',
    'UnitOfMeasure',
    'UsageUnit',
    'VMPriceOSType',
    'VMTier',
    'VmPriority',
]
