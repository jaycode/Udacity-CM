### Project Instructions

1. Set up a Postgres database.
1. Create a Dockerfile for the Python application.
   1. You'll submit the Dockerfile.
1. Write a simple build pipeline with AWS CodeBuild to build and push a Docker image into AWS ECR.
   1. Take a screenshot of AWS CodeBuild pipeline for your project submission.
   1. Take a screenshot of AWS ECR repository for the application's repository.
1. Create a service and deployment using Kubernetes configuration files to deploy the application.
1. You'll submit all the Kubernetes config files used for deployment (ie YAML files).
   1. Take a screenshot of running the kubectl get svc command.
   1. Take a screenshot of kubectl get pods.
   1. Take a screenshot of  kubectl describe svc <DATABASE_SERVICE_NAME>.
   1. Take a screenshot of kubectl describe deployment <SERVICE_NAME>.
1. Check AWS CloudWatch for application logs.
   1. Take a screenshot of AWS CloudWatch Container Insights logs for the application.
1. Create a README.md file in your solution that serves as documentation for your user to detail how your deployment process works and how the user can deploy changes. The details should not simply rehash what you have done on a step by step basis. Instead, it should help an experienced software developer understand the technologies and tools in the build and deploy process as well as provide them insight into how they would release new builds.

### Best Practices

> Dockerfile uses an appropriate base image for the application being deployed. Complex commands in the Dockerfile include a comment describing what it is doing.  

> The Docker images use semantic versioning with three numbers separated by dots, e.g. 1.2.1 and versioning is visible in the screenshot. See Semantic Versioning for more details.  

### Stand-Out Suggestions

Please provide up to 3 sentences for each suggested addition to your project in your README. Additional content in your submission from the standout suggestions do not impact the length or acceptance of your total submission.

* Specify reasonable Memory and CPU allocation in the Kubernetes deployment configuration
* In your README, specify what AWS instance type would be best used for the application? Why?
* In your README, provide your thoughts on how we can save on costs?