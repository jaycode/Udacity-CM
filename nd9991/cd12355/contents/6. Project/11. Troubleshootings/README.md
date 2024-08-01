You may eventually run into some issues when working on this project, and that is a normal, even beneficial, learning process.

### Initial Diagnostic Tools

One popular issue is a non-working pod, which you can check by running the following command:

```bash
kubectl get pods
```

it will then gave you an output like the following, for example:

```bash
NAME                          READY   STATUS    RESTARTS   AGE
coworking-555f8b9498-6p9qt    0/1     Running   0          29m
postgresql-688c5c767c-v94jr   1/1     Running   0          136m
```

Notice that the READY value for the `coworking-555f8b9498-6p9qt` pod is `0/1`, indicating an issue during its deployment.

To further diagnose this issue, you may describe this pod as such:

```bash
kubectl describe pod coworking-555f8b9498-6p9qt
```

at the bottom of its output, you should see a list of events that you can use to verify at which stage the issue happened. For example:

```
Events:
  Type     Reason     Age                    From               Message
  ----     ------     ----                   ----               -------
  Normal   Scheduled  32m                    default-scheduler  Successfully assigned default/coworking-555f8b9498-6p9qt to ip-192-168-54-210.ec2.internal
  Normal   Pulling    32m                    kubelet            Pulling image "324459517973.dkr.ecr.us-east-1.amazonaws.com/coworking:1"
  Normal   Pulled     32m                    kubelet            Successfully pulled image "324459517973.dkr.ecr.us-east-1.amazonaws.com/coworking:1" in 8.97823742s
  Normal   Created    32m                    kubelet            Created container coworking
  Normal   Started    32m                    kubelet            Started container coworking
  Warning  Unhealthy  2m23s (x202 over 32m)  kubelet            Readiness probe failed: Get "http://192.168.43.56:5153/readiness_check": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
```

It shows that the kubelet was able to pull and start the Docker image, but the issue happens when the application port was probed. This indicates an issue when running the application itself.

You may then run the following code to view the application log:

```bash
kubectl logs coworking-555f8b9498-6p9qt
```

### Checking/Updating Active Environment Variables

If, for example, the error messages show that the application was not able to connect to the database, you may want to check if the environment variables are correctly set.

To check the active environment variables in a deployment, you may run the following command:

```bash
kubectl describe deployment <deployment_name>
```

Get the `<deployment_name>` from the output of `kubectl get deployments`.

You may then make some changes to your YAML deployment configuration files, and then delete the active pod:

```bash
kubectl delete pod coworking-555f8b9498-6p9qt
```

and then check if the environment variables have indeed changed.