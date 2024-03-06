<details open>
<summary><b>Change 1:</b> Add the following content at the end of the page</summary>

## Troubleshooting

### 1. Permission denied error when creating a registry

When running the `aws ecr get-login-password` command, you may run into the following error:

```bash
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/auth": dial unix /var/run/docker.sock: connect: permission denied
```

The error message suggests that your user does not have permission to access the Docker daemon. This problem persists because Docker commands, by default, require root privileges or for the user to be part of the docker group to execute successfully.

To resolve this issue, run the following command to add your user to the docker group:

```bash
sudo usermod -aG docker $USER
```

Then, log out and log back in or use `newgrp docker` to apply the group changes to your current session:

```bash
newgrp docker
```

### 2. Endless retries when pushing to docker

When running the `docker push` command, there is an issue that is quite difficult to debug since it does not give you any error message.

Running the `push` command may give you messages that it keeps retrying without avail:

```bash
The push refers to repository [repo_url/repo_name]
43e0127dbd78: Retrying in 4 seconds
90e3aa0f1f3b: Retrying in 4 seconds
34e0d794ab25: Retrying in 4 seconds
7c03fd745dba: Retrying in 4 seconds
71091a9901fb: Retrying in
...
```

This issue happens when the Docker registry is not successfully set up with your AWS ECR repository.

#### Diagnosis

First, diagnose that this is indeed the issue. Run the following command on your terminal (you may remove the `profile` option if you are using the default profile):

```bash
aws describe-repositories --region [your_region] --profile [your_profile]
```

And then, compare the output with the list of repositories in your AWS ECR console. If they are different, then that is an indication that this is indeed the issue.

#### Solution

To resolve this issue, you need to create a new IAM user from the AWS IAM console, and then run `aws configure` with this new user access credentials. After that, create the Docker registry again, tag, and then push your image again (**don't forget to use the new repository ID**).
</details>
