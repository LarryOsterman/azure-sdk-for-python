# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ManagedLabsClientConfiguration
from .operations import ProviderOperationsOperations
from .operations import GlobalUsersOperations
from .operations import LabAccountsOperations
from .operations import Operations
from .operations import GalleryImagesOperations
from .operations import LabsOperations
from .operations import EnvironmentSettingsOperations
from .operations import EnvironmentsOperations
from .operations import UsersOperations
from .. import models


class ManagedLabsClient(object):
    """The Managed Labs Client.

    :ivar provider_operations: ProviderOperationsOperations operations
    :vartype provider_operations: azure.mgmt.labservices.aio.operations.ProviderOperationsOperations
    :ivar global_users: GlobalUsersOperations operations
    :vartype global_users: azure.mgmt.labservices.aio.operations.GlobalUsersOperations
    :ivar lab_accounts: LabAccountsOperations operations
    :vartype lab_accounts: azure.mgmt.labservices.aio.operations.LabAccountsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.labservices.aio.operations.Operations
    :ivar gallery_images: GalleryImagesOperations operations
    :vartype gallery_images: azure.mgmt.labservices.aio.operations.GalleryImagesOperations
    :ivar labs: LabsOperations operations
    :vartype labs: azure.mgmt.labservices.aio.operations.LabsOperations
    :ivar environment_settings: EnvironmentSettingsOperations operations
    :vartype environment_settings: azure.mgmt.labservices.aio.operations.EnvironmentSettingsOperations
    :ivar environments: EnvironmentsOperations operations
    :vartype environments: azure.mgmt.labservices.aio.operations.EnvironmentsOperations
    :ivar users: UsersOperations operations
    :vartype users: azure.mgmt.labservices.aio.operations.UsersOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ManagedLabsClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.provider_operations = ProviderOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.global_users = GlobalUsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.lab_accounts = LabAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_images = GalleryImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.labs = LabsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environment_settings = EnvironmentSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environments = EnvironmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ManagedLabsClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
