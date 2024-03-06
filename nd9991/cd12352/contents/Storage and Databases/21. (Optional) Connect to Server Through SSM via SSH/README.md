> Unfortunately, due to some workspace restrictions, you cannot perform this from the Udacity workspace. The commands on this page should be run from your local computer, where you have access to the `~/.ssh` directory.


Note that the terminal from the earlier connection method is missing two useful bash features:

1. Auto-completion, and
2. Command history

To have these features in our terminal, you'll want to connect via SSH using SSM instead.

To set this up, you may follow the instructions on this page: [Step 8: (Optional) Enable and Control Permissions for SSH Connections Through Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-enable-ssh-connections.html).

Before that, though, you'll need to add a `KeyName` property to your CloudFormation template for the `WebAppLaunchTemplate` component and pass in a key pair name into it.

### Step 1: Assign a Key Pair to the Launch Template

This step should be quite straightforward, but if you need a refresher on what a key pair is, how to set it up, and where to update it in your CloudFormation template, please read the next page **Refresher on Key Pairs**.

### Step 2: Create/Update the SSH Configuration File

It is easier to do this by creating a shell script that you can run anytime. Create a script; you can call this script anything, but for this demonstration, we will use the name `ssm_via_ssh.sh`. Enter the following content into that script:

```bash
#!/bin/bash

cat <<EOF > "$HOME/.ssh/config"
# SSH over Session Manager
host i-* mi-*
    ProxyCommand sh -c "AWS_PROFILE=$1 aws ssm start-session --target %h --document-name AWS-StartSSHSession --parameters 'portNumber=%p'"
EOF

echo "SSH config file has been updated."
```

As you learned on an earlier page, this code inserts the text just under the `cat` command into the SSH configuration file `~/.ssh/config`.

Now, add permission to execute that file by running this command:

```bash
chmod +x ./ssm_via_ssh.sh
```

Then run the script:

```bash
./ssm_via_ssh.sh udacity
```

#### (Optional) Using the Default Profile in the Bash Script
The bash script above assumes that you use a custom profile with your AWS commands. If you want to use the default profile, you need to remove the part `AWS_PROFILE=$1` from the code. As a fun challenge, you may also adjust the code so it allows you to optionally pass the profile parameter.

### Step 3: Connect Through SSH

Now that you've got the config set up, you can SSH connect to your EC2 instance by running this command:

```bash
ssh -i ./MyKeyPair.pem ubuntu@[Instance ID]
```