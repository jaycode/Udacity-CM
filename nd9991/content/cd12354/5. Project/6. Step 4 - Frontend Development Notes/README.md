<details open>
<summary><b>Change 1:</b> Replace the title from "Step 4: Frontend Tests" to "Step 4: Frontend development Notes"
</details>

<details>
<summary><b>Change 2:</b> Replace the content to the following</summary>

> The following notes were made by the development team as a documentation of their frontend application.
>
> Your task is to take out only the relevant commands to be placed in your workflow YAML files. For example,
> `nvm` is not needed when you use GitHub action [actions/setup-node](https://github.com/actions/setup-node).


## Running tests

While in the frontend directory, perform the following steps:

```bash
# Use correct NodeJS version
nvm use

# Install dependencies
npm ci

# Run the tests interactively. You'll need to press `a` to run the tests
npm test

# OR simulate running the tests in a CI environment
CI=true npm test


# Expected output
PASS src/components/__tests__/MovieList.test.js
PASS src/components/__tests__/App.test.js

Test Suites: 2 passed, 2 total
Tests:       3 passed, 3 total
Snapshots:   0 total
Time:        1.33 s
Ran all test suites.
```

> Note: `npm ci` should install the packages according to the dependencies described in `package-lock.json`, but if it doesn't work, you may try `npm install` as a workaround.

## Running linter

When there are no linting errors, the output won't return any errors

```bash
npm run lint

# Expected output
> frontend@1.0.0 lint
> eslint .
```

## Build and run

For local development without docker, the developers use the following commands:

```bash
cd starter/frontend

# Install dependencies
npm ci

# Run local development server with hot reloading and point to the backend default
REACT_APP_MOVIE_API_URL=http://localhost:5000 npm start
```

To build the frontend application for a production deployment, they use the following commands:

```bash
# Build the image
# NOTE: Make sure the image is built with the URL of the backend system.
# The URL below would be the default backend URL when running locally
docker build --build-arg=REACT_APP_MOVIE_API_URL=http://localhost:5000 --tag=mp-frontend:latest .

docker run --name mp-frontend -p 3000:3000 -d mp-frontend]

# Open the browser to localhost:3000 and you should see the list of movies,
# provided the backend is available on localhost:5000
```

# Important Note!

The rubric includes the following specification:

> There should be a step that builds the application using docker only after linting and testing complete (use the needs directive) This step should also utilize build-args to ensure the application is built with an environment variable REACT_APP_MOVIE_API_URL

This means that you need to create an environment variable **REACT_APP_MOVIE_API_URL** to store the value `http://localhost:5000` and then use it in the above `docker/build` command rather than hard-coding the URL.

## Deploy Kubernetes Manifests

In order to build the Kubernetes manifests correctly, the team uses `kustomize` in the following way:

```undefined
cd starter/frontend/k8s


/# Make sure you're kubeconfig is configured for the EKS cluster, i.e.
/# aws eks update-kubeconfig`

/# Set the image tag to the newer version
/# ℹ️ Don't commit any changes to the manifests that this command introduces

kustomize edit set image frontend=<ECR_REPO_URL>:<NEW_TAG_HERE>

/# Apply the manifests to the cluster
kustomize build | kubectl apply -f -
```
</details>