# AWS Lambda CI/CD with GitHub Actions

This project demonstrates a simple CI/CD pipeline to automatically deploy a Python AWS Lambda function using GitHub Actions.

## How It Works

The process is defined in the `.github/workflows/lambda-deploy.yml` file:

1.  **Trigger:** The workflow runs on every `push` to the `main` branch.
2.  **Setup:** A virtual machine is set up with a specific version of Python.
3.  **Install Dependencies:** Python packages listed in `lambda/requirements.txt` are installed directly into the `lambda` directory.
4.  **AWS Credentials:** The workflow securely logs into AWS using secrets stored in the repository settings.
5.  **Package & Deploy:** The contents of the `lambda` folder are zipped and deployed to update the AWS Lambda function's code.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── lambda-deploy.yml   # CI/CD workflow definition
├── lambda/
│   ├── lambda_function.py      # Lambda function code
│   └── requirements.txt        # Python dependencies
└── README.md                   # This file
```

## Setup Instructions

### 1. Create an IAM User in AWS
- Create a new user with **programmatic access**.
- Attach a policy like `AdministratorAccess` (for learning purposes) or a more restrictive one like `AWSLambda_FullAccess`.
- **Save the `Access key ID` and `Secret access key`**.

### 2. Create the Lambda Function in AWS
- In the AWS Lambda console, create a new function from scratch.
- **Function name:** `my-test-ciccd-lambda` (must match the name in the `.yml` file).
- **Runtime:** `Python 3.12`.
- Use the default option to create a new execution role.

### 3. Configure GitHub Secrets
- In your GitHub repository, go to `Settings` > `Secrets and variables` > `Actions`.
- Add two new repository secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

---

## ⚠️ Cleanup (Resource Destruction)

To avoid any AWS charges, you **must delete all created resources** after you are finished.

1.  **Delete the Lambda Function:** In the Lambda console, select the function and delete it.
2.  **Delete the IAM Role:** In the IAM console, find the role created for the Lambda function (e.g., `my-test-ciccd-lambda-role-...`) and delete it.
3.  **Delete CloudWatch Logs:** In the CloudWatch console, find the log group (`/aws/lambda/my-test-ciccd-lambda`) and delete it.
4.  **Delete the IAM User:** In the IAM console, delete the user you created for GitHub Actions. You may need to delete its access keys first.
