<details open>
<summary><b>Change 1:</b> Replace the title from "Step 5: Backend Tests" to "Step 5: Backend development Notes"
</details>

<details>
<summary><b>Change 2:</b> Replace the content to the following</summary>

> Just as before, the following notes were made by the development team as a documentation of their backend application.
>
> Your task is to take out only the relevant commands to be placed in your workflow YAML files.

## Running tests

While in the backend directory, perform the following steps:

```bash
# Install dependencies
pipenv install

# Run the tests
pipenv run test

# Expected output
================================================================== test session starts ==================================================================
platform linux -- Python 3.10.6, pytest-7.2.1, pluggy-1.0.0 -- /home/kirby/.local/share/virtualenvs/backend-AXGg_iGk/bin/python
cachedir: .pytest_cache
rootdir: /home/kirby/udacity/cd12354-build-ci-cd-pipelines-monitoring-and-logging/project/solution/backend
collected 3 items

test_app.py::test_movies_endpoint_returns_200 PASSED                                                                                              [ 33%]
test_app.py::test_movies_endpoint_returns_json PASSED                                                                                             [ 66%]
test_app.py::test_movies_endpoint_returns_valid_data PASSED                                                                                       [100%]
```

## Running linter

When there are no linting errors, there won't be any output.

```bash
pipenv run lint
# No output
```

## Build and run

For local development without docker, the developers use the following commands to build and run the backend application:

```bash
cd starter/backend

# Install dependencies
pipenv install

# Run application
pipenv run serve
```

For production deployments, the team uses the following commands to build and run the Docker image.

```bash
cd starter/backend

# Build the image
docker build --tag mp-backend:latest .

# Run the image
docker run -p 5000:5000 --name mp-backend -d mp-backend

# Check the running application
curl http://localhost:5000/movies

# Review logs
docker logs -f mp-backend

# Expected output
{"movies":[{"id":"123","title":"Top Gun: Maverick"},{"id":"456","title":"Sonic the Hedgehog"},{"id":"789","title":"A Quiet Place"}]}

# Stop the application
docker stop
```

## Deploy Kubernetes Manifests

In order to build the Kubernetes manifests correctly, the team uses `kustomize` in the following way:

```bash
cd starter/backend/k8s


/# Make sure you're kubeconfig is configured for the EKS cluster, i.e.
/# aws eks update-kubeconfig`

/# Set the image tag to the newer version
/# ℹ️ Don't commit any changes to the manifests that this command introduces

kustomize edit set image frontend=<ECR_REPO_URL>:<NEW_TAG_HERE>

/# Apply the manifests to the cluster
kustomize build | kubectl apply -f -
```

## IMPORTANT NOTE

To avoid depleting your AWS credits, tear down your AWS resources after implementing your project.

* Delete the resources manually if you created them directly from AWS console.
* If you created these resources via Terraform, run the following code from the `setup/terraform` directory:

  * **`terraform destroy`**
</details>