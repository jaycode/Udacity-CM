## Frontend Deliverables

> The following lists provide you with the deliverables for the frontend application of this project.
> For more details on how to do each item, please read **Step 3. Setup CD Environment** and **Step 4: Frontent Development Notes**.
> The frontend code is written in NodeJs.

### A Continuous Integration workflow file that:

1. Is **triggered** on `pull_requests` events against the `main` branch, 
   1. Only when code in the frontend application changes
1. Can be run on-demand (i.e. manually without needing to push code)
1. Runs the following tasks in parallel:
   * Runs a linting job that fails if the code doesn't adhere to eslint rules
   * Runs a test job that fails if the test suite doesn't pass
   * Read the development notes to find out how to run the test and linting jobs
1. Runs a build job only if the lint and test jobs succeed.
   * The build job can be done by building the provided Dockerfile in the `starter/frontend` directory. Read the development notes to get the relevant commands

### A Continuous Deployment workflow file that:

1. Is **triggered** on `push` events against the `main` branch, 
   1. Only when code in the frontend application changes
1. Can be run on-demand (i.e. manually without needing to push code)
1. Accomplishes the following tasks:
   1. Test
   1. Build
      1. Run **after** tests succeed
      1. Tag the built docker image with the git sha (use GitHub Context)
   1. If deploying to a Kubernetes cluster: 
      1. Push the image to ECR
      1. Apply the Kubernetes manfiests using the image tag from **build**
      1. The relevant commands to deploy to Kubernetes are available in the development notes

