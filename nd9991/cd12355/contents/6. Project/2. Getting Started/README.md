<details open>
<summary><b>Change #1:</b> Replace Python dependency</summary>

> Change Python 3.6+ to Python 3.12+

<summary><b>Change #2:</b> Add the following under the **Install AWS CLI v2** section</summary>

Afterward, run `aws configure` to set up your AWS settings. We recommend creating a new IAM user with admin role rather than using the federated user credentials directly. This approach avoids the need for reconfiguration after session timeouts.