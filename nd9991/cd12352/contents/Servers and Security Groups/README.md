ssh-add before ssh -A -i to server

The bastion host's DNS. Assuming it uses Ubuntu AMI, access it as such: First run `ssh-add ./MyKeyPair.pem` on your terminal, and then this command `ssh -A -i ./MyKeyPair.pem ubuntu@[ BastionHostDNS ]` to connect to the bastion host. From the bastion host, connect to the EC2 instance spun up by auto scaler with `ssh ubuntu@[ instance's private ip ]`