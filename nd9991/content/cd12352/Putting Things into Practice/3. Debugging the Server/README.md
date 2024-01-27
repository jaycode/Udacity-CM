## How Does the Network Architecture Fit in All This?

Notice that we glossed over the network infrastructure in all our discussions so far. This is possible due to the *separation of concerns* afforded by how CloudFormation was designed. Bringing the network architecture into the picture, notice that:

1. **AutoScalingGroup** is going to spin EC2 instances in private subnets, as shown by its `VPCZoneIdentifier` property.
2. **LoadBalancer** resides in both public subnets. This is described in its `Subnets` property.

Reading the above, you may immediately think that it does not seem to be possible to debug the EC2 instances as they are behind private subnets. And you would be correct to think that.

## How Do I Debug My EC2 Instances?

Firstly, you need to know that you may use the very terminal in the workspace to gain access into an EC2 instance. This is called Secure Shell (SSH) access and you can do that by running the following command:

```
ssh -i [keypair file] [user]@[server IP or DNS]
```

SSH connection is done via port 22, as mentioned multiple times throughout the lessons.

### What is a Key Pair?

Just as its name suggest, a key pair is a key to unlock access to a server. [TODO]

## How to SSH Access a Private EC2 Instance?

To be able to access the EC2 instances behind private subnets, you'll need to create *another* EC2 instance that resides in a public subnet. You will then SSH access into it, and from it SSH access into the private subnets. We call this instance:

## Bastion Servers

This concept was brushed upon in **Servers and Security Groups** > **Exercise: Least Privilege Security Groups** where you were asked to create bastions or SSH jump boxes to connect to the application servers.

### Requirements to create a Bastion Server

To create a bastion server, you would need to create two things:

1. An EC2 Instance as the server itself, and
2. A SecurityGroup component to allow port 22 access from external IP addresses.

- The bastion server must be placed in a public subnet.
- Both the bastion server and your `LaunchTemplate` component must have a `KeyName` property.

[TODO]