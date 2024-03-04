## Backend Deliverables

> The following lists provide you with the deliverables for the frontend application of this project.
> For more details on how to do each item, please read **Step 3. Setup CD Environment** and **Step 5: Backend Development Notes**.
> The backend code is written in Python.

### A Continuous Integration workflow that:

1. Runs on `pull_requests` against the `main` branch, only when code in the frontend application changes.
1. Is able to be run on-demand (i.e., manually without needing to push code)
1. Runs the following jobs in parallel:
   * Runs a linting job that fails if the code doesn't adhere to eslint rules
   * Runs a test job that fails if the test suite doesn't pass
   * Read the development notes to find out how to run the test and linting jobs
1. Runs a build job only if the lint and test jobs pass and successfully builds the application
   * The build job can be done by building the provided Dockerfile in the `starter/backend` directory. Read the development notes to get the relevant commands

### A Continuous Deployment workflow that:

1. Runs on `push` against the `main` branch, only when code in the frontend application changes.
1. Is able to be run on-demand (i.e. manually without needing to push code)
1. Runs the same lint/test jobs as the Continuous Integration workflow
1. Runs a build job only when the lint and test jobs pass
   * The built docker image should be tagged with the git sha
1. Runs a deploy job that applies the Kubernetes manifests to the provided cluster.
   * The manifest should deploy the newly created tagged image

**⚠️ NOTE**
Once you begin work on Continuous Deployment, you'll need to first setup the AWS and Kubernetes environment. Follow the next set of instructions when you're ready to start testing your deployments.

