## What About a Web Server?

If you want the EC2 instances spun up by **AutoScalingGroup** to act as a web server, you will obviously need to set them up as one. You may do this by telling them to install and set up a web server when they first instantiated. Remember that in lesson **Servers and Security Groups** > **Launch Templates** we've talked about `LaunchTemplateData.UserData` property. You you may enter a setting up script into it.

## NGINX

### Static Assets

A website would be rather bland without any images, css, and possibly javascripts. In the **Storage and Databases** lesson, you have learned how to create an S3 bucket and granting your EC2 instances access to it.
