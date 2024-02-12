### Introduction to Automatic Builds with CodeBuild

In this demo, we're going to highlight how we can set up automatic builds using CodeBuild, as well as some conventions on how we can handle versioning in Docker images that are created from automatic builds when we need to push them somewhere.

### Configuring Webhooks for Automatic Builds

Note: in order to set webhooks for a repository, the repository has to be something that we own or have access to in our own GitHub accounts.

Changing the webhook can be done through the **Primary source webhook events** section.

In this demo, I set it to **pull requests merged**, which means the build with be initiated when a pull request is merged into the repository. Another common trigger is on push.


### Versioning Strategy

This is simply one mechanism for us to handle how we want our versioning strategy to be inside of our Docker repository. There are many options such as:

- using an epoch timestamp,
- manually handling and setting the variable, 
- or using something internal to the build process that increments for us like shown in the video above.

To do the latter, replace all `$IMAGE_TAG` instances in the `buildspec.yaml` document to `$CODEBUILD_BUILD_NUMBER`. CodeBuild will replace these placehoders with a number that increments as we initiate more builds.