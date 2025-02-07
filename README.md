# [Roles/create_assume_role.py](#script)

## Description
This Python script automates the creation of AWS IAM roles and policies across multiple AWS accounts. It uses `boto3` to interact with AWS IAM services, creating roles with predefined policies and attaching them to the accounts specified in the script.

## Prerequisites
Before running the script, ensure you have:
- AWS CLI configured with profiles for each target AWS account.
- IAM permissions to create roles and policies.
- `boto3` installed in your Python environment.

## Installation
1. Install `boto3` if you haven't already:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your AWS credentials:
   ```bash
   aws configure --profile <profile_name>
   ```
git remote add origin https://github.com/afrociberdelio/aws-scripts.git
## Script Breakdown
### Functions:
- `get_policy(arn, iam_client)`: Retrieves and returns the JSON document of an existing IAM policy.
- `create_iam_role(acctount, role_name, policy_name, policy_document, assume_role_policy)`: Creates an IAM role, attaches a policy to it, and prints the status.

### Main Execution:
- Iterates through a list of AWS accounts.
- Calls `create_iam_role()` for each account, creating a role and attaching the policy.

## Configuration
Modify the following variables as needed:
- `accounts`: List of AWS account profiles.
- `role_name`: Name of the IAM role to be created.
- `policy_name`: Name of the IAM policy.
- `assume_role_policy`: Trust policy allowing the role to be assumed.
- `policy_document`: Permissions assigned to the policy.

## Running the Script
Execute the script using Python:
```bash
python script.py
```

## Example Output
```
Creating the role 'rolepolicy-name-example'...
Role 'rolepolicy-name-example' created successfully.
Creating the policy 'policy-name-example'...
Policy 'policy-name-example' created successfully. ARN: arn:aws:iam::123456789012:policy/policy-name-example
Attached policy 'policy-name-example' to role 'rolepolicy-name-example'.
```

## Error Handling
If an error occurs, it will be printed with the respective AWS account where the failure happened.

## License
This script is provided under the MIT License.

#####################################################################################