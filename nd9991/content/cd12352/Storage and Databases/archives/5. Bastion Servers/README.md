To create a bastion server, here are some additions needed to your CloudFormation template:

1. An EC2 Instance as the bastion server
2. A SecurityGroup for the bastion server to allow port 22 access from external IP addresses.
3. Update the SecurityGroup of the existing web server (**not** the Load Balancer Security Group) to allow port 22 access from the bastion server's security group.

Additional notes:
- The bastion server must be placed in a public subnet.
- The bastion server's EC2 component must also have a `KeyName` property.

---

```yaml
  # EC 2 server as a bastion host
  BastionHost:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      KeyName: MyKeyPair
      ImageId: # Paste the latest UBUNTU AMI

      SecurityGroupIds:
        - !Ref BastionHostSecurityGroup

      # Use either any public subnet
      SubnetId:
        Fn::ImportValue: !Sub "${ProjectName}-public-subnet1"

      # this helps us identify which EC2 instance is the Bastion Host
      Tags:
        - Key: Name
          Value: "Bastion Host"

  # The Security Group of the Bastion Host
  BastionHostSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow public SSH access to the bastion host
      VpcId:
        Fn::ImportValue:
          !Sub "${ProjectName}-vpc-id"
      SecurityGroupIngress:
      # Allow SSH access to the bastion host
      # Ideally, set the ip address of your local computer. In this case, though,
      # let's just allow any ip address.
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        CidrIp: 0.0.0.0/0

  # The Security Group of the WebApp (named `SecurityGroup` in the template)
  # Add an additional port to its ingress rule so the bastion host may connect into it.
  WebAppSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      ...
      SecurityGroupIngress:
      ...
      # Add the following item to allow SSH access from the bastion host
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        SourceSecurityGroupId: !Ref BastionHostSecurityGroup
```