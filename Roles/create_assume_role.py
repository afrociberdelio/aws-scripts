import boto3
import json

def get_policy(arn, iam_client):
    arn = arn
    iam_client=iam_client
    policy = iam_client.get_policy(
        PolicyArn=arn
    )
    policy_version = iam_client.get_policy_version(
        PolicyArn=arn,
        VersionId=policy['Policy']['DefaultVersionId']
    )
    return json.dumps(policy_version['PolicyVersion']['Document'])


def create_iam_role(acctount, role_name, policy_name, policy_document, assume_role_policy):
    try:
        # Create IAM
        session = boto3.Session(profile_name=acctount)
        iam_client = session.client('iam')

        # Create Role
        print(f"Criando a role '{role_name}'...")
        role_response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(assume_role_policy),
            Description="Aplicacao interna para busca de EC2 em todas as contas",
        )
        print(f"Role '{role_name}' criada com sucesso.")

        # Create Policy
        print(f"Criando a policy '{policy_name}'...")
        policy_response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document),
            Description="Description to Role",
        )
        policy_arn = policy_response['Policy']['Arn']

        print(f"Policy '{policy_name}' created successfully. ARN: {policy_arn}, conta {acctount}")

        # Attach policy to role
        print(f"Attached to policy '{policy_name}' à role '{role_name}'...")
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn,
        )
        print(f"Policy '{policy_name}' successfully attached to role '{role_name}'.")

        return role_response, policy_response

    except Exception as e:
        print(f"Error creating role or policy: {e} in account {acctount}")
        return None


if __name__ == "__main__":

    accounts = ['aws-my-company-1','aws-my-company-2','aws-my-company-3','aws-my-company-4']

    # Nome da Role e Policy
    role_name = "rolepolicy-name-example"
    policy_name = "policy-name-example"

    # Trust Policy (assume role)
    assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::XXXXXXXXXXXX:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
        }
    ]
}

    # Document of Policy
    policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:Describe*",
                "rds:Describe*"
            ],
            "Resource": "*"
        }
    ]
}

    # Call function
    for account in accounts:
        create_iam_role(account, role_name, policy_name, policy_document, assume_role_policy)