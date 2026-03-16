# Architecture Overview

## Project Overview
This is the midterm project for Group 7 in SE4453. The application is a Flask-based web service that connects to a PostgreSQL database, with secrets managed through Azure Key Vault.

## Git Workflow
- **Trunk-Based Development**: All development happens on the main branch. Feature branches are short-lived and merged back quickly. No long-running branches.

## Azure Resources
- **Resource Group**: MidtermProject (location: francecentral)
- **App Service**: Private App Service created via CLI, deployed from GitHub repo
- **PostgreSQL**: Private PostgreSQL Flexible Server created via CLI, accessed over VM SSH
- **Key Vault**: Created via Portal with Private Endpoint for secret management

## Application Architecture
- **Flask App**: Simple web API with database connectivity test
- **Database**: PostgreSQL for data storage
- **Secrets**: Stored in Key Vault, accessed by App Service via Managed Identity

## Network Security
- All resources configured with private endpoints/VNet integration for secure access
- No public IPs exposed