### Check IAM Permission

Ensure the AWS CLI is configured correctly.

```bash
aws sts get-caller-identity
```

You should have the necessary IAM permissions to create a cluster. 

If you get a credential error, that means you need to configure the aws settings:

```bash
aws configure
```

and paste in your user's AWS credentials.

> **Note**: Just as mentioned in an earlier page, if the workspace does not allow you to paste contents, you may do so in a new window.  
>


### Create an EKS Cluster

Install <a href="https://eksctl.io/installation/" target="_blank">eksctl</a> and use it to create an EKS cluster. Here is a <a href="https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html" target="_blank">quick start guide</a> for creating EKS cluster using the eksctl cli tool. It's as simple as running a single command to create a cluster:

```bash
eksctl create cluster --name my-cluster --region us-east-1 --nodegroup-name my-nodes --node-type t3.small --nodes 1 --nodes-min 1 --nodes-max 2
```

### Update the Kubeconfig

After creating an EKS cluster, execute the command below to update the context in the local Kubeconfig file. This file allows configuring access to clusters, and should have at least one active context. It contains the information about clusters, users, namespaces, and authentication mechanisms.

```bash
aws eks --region us-east-1 update-kubeconfig --name my-cluster
```

Verify and copy the context name

```bash
kubectl config current-context
```

Output will be simiar to

```bash
arn:aws:eks:us-west-2:411764878390902:cluster/my-cluster
```

Alternatively, view the entire Kubeconfig file. 

```bash
kubectl config view
```

> **Note**: If your kubeconfig file is blank or unavailable, you may not be able to interact with any of your clusters. In general, when you install `kubectl` and create a local Kubernetes cluster, `kubectl` utility  automatically sets the <a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/" target="_blank">kubeconfig</a> file.   
>


### Delete the EKS Cluster

When you finish your project, use the following command to delete your EKS cluster

```bash
eksctl delete cluster --name my-cluster --region us-east-1
```