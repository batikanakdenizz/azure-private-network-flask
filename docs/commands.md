# Azure Setup Commands

## Resource Group
```bash
az group create --name MidtermProject --location francecentral
```

## Virtual Network and Subnets
```bash
# Create VNet
az network vnet create \
  --resource-group MidtermProject \
  --name midterm-vnet \
  --address-prefix 10.0.0.0/16 \
  --location francecentral

# Create subnet for App Service
az network vnet subnet create \
  --resource-group MidtermProject \
  --vnet-name midterm-vnet \
  --name app-service-subnet \
  --address-prefix 10.0.1.0/24 \
  --service-endpoints Microsoft.Web

# Create subnet for PostgreSQL
az network vnet subnet create \
  --resource-group MidtermProject \
  --vnet-name midterm-vnet \
  --name postgresql-subnet \
  --address-prefix 10.0.2.0/24 \
  --service-endpoints Microsoft.Storage

# Create subnet for Key Vault private endpoint
az network vnet subnet create \
  --resource-group MidtermProject \
  --vnet-name midterm-vnet \
  --name keyvault-subnet \
  --address-prefix 10.0.3.0/24 \
  --disable-private-endpoint-network-policies true

# Create subnet for VM (for SSH access)
az network vnet subnet create \
  --resource-group MidtermProject \
  --vnet-name midterm-vnet \
  --name vm-subnet \
  --address-prefix 10.0.4.0/24
```

## PostgreSQL Flexible Server (Private)
```bash
az postgres flexible-server create \
  --resource-group MidtermProject \
  --name midterm-postgres \
  --location francecentral \
  --admin-user postgresadmin \
  --admin-password <password> \
  --sku-name Standard_B1ms \
  --tier Burstable \
  --storage-size 32 \
  --version 15 \
  --vnet midterm-vnet \
  --subnet postgresql-subnet \
  --private-dns-zone midterm-postgres.private.postgres.database.azure.com \
  --yes
```

## Virtual Machine for SSH Access
```bash
# Create VM
az vm create \
  --resource-group MidtermProject \
  --name midterm-vm \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --vnet-name midterm-vnet \
  --subnet vm-subnet \
  --size Standard_B1s \
  --public-ip-sku Standard

# Open SSH port
az vm open-port --resource-group MidtermProject --name midterm-vm --port 22
```

## App Service (Private)
```bash
# Create App Service Plan
az appservice plan create \
  --resource-group MidtermProject \
  --name midterm-asp \
  --location francecentral \
  --sku B1 \
  --is-linux

# Create Web App
az webapp create \
  --resource-group MidtermProject \
  --plan midterm-asp \
  --name se4453-group7-webapp \
  --runtime "PYTHON:3.9" \
  --deployment-local-git

# Enable VNet integration
az webapp vnet-integration add \
  --resource-group MidtermProject \
  --name se4453-group7-webapp \
  --vnet midterm-vnet \
  --subnet app-service-subnet
```

## Key Vault (via Portal, but CLI commands for reference)
```bash
# Create Key Vault
az keyvault create \
  --name midterm-kv \
  --resource-group MidtermProject \
  --location francecentral \
  --enabled-for-deployment true \
  --enabled-for-template-deployment true

# Create private endpoint for Key Vault
az network private-endpoint create \
  --name kv-private-endpoint \
  --resource-group MidtermProject \
  --vnet-name midterm-vnet \
  --subnet keyvault-subnet \
  --private-connection-resource-id $(az keyvault show --name midterm-kv --resource-group MidtermProject --query id -o tsv) \
  --group-id vault \
  --connection-name kv-connection

# Add secrets to Key Vault
az keyvault secret set --vault-name midterm-kv --name db-host --value midterm-postgres.postgres.database.azure.com
az keyvault secret set --vault-name midterm-kv --name db-name --value postgres
az keyvault secret set --vault-name midterm-kv --name db-user --value postgresadmin
az keyvault secret set --vault-name midterm-kv --name db-password --value <password>
az keyvault secret set --vault-name midterm-kv --name db-port --value 5432
```

## App Service Configuration
```bash
# Set environment variables from Key Vault
az webapp config appsettings set \
  --resource-group MidtermProject \
  --name se4453-group7-webapp \
  --setting DB_HOST=@Microsoft.KeyVault(SecretUri=https://midterm-kv.vault.azure.net/secrets/db-host) \
  --setting DB_NAME=@Microsoft.KeyVault(SecretUri=https://midterm-kv.vault.azure.net/secrets/db-name) \
  --setting DB_USER=@Microsoft.KeyVault(SecretUri=https://midterm-kv.vault.azure.net/secrets/db-user) \
  --setting DB_PASSWORD=@Microsoft.KeyVault(SecretUri=https://midterm-kv.vault.azure.net/secrets/db-password) \
  --setting DB_PORT=@Microsoft.KeyVault(SecretUri=https://midterm-kv.vault.azure.net/secrets/db-port)

# Enable managed identity
az webapp identity assign \
  --resource-group MidtermProject \
  --name se4453-group7-webapp

# Grant access to Key Vault
az keyvault set-policy \
  --name midterm-kv \
  --resource-group MidtermProject \
  --object-id $(az webapp identity show --resource-group MidtermProject --name se4453-group7-webapp --query principalId -o tsv) \
  --secret-permissions get list
```

## Deployment
```bash
# Add GitHub remote if not already
git remote add origin https://github.com/batikanakdenizz/SE4453-Midterm-Project.git

# Push to main branch (trunk)
git checkout -b main
git merge feature/flask-app
git push origin main

# Deploy to App Service
az webapp deployment source config \
  --resource-group MidtermProject \
  --name se4453-group7-webapp \
  --repo-url https://github.com/batikanakdenizz/SE4453-Midterm-Project \
  --branch main \
  --git-token <your-github-token>
```