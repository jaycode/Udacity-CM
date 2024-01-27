## What About a Web Server?

If you want the EC2 instances spun up by **AutoScalingGroup** to act as a web server, you will obviously need to set them up as one. You can do this by configuring them to install and set up a web server when they are first instantiated. Remember that in **Servers and Security Groups** > **Launch Templates** we talked about the `LaunchTemplateData.UserData` property. You may enter a setup script into it.

In the project, you will be given starter code to install and start your NGINX server:

```
#!/bin/bash
apt-get update -y
sudo apt-get install nginx -y
service nginx start
```

When set up properly, you should see the following page when accessing your LoadBalancer's public URL:

![A beautiful NGINX success page!](nginx-success.png)

### Wait, What is a "LoadBalancer's Public URL"?

Remember from the previous page that the LoadBalancer is the first component to receive a user's request. The request is sent to the LoadBalancer's Domain Name Server (DNS), which also serves as the public URL accessible via a browser.

### Updating Your Website's Index Page

One of the project's rubric requirements is to display a page that contains the following text:

```md
it works! Udagram, Udacity
```

Therefore, you'll need to update your index page from the original NGINX welcome page shown above.

To do this, the `LaunchTemplateData.UserData` property can be updated to include a script that does the following:

1. Create a new `index.html` file.
2. Save this file in the `/var/www/html/` directory. This directory has another file, `index.nginx-debian.html`, which is the default page you saw earlier. The `index.html` page you add will take precedence over this page. 
3. Reload nginx.

Here are some useful bash commands to help you achieve this:

#### To Store Text into a File

```bash
cat <<EOF > [filename]
[content]
EOF
```

Replace `[filename]` with a filename and `[content]` with the content to be saved into that file.

#### To Copy or Move a File

```bash
cp [old location] [new location]
mv [old location] [new location]
```

#### To Act as a Root User

The `/var/www/html/` directory is restricted, so you'll need root access to edit it.

You can add `sudo` to run these commands as a root user, e.g., `sudo cp index.html /var/www/html/index.html`.

```bash
![`sudo` is such a strong word](sudo.png)
```

#### To Reload nginx

At the end of your script, add the following code to reload nginx to ensure the changes are propagated.

```
sudo systemctl reload nginx
```

### Static Assets

A website would be rather bland without any images, CSS, and possibly JavaScript. In the **Storage and Databases** lesson, you learned how to create an S3 bucket and grant your EC2 instances access to it. Revisit the pages from that lesson and add relevant code to your CloudFormation template.

In a real-world web application, server-related code is stored in EC2 instances while assets are stored in S3 buckets.