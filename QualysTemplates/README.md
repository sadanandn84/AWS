# Create Qualys Insights in AWS Security Hub
CloudFormation template to create Qualys Specific Insights in AWS Security Hub

# License
**THIS SCRIPT IS PROVIDED TO YOU "AS IS." TO THE EXTENT PERMITTED BY LAW, QUALYS HEREBY DISCLAIMS ALL WARRANTIES AND LIABILITY FOR THE PROVISION OR USE OF THIS SCRIPT. IN NO EVENT SHALL THESE SCRIPTS BE DEEMED TO BE CLOUD SERVICES AS PROVIDED BY QUALYS.**

# Usage
Use CloudFormation Template to create AWS security hub insights specific to Qualys. The deplyoment of this cloud formation template will create 4 specific insights as mentioned in https://discussions.qualys.com/docs/DOC-6588-qualys-integration-with-aws-security-hub.

# Pre-requisites
1. AWS Security hub and Qualys Integration should be enabled. Please note as Security Hub is a regional service, ensure to enable Qualys: Vulnerability Management in desired AWS region.
2. Qualys findings should be available in AWS Security Hub.
3. User should have sufficient Permissions to create CloudFormation Stack in AWS console.

# Template workflow and resources
Resources used in this template:
1. Lambda function
2. Lambda Executione role (IAM)

Workflow:
1. A lambda function to create Qualys specific insights in AWS Security Hub.
2. This template will create a Lambda execution role in IAM. This role is granted with permission based on "Least Privilege Principle" to create only Insights within Security hub. This is a service role which will be associated with the Lambda function created as mentioned in #1.
3. After invocation of the Lambda function, insights will be created within AWS security hub.

for eg:  ***(i)   A user has enabled Qualys: Vulnerability Management product in AWS security Hub in N Virginia (us-east-1) region.
         (ii)  User raises request to Qualys support for enabling Qualys Integration with AWS Security Hub (Please refer the Link for
         more details about enabling Qualys Integration with AWS Security Hub)
         (iii) Ensure, Qualys Vulnerability findings are available within security hub.
         (iv)  Deploy the cloud formation template provided to create Qualys specific insights in Security Hub.
         (v)   4 insights specific to Qualys will be created i.e "Instances with Critical vulnerabilities from Qualys", "Instances with
               Exploitable Vulnerabilities from Qualys", "Instances with missing patches from Qualys" and "AMIs with highest number
               of Vulnerabilities from Qualys". These insights can be viewed in "Insights" section in AWS Security Hub.***


