To do this project, you may opt to first do everything locally before pushing your Docker container and Kubernetes cluster to AWS servers. This is a valid, and often even a recommended approach when preparing a Kubernetes deployment. Deploying locally—provided your local computer has sufficient specs—may save up a lot of setup costs and gives you a sandbox environment to experiment without worrying about the underlying costs.

> Doing things this way is optional, especially since some commands are not executable from the Udacity workspace, but you are more than welcome to try it locally.

## Introducing: minikube

[minikube](https://minikube.sigs.k8s.io/docs/) is a popular tool to set up a local Kubernetes cluster on macOS, Linux, and Windows.

Follow the installation instructions from [its documentation](https://minikube.sigs.k8s.io/docs/start/).

Once you have installed minikube, you may start a Kubernetes cluster with the following command:

```bash
minikube start
```

This command somewhat parallels the command you have learned earlier to connect `kubectl` with Amazon EKS:

```bash
aws eks --region <REGION> update-kubeconfig --name <CLUSTER_NAME>
```

After running the `minikube start` command, your `kubectl` should then be connected to your local Kubernetes cluster.

## What about Amazon ECR?

Instead of hosting your Docker images in Amazon ECR, you may build them locally and use them in your deployment YAML files.

### Important: Change the Docker environment so that minikube can "see" your Docker images

Fundamentally, minikube is a virtual machine (VM) with its own environment. It does not have access to your local machine's Docker daemon. Before building a Docker image to be run in your minikube environment, run the following command on your terminal to **connect your shell to minikube's Docker daemon**:

```bash
eval $(minikube docker-env)
```

Any other Docker command you execute after running that command will now interact with minikube's Docker daemon.

### Update the deployment YAML files

This is the part in a deployment YAML file so that it loads your local Docker image:

```yaml
spec:
  template:
    spec:
      containers:
      - name: coworking
        image: <DOCKER IMAGE NAME>:<IMAGE TAG>
```

When you make changes to your Docker image, you may rebuild it, delete your active Kubernetes pods, and then the new pods will get updated. This video gives you a quick demonstration of this.

[VIDEO]

Instructions on the next two pages can be done either locally or via Amazon EKS.