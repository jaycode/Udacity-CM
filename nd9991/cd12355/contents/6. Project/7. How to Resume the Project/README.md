There might be times when you have to shut down your workspace and pick up your work later. When that happens, you'll need to do all of the following steps to get your working environment ready again.

## Set Up SSH Key

[Generate and add an SSH key to connect the workspace to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux). You may remove the previous SSH key from your GitHub account since you won't be using it anymore.

## Set Up kubectl Port-forwarding

Run the following commands.

```bash
# Set the AWS credentials
aws configure

# Update the context in your local Kubeconfig file. Replace my-cluster
# with your kubernetes cluster name in Amazon EKS.
aws eks --region us-east-1 update-kubeconfig --name my-cluster
```

And then, verify that you get the appropriate context name:

```bash
kubectl config current-context
```

If you need to set port-forwarding to access the database locally, you will also need to set it up again:

```bash
# Find the service name of postgresql by listing your services
kubectl get svc

# Set up port-forwarding for the postgresql service
kubectl port-forward svc/postgresql-service 5433:5432 &
```

If you ever need to use `psql` to access your database, you'll need to reinstall it too. The same goes for the Python modules and the Docker image when you need to run the analytics app locally.