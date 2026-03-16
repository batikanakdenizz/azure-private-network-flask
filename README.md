# SE4453 Midterm Project - Group 7

## Overview
This project implements a Flask web application deployed on Azure with secure infrastructure components. The application connects to a PostgreSQL database and uses Azure Key Vault for secret management.

## Features
- Flask web API with database connectivity
- Private Azure App Service
- Private PostgreSQL database (accessed via VM SSH)
- Azure Key Vault with private endpoint for secrets
- Trunk-based Git workflow

## Local Development
1. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set environment variables:
   ```bash
   export DB_HOST=localhost
   export DB_NAME=your_db
   export DB_USER=your_user
   export DB_PASSWORD=your_password
   export DB_PORT=5432
   export APP_ENV=development
   ```

4. Run the app:
   ```bash
   python app.py
   ```

## Azure Deployment
See `docs/commands.md` for complete Azure setup instructions.

## Architecture
See `docs/architecture.md` for detailed architecture overview.

## Resources
See `docs/resources.md` for list of Azure resources created.
   



