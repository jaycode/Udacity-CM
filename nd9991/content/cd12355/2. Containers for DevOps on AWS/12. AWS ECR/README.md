<details open>
<summary><b>Change 1:</b> Add a video</summary>
Video content:

- Open up AWS console to find the account ID and region name
- Create an alias for AWS ECR
- Authenticate AWS ECR
- Create a private repository
- 

</details>

<details open>
<summary><b>Change 2:</b> Add an important tip</summary>

> Add the following tip before others:

- You don't have to remember or try running any of the commands on this page. After you have created your private repository, AWS will provide you with all the commands on this page with all the placeholders replaced by your account's specific values. They are accessible from the **View push commands** menu on your private repository main page (the video on the next page will show you how).

</details>

<details open>
<summary><b>Change 3:</b> Add the following tip on profile setting at the end of the "Creating a Registry" section</summary>

If you use a separate `profile` on your CLI configuration (through `aws configure --profile [profile_name]` or similar means), you may use that profile when getting the login and password of your ECR. Run the following command instead (notice the `--profile` addition):

```bash
aws ecr get-login-password --region region --profile [profile_name] | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```
</details>