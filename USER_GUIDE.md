Cloud CostSense
1. Overview
Cloud CostSense is a CLI-based multi-cloud cost analysis tool developed to help users understand, compare, and analyze cloud infrastructure pricing across different cloud providers.
The tool focuses on Virtual Machine (VM) pricing and enables users to:
a) View VM pricing details
b) Compare costs across regions and providers
c) Identify the cheapest VM options
d) Filter resources based on user requirements
e) Generate reports for analysis and presentation
This application is designed as a pre-deployment cost comparison utility, helping users make informed decisions before selecting a cloud provider.

2. Project Architecture
The project follows a modular and layered architecture:
a)API Layer
  Fetches pricing data from cloud providers (AWS, Azure, GCP).
b)Data Storage Layer
  Stores normalized pricing data in a local SQLite database for fast querying and offline access.
c)Business Logic Layer
  Handles filtering, comparison, and aggregation of VM pricing.
d)CLI Interface Layer
  Provides an interactive menu-based interface for users.

This design ensures:
Better performance (local DB queries)
Reduced API dependency
Clear separation of responsibilities

3. Prerequisites
Before running the project, ensure the following are installed:
Python 3.9 or later
pip (Python package manager)
* Internet connection (for API data fetch)
* AWS credentials (for AWS pricing API access)
Required Python packages:
boto3
requests
tabulate
sqlite3

4. Environment Setup
Step 1: Create and Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate 

Step 2: Install Dependencies
pip install boto3 requests tabulate

Step 3: Configure Environment Variables
Create a .env file and add:
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1

5. Loading Cloud Pricing Data
a)AWS Pricing Load
cd db
python load_aws_api.py
This script:
- Fetches EC2 pricing from AWS Pricing API
- Normalizes the data
- Stores it in `cloud_costs.db`
b)Azure Pricing Load
python load_azure_api.py
Uses Azure Retail Prices API (public endpoint) to fetch VM pricing.
c)GCP Pricing Load
python load_gcp_api.py
Fetches VM pricing data from GCP public pricing catalogs (where accessible).

6. Running the Application
i. Option A: Argument-Based CLI (main.py)
Show All VM Pricing
- python main.py
Find Cheapest VM
- python main.py --cheapest
Filter by Provider
- python main.py --provider AWS
Filter by Region
- python main.py --region "Asia Pacific (Tokyo)"
Filter by CPU, Memory, and Price
- python main.py --min-vcpu 4 --min-memory 16 --max-price 1.0

ii. Option B: Menu-Based CLI
python cli/menu_cli.py
Menu Options:
1. Show all VM pricing
2. Show cheapest VM
3. Filter VM options
4. Generate report
5. Exit
The menu-driven interface is designed for non-technical users and live demos.

7. Filtering Capabilities
The application supports filtering by:
* Cloud Provider (AWS / Azure / GCP)
* Region
* Minimum vCPU
* Minimum Memory (GB)
* Maximum Price per Hour
This enables precise cost comparisons tailored to user requirements.

8. Report Generation
The Generate Report option:
- Extracts filtered or full pricing data
- Saves results as CSV/text files in the `exports/` folder

9. Key Use Cases
- Pre-deployment cloud cost comparison
- Identifying low-cost VM options
- Cost optimization analysis
10. Limitations
- Azure and GCP pricing APIs may have regional or network limitations
- Real-time pricing refresh depends on API availability
- Currently focused on VM pricing only

11. Future Enhancements
- Automated daily pricing refresh (cache scheduler)
- Support for additional cloud services (SQL, Storage)
- Web-based UI
- Visualization dashboards
- Multi-account support

12. Conclusion
Cloud CostSense provides a practical, scalable, and extensible solution for cloud cost comparison.
By combining real cloud pricing APIs, local database caching, and an interactive CLI, the tool demonstrates a strong foundation for enterprise-level cost analysis systems.

