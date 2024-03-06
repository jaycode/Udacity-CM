If you've been following the lessons up until now, you should already have an idea of what you can do with CloudFormation, although the big picture may still be a bit vague. That's alright, though; in the course project, you are going to put what you've learned into practice. The next few pages are put together to better prepare you for completing it.

## By the end of these lessons, you should...

- Understand how everything you've learned so far fits together in web application development.
- Understand what is needed to create a single page static website.
- Be able to debug a published infrastructure. This is very important as it is a significant part of what you will do.

But first, let's try to understand the big picture.

## The Big Picture

Take a look at the solution code in the lesson **Servers and Security Groups**, page **Solution: Load Balancing WebApp Servers**. We will use the infrastructure produced by that template as a base.

What happens when an HTTP request (on port 80) lands on your server?

1. **Load Balancer Receives the Request:**
    - The Application Load Balancer (ALB) **Listener** is going to be the first component in your infrastructure that "listens" to that request.
2. **Routing Decision by ALB:**
    - The ALB evaluates the request against the listener rules defined by the **ListenerRule** component.
    - Since the setup has a rule for forwarding traffic coming to path `/`, the ALB forwards the request to the **TargetGroup**.
3. **Target Group Processing:**
    - The **TargetGroup** determines which instances in the Auto Scaling group (**AutoScalingGroup**) should handle the request.
    - The **TargetGroup** uses health checks defined in it to ensure that it forwards the request to a healthy instance.
4. **Request Reaches the EC2 Instance:**
    - The selected EC2 instance, part of the **AutoScalingGroup**, receives the request. This instance is configured with the **LaunchTemplate**.
    - IMPORTANT: Notice that the **LaunchTemplate** has an `ImageId` property. You need to set it up with an AMI of a new Ubuntu instance. Look for an appropriate AMI in your AWS **EC2 console**, and then find a link to the **AMI Catalog** from the left sidebar.
    - The **AutoScalingGroup** will spin up additional instances when needed and drop unused extra instances but will keep a minimum of `MinSize` instances. It means the EC2 instances created in the infrastructure are *ephemeral*; they do not keep their states. This fact will be important later when you need to debug your EC2 instances.
5. **Response Sent Back:**
    - The response from the EC2 instance (either static content or dynamically generated content) is sent back to the ALB.
    - The ALB then routes this response back to the client who initiated the request.