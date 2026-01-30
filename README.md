**Cloud CostSense**

**Overview**

Cloud CostSense is a CLI-based multi-cloud cost comparison tool developed during the Caze Labs Internship Programme.
The application helps users analyze, compare, and evaluate Virtual Machine (VM) pricing across major cloud providers before deployment, enabling informed cost-effective decisions.

The tool currently focuses on pre-deployment cost visibility by fetching pricing data from cloud provider APIs, normalizing it, and storing it locally for fast and secure analysis.


**Key Objectives**

- Provide clear visibility into cloud infrastructure costs
- Enable cost comparison across multiple cloud providers
- Help users identify the most cost-effective VM options
- Support filtering based on resource requirements
- Generate structured outputs suitable for reporting and demos


**Features**

- View all available VM pricing
- Identify the cheapest VM across providers
- Filter VMs by:

Cloud provider (AWS / Azure / GCP)
Region
Maximum price per hour
Minimum vCPU
Minimum memory
- Store pricing data locally in SQLite for fast querying
- Menu-driven CLI interface
- Report generation support
- Modular and extensible architecture


**Limitations**

- GCP pricing APIs are unreliable and may not always return data
- Pricing values are subject to change by cloud providers
- Current version focuses on VM pricing only


**Future Enhancements**

- Stable GCP pricing integration
- Support for additional resources (DB, Storage)
- Web UI dashboard
- Scheduled price refresh (cron job)
- Multi-account cloud support
- Visualization dashboards



**Internship Context**

This project was developed as part of the Caze Labs Internship Programme, focusing on:
Cloud cost optimization concepts

- API integration-
- Data normalization
- CLI application design
- Real-world cloud engineering challenges


**Conclusion**

Cloud CostSense demonstrates a practical approach to multi-cloud cost analysis, providing users with clear cost visibility before deployment and forming a strong foundation for future expansion into a full-fledged cloud cost optimization platform.
