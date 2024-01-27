If you've been following the lessons up until now, you should already have an idea of what you can do with CloudFormation, although the big picture may still a bit vague. That's alright, though; In the course project, you are going to put what you've learned into practice. These few lessons are here to better prepare you in completing it.

## By the end of these lessons, you should...

- Understand how everything you've learned so far fit together in a web application development.
- Understand what are needed to create a single page static website.
- Be able to debug a published infrastructure. This is very important as it is a significant part of what you will do.

But first, let's try to understand the big picture.

## The Big Picture

Take a look at the solution code on lesson **Servers and Security Groups**, page **Solution: Load Balancing WebApp Servers**. We will use the infrastructure produced by that template as a base.

What happens when an HTTP request (on port 80) land on your server?

1. **Load Balancer Receives the Request:**
    - The Application Load Balancer (ALB) **Listener** is going to be the first component in your infrastructure that "listens" to that request.
2. **Routing Decision by ALB:**
    - The ALB evaluates the request against the listener rules defined by the **ListenerRule** component.
    - Since the setup has a rule for forwarding traffic coming to path `/``, the ALB forwards the request to the **TargetGroup**.
3. **Target Group Processing:**
    - The **TargetGroup** determines which instances in the Auto Scaling group (**AutoScalingGroup**) should handle the request.
    - The **TargetGroup** uses health checks defined in it to ensure that it forwards the request to a healthy instance.
4. **Request Reaches the EC2 Instance:**
    - The selected EC2 instance, part of the **AutoScalingGroup**, receives the request. This instance is configured with the **LaunchTemplate**.
    - IMPORTANT: Notice that the **LaunchTemplate** has an `ImageId` property. You need to set it up with an AMI of a new Ubuntu instance. Look for an appropriate AMI in your AWS' **EC2 console**, and then find a link to **AMI Catalog** from the left sidebar.

      ![AMI Catalog link in the EC2 page in AWS console](ami-catalog.png)
    - **AutoScalingGroup** will spin up additional instances when needed and drop unused extra instances but will keep a minimum of `MinSize` instances. It means the EC2 instances created in the infrastructure are *ephemeral*; They do not keep their states. This fact will be important for later when you need to debug your EC2 instances.
5. **Response Sent Back:**
    - The response from the EC2 instance (either static content or dynamically generated content) is sent back to the ALB.
    - The ALB then routes this response back to the client who initiated the request.

## How Does the Network Architecture Fit in All This?

Notice that we glossed over the network infrastructure in the explanation above. This is possible due to the *separation of concerns* afforded by how CloudFormation was designed. Bringing the network architecture into the picture, notice that:

1. **AutoScalingGroup** is going to spin EC2 instances in private subnets, as shown by its `VPCZoneIdentifier` property.
2. **LoadBalancer** resides in both public subnets. This is described in its `Subnets` property.

## How Do I Debug My EC2 Instances?

Reading the above, you may immediately think that it does not seem to be possible to debug the EC2 instances as they are behind private subnets. And you would be correct to think that.

To be able to access the EC2 instances behind private subnets, you'll need to create *another* EC2 instance that resides in a public subnet. You will then SSH access into it, and from it SSH access into the private subnets. You will learn more about

## What About a Web Server?

If you want the EC2 instances spun up by **AutoScalingGroup** to act as a web server, you will obviously need to set them up as one. You may do this by telling them to install and set up a web server when they first instantiated. Remember that in lesson **Servers and Security Groups** > **Launch Templates** we've talked about `LaunchTemplateData.UserData` property. You you may enter a setting up script into it.

## Static Assets

A website would be rather bland without any images, css, and possibly javascripts. In the **Storage and Databases** lesson, you have learned how to create an S3 bucket and granting your EC2 instances access to it.

