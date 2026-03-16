# Azure Resources

## Resource Group
- Name: MidtermProject
- Location: francecentral
- Subscription: Azure for Students

## Virtual Network
- Name: midterm-vnet
- Address Space: 10.0.0.0/16
- Subnets:
  - app-service-subnet: 10.0.1.0/24
  - postgresql-subnet: 10.0.2.0/24
  - keyvault-subnet: 10.0.3.0/24
  - vm-subnet: 10.0.4.0/24

## PostgreSQL Flexible Server
- Name: midterm-postgres
- SKU: Standard_B1ms
- Version: 15
- Admin User: postgresadmin
- Private DNS Zone: midterm-postgres.private.postgres.database.azure.com
- VNet: midterm-vnet
- Subnet: postgresql-subnet

## Virtual Machine
- Name: midterm-vm
- OS: Ubuntu 2204
- Size: Standard_B1s
- User: azureuser
- VNet: midterm-vnet
- Subnet: vm-subnet
- Public IP: Yes (for SSH access)

## App Service
- Name: se4453-group7-webapp
- Plan: midterm-asp (B1, Linux)
- Runtime: Python 3.9
- VNet Integration: midterm-vnet / app-service-subnet
- Managed Identity: Enabled
- Deployment: GitHub (main branch)

## Key Vault
- Name: midterm-kv
- Location: francecentral
- Private Endpoint: kv-private-endpoint
- Secrets:
  - db-host
  - db-name
  - db-user
  - db-password
  - db-port

## GitHub Repository
- URL: https://github.com/batikanakdenizz/SE4453-Midterm-Project
- Branch: main (trunk-based workflow)