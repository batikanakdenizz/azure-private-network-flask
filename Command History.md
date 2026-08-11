az group create --name MidtermProject --location francecentral
{
  "id": "/subscriptions/<subscription-id>/resourceGroups/MidtermProject",
  "location": "francecentral",
  "managedBy": null,
  "name": "MidtermProject",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}


az config get
Command group 'config' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
{
  "cloud": [
    {
      "name": "name",
      "source": "C:\\Users\\batik\\.azure\\config",
      "value": "AzureCloud"
    }
  ],
  "core": [
    {
      "name": "first_run",
      "source": "C:\\Users\\batik\\.azure\\config",
      "value": "yes"
    }
  ]
}

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\batik> az login
Select the account you want to log in with. For more information on login with Azure CLI, see https://go.microsoft.com/fwlink/?linkid=2271136

Retrieving tenants and subscriptions for the selection...

[Tenant and subscription selection]

No     Subscription name    Subscription ID                       Tenant
-----  -------------------  ------------------------------------  ----------------
[1] *  Azure for Students   <subscription-id>  Yasar University

The default is marked with an *; the default tenant is 'Yasar University' and subscription is 'Azure for Students' (<subscription-id>).

Select a subscription and tenant (Type a number or Enter for no changes):

Tenant: Yasar University
Subscription: Azure for Students (<subscription-id>)

[Announcements]
With the new Azure CLI login experience, you can select the subscription you want to use more easily. Learn more about it and its configuration at https://go.microsoft.com/fwlink/?linkid=2271236

If you encounter any problem, please open an issue at https://aka.ms/azclibug

[Warning] The login output has been updated. Please be aware that it no longer displays the full list of available subscriptions by default.

PS C:\Users\batik> az group show --name MidtermProject --output table
Location       Name
-------------  --------------
francecentral  MidtermProject
PS C:\Users\batik> az network vnet create `
>>   --resource-group MidtermProject `
>>   --name midterm-vnet `
>>   --location francecentral `
>>   --address-prefixes 10.0.0.0/16 `
>>   --subnet-name vm-subnet `
>>   --subnet-prefixes 10.0.1.0/24
{
  "newVNet": {
    "addressSpace": {
      "addressPrefixes": [
        "10.0.0.0/16"
      ]
    },
    "enableDdosProtection": false,
    "etag": "W/\"<guid>\"",
    "id": "/subscriptions/<subscription-id>/resourceGroups/MidtermProject/providers/Microsoft.Network/virtualNetworks/midterm-vnet",
    "location": "francecentral",
    "name": "midterm-vnet",
    "privateEndpointVNetPolicies": "Disabled",
    "provisioningState": "Succeeded",
    "resourceGroup": "MidtermProject",
    "resourceGuid": "<guid>",
    "subnets": [
      {
        "addressPrefix": "10.0.1.0/24",
        "delegations": [],
        "etag": "W/\"<guid>\"",
        "id": "/subscriptions/<subscription-id>/resourceGroups/MidtermProject/providers/Microsoft.Network/virtualNetworks/midterm-vnet/subnets/vm-subnet",
        "name": "vm-subnet",
        "privateEndpointNetworkPolicies": "Disabled",
        "privateLinkServiceNetworkPolicies": "Enabled",
        "provisioningState": "Succeeded",
        "resourceGroup": "MidtermProject",
        "type": "Microsoft.Network/virtualNetworks/subnets"
      }
    ],
    "type": "Microsoft.Network/virtualNetworks",
    "virtualNetworkPeerings": []
  }
}
PS C:\Users\batik> az network vnet show `
>>   --resource-group MidtermProject `
>>   --name midterm-vnet `
>>   --output table
EnableDdosProtection    Location       Name          PrivateEndpointVNetPolicies    ProvisioningState    ResourceGroup    ResourceGuid
----------------------  -------------  ------------  -----------------------------  -------------------  ---------------  ------------------------------------
False                   francecentral  midterm-vnet  Disabled                       Succeeded            MidtermProject   <guid>
PS C:\Users\batik> az network vnet subnet create `
>>   --resource-group MidtermProject `
>>   --vnet-name midterm-vnet `
>>   --name app-subnet `
>>   --address-prefixes 10.0.2.0/24
{
  "addressPrefix": "10.0.2.0/24",
  "delegations": [],
  "etag": "W/\"<guid>\"",
  "id": "/subscriptions/<subscription-id>/resourceGroups/MidtermProject/providers/Microsoft.Network/virtualNetworks/midterm-vnet/subnets/app-subnet",
  "name": "app-subnet",
  "privateEndpointNetworkPolicies": "Disabled",
  "privateLinkServiceNetworkPolicies": "Enabled",
  "provisioningState": "Succeeded",
  "resourceGroup": "MidtermProject",
  "type": "Microsoft.Network/virtualNetworks/subnets"
}
PS C:\Users\batik> az network vnet subnet create `
>>   --resource-group MidtermProject `
>>   --vnet-name midterm-vnet `
>>   --name private-endpoint-subnet `
>>   --address-prefixes 10.0.3.0/24
{
  "addressPrefix": "10.0.3.0/24",
  "delegations": [],
  "etag": "W/\"<guid>\"",
  "id": "/subscriptions/<subscription-id>/resourceGroups/MidtermProject/providers/Microsoft.Network/virtualNetworks/midterm-vnet/subnets/private-endpoint-subnet",
  "name": "private-endpoint-subnet",
  "privateEndpointNetworkPolicies": "Disabled",
  "privateLinkServiceNetworkPolicies": "Enabled",
  "provisioningState": "Succeeded",
  "resourceGroup": "MidtermProject",
  "type": "Microsoft.Network/virtualNetworks/subnets"
}
PS C:\Users\batik> az network vnet subnet list `
>>   --resource-group MidtermProject `
>>   --vnet-name midterm-vnet `
>>   --output table
AddressPrefix    Name                     PrivateEndpointNetworkPolicies    PrivateLinkServiceNetworkPolicies    ProvisioningState    ResourceGroup
---------------  -----------------------  --------------------------------  -----------------------------------  -------------------  ---------------
10.0.1.0/24      vm-subnet                Disabled                          Enabled                              Succeeded            MidtermProject
10.0.2.0/24      app-subnet               Disabled                          Enabled                              Succeeded            MidtermProject
10.0.3.0/24      private-endpoint-subnet  Disabled                          Enabled                              Succeeded            MidtermProject
PS C:\Users\batik> az network vnet subnet create `
>>   --resource-group MidtermProject `
>>   --vnet-name midterm-vnet `
>>   --name db-subnet `
>>   --address-prefixes 10.0.4.0/24
{
  "addressPrefix": "10.0.4.0/24",
  "delegations": [],
  "etag": "W/\"<guid>\"",
  "id": "/subscriptions/<subscription-id>/resourceGroups/MidtermProject/providers/Microsoft.Network/virtualNetworks/midterm-vnet/subnets/db-subnet",
  "name": "db-subnet",
  "privateEndpointNetworkPolicies": "Disabled",
  "privateLinkServiceNetworkPolicies": "Enabled",
  "provisioningState": "Succeeded",
  "resourceGroup": "MidtermProject",
  "type": "Microsoft.Network/virtualNetworks/subnets"
}
PS C:\Users\batik> az network vnet subnet list `
>>   --resource-group MidtermProject `
>>   --vnet-name midterm-vnet `
>>   --output table
AddressPrefix    Name                     PrivateEndpointNetworkPolicies    PrivateLinkServiceNetworkPolicies    ProvisioningState    ResourceGroup
---------------  -----------------------  --------------------------------  -----------------------------------  -------------------  ---------------
10.0.1.0/24      vm-subnet                Disabled                          Enabled                              Succeeded            MidtermProject
10.0.2.0/24      app-subnet               Disabled                          Enabled                              Succeeded            MidtermProject
10.0.3.0/24      private-endpoint-subnet  Disabled                          Enabled                              Succeeded            MidtermProject
10.0.4.0/24      db-subnet                Disabled                          Enabled                              Succeeded            MidtermProject
PS C:\Users\batik> az postgres flexible-server list-skus `
>> --location francecentral `
>> --output table
For prices please refer to https://aka.ms/postgres-pricing
SKU                 Tier             VCore    Memory    Max Disk IOPS
------------------  ---------------  -------  --------  ---------------
Standard_B1ms       Burstable        1        2 GiB     640
Standard_B2s        Burstable        2        4 GiB     1280
Standard_B2ms       Burstable        2        8 GiB     1920
Standard_B4ms       Burstable        4        16 GiB    2880
Standard_B8ms       Burstable        8        32 GiB    4320
Standard_B12ms      Burstable        12       48 GiB    4320
Standard_B16ms      Burstable        16       64 GiB    4320
Standard_B20ms      Burstable        20       80 GiB    4320
Standard_D2s_v3     GeneralPurpose   2        8 GiB     3200
Standard_D4s_v3     GeneralPurpose   4        16 GiB    6400
Standard_D8s_v3     GeneralPurpose   8        32 GiB    12800
Standard_D16s_v3    GeneralPurpose   16       64 GiB    25600
Standard_D32s_v3    GeneralPurpose   32       128 GiB   51200
Standard_D48s_v3    GeneralPurpose   48       192 GiB   76800
Standard_D64s_v3    GeneralPurpose   64       256 GiB   80000
Standard_D2ds_v4    GeneralPurpose   2        8 GiB     3200
Standard_D4ds_v4    GeneralPurpose   4        16 GiB    6400
Standard_D8ds_v4    GeneralPurpose   8        32 GiB    12800
Standard_D16ds_v4   GeneralPurpose   16       64 GiB    25600
Standard_D32ds_v4   GeneralPurpose   32       128 GiB   51200
Standard_D48ds_v4   GeneralPurpose   48       192 GiB   76800
Standard_D64ds_v4   GeneralPurpose   64       256 GiB   80000
Standard_D2ads_v5   GeneralPurpose   2        8 GiB     3200
Standard_D4ads_v5   GeneralPurpose   4        16 GiB    6400
Standard_D8ads_v5   GeneralPurpose   8        32 GiB    12800
Standard_D16ads_v5  GeneralPurpose   16       64 GiB    25600
Standard_D32ads_v5  GeneralPurpose   32       128 GiB   51200
Standard_D48ads_v5  GeneralPurpose   48       192 GiB   76800
Standard_D64ads_v5  GeneralPurpose   64       256 GiB   80000
Standard_D96ads_v5  GeneralPurpose   96       384 GiB   80000
Standard_D2ds_v5    GeneralPurpose   2        8 GiB     3750
Standard_D4ds_v5    GeneralPurpose   4        16 GiB    6400
Standard_D8ds_v5    GeneralPurpose   8        32 GiB    12800
Standard_D16ds_v5   GeneralPurpose   16       64 GiB    25600
Standard_D32ds_v5   GeneralPurpose   32       128 GiB   51200
Standard_D48ds_v5   GeneralPurpose   48       192 GiB   76800
Standard_D64ds_v5   GeneralPurpose   64       256 GiB   80000
Standard_D96ds_v5   GeneralPurpose   96       384 GiB   80000
Standard_E2s_v3     MemoryOptimized  2        16 GiB    3200
Standard_E4s_v3     MemoryOptimized  4        32 GiB    6400
Standard_E8s_v3     MemoryOptimized  8        64 GiB    12800
Standard_E16s_v3    MemoryOptimized  16       128 GiB   25600
Standard_E32s_v3    MemoryOptimized  32       256 GiB   32000
Standard_E48s_v3    MemoryOptimized  48       384 GiB   51200
Standard_E64s_v3    MemoryOptimized  64       432 GiB   76800
Standard_E2ds_v4    MemoryOptimized  2        16 GiB    3200
Standard_E4ds_v4    MemoryOptimized  4        32 GiB    6400
Standard_E8ds_v4    MemoryOptimized  8        64 GiB    12800
Standard_E16ds_v4   MemoryOptimized  16       128 GiB   25600
Standard_E20ds_v4   MemoryOptimized  20       160 GiB   32000
Standard_E32ds_v4   MemoryOptimized  32       256 GiB   51200
Standard_E48ds_v4   MemoryOptimized  48       384 GiB   76800
Standard_E64ds_v4   MemoryOptimized  64       432 GiB   80000
Standard_E2ads_v5   MemoryOptimized  2        16 GiB    3750
Standard_E4ads_v5   MemoryOptimized  4        32 GiB    6400
Standard_E8ads_v5   MemoryOptimized  8        64 GiB    12800
Standard_E16ads_v5  MemoryOptimized  16       128 GiB   25600
Standard_E20ads_v5  MemoryOptimized  20       160 GiB   32000
Standard_E32ads_v5  MemoryOptimized  32       256 GiB   51200
Standard_E48ads_v5  MemoryOptimized  48       384 GiB   76800
Standard_E64ads_v5  MemoryOptimized  64       512 GiB   80000
Standard_E96ads_v5  MemoryOptimized  96       672 GiB   80000
Standard_E2ds_v5    MemoryOptimized  2        16 GiB    3750
Standard_E4ds_v5    MemoryOptimized  4        32 GiB    6400
Standard_E8ds_v5    MemoryOptimized  8        64 GiB    12800
Standard_E16ds_v5   MemoryOptimized  16       128 GiB   25600
Standard_E20ds_v5   MemoryOptimized  20       160 GiB   32000
Standard_E32ds_v5   MemoryOptimized  32       256 GiB   51200
Standard_E48ds_v5   MemoryOptimized  48       384 GiB   76800
Standard_E64ds_v5   MemoryOptimized  64       512 GiB   80000
Standard_E96ds_v5   MemoryOptimized  96       672 GiB   80000
PS C:\Users\batik> az postgres flexible-server create `
>>   --resource-group MidtermProject `
>>   --name midterm-postgres `
>>   --location francecentral `
>>   --admin-user pgadmin `
>>   --admin-password <admin-password> `
>>   --sku-name Standard_B1ms `
>>   --tier Burstable `
>>   --version 16 `
>>   --vnet midterm-vnet `
>>   --subnet db-subnet `
>>   --private-dns-zone midterm.postgres.database.azure.com
Checking the existence of the resource group 'MidtermProject'...
Resource group 'MidtermProject' exists ? : True
You have supplied a Vnet and Subnet name. Verifying its existence...
Using existing Vnet "midterm-vnet" in resource group "MidtermProject"
Using existing Subnet "db-subnet" in resource group "MidtermProject"
Adding "Microsoft.DBforPostgreSQL/flexibleServers" delegation to the existing subnet db-subnet.
Do you want to create a new private DNS zone midterm.postgres.database.azure.com in resource group MidtermProject (y/n): y
Creating a private dns zone midterm.postgres.database.azure.com in resource group "MidtermProject"
Creating PostgreSQL Server 'midterm-postgres' in group 'MidtermProject'...
Your server 'midterm-postgres' is using sku 'Standard_B1ms' (Paid Tier). Please refer to https://aka.ms/postgres-pricing for pricing details
Make a note of your password. If you forget, you would have to reset your password with "az postgres flexible-server update -n midterm-postgres -g MidtermProject -p <new-password>".
Try using 'az postgres flexible-server connect' command to test out connection.
{
  "connectionString": "postgresql://pgadmin:<admin-password>@midterm-postgres.postgres.database.azure.com/postgres?sslmode=require",
  "databaseName": "postgres",
  "host": "midterm-postgres.postgres.database.azure.com",
  "id": "/subscriptions/<subscription-id>/resourceGroups/MidtermProject/providers/Microsoft.DBforPostgreSQL/flexibleServers/midterm-postgres",
  "location": "France Central",
  "password": "<admin-password>",
  "resourceGroup": "MidtermProject",
  "skuname": "Standard_B1ms",
  "subnetId": "/subscriptions/<subscription-id>/resourceGroups/MidtermProject/providers/Microsoft.Network/virtualNetworks/midterm-vnet/subnets/db-subnet",
  "username": "pgadmin",
  "version": "16"
}
PS C:\Users\batik> az postgres flexible-server show `
>>   --resource-group MidtermProject `
>>   --name midterm-postgres `
>>   --output table
AdministratorLogin    AvailabilityZone    FullyQualifiedDomainName                      Location        MinorVersion    Name              ReplicaCapacity    ReplicationRole    ResourceGroup    State    Version
--------------------  ------------------  --------------------------------------------  --------------  --------------  ----------------  -----------------  -----------------  ---------------  -------  ---------
pgadmin               3                   midterm-postgres.postgres.database.azure.com  France Central  12              midterm-postgres  5                  Primary            MidtermProject   Ready    16




