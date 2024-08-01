<details open>
<summary><b>Note</b></summary>

> This page replaces the existing "Configuration" page.
</details>

<details open>
<summary><b>New Page</b></summary>
The first thing that we recommend you to do in this project is to set up a Postgres database using a Helm Chart.

## 1. Set up Bitnami Repo

```bash
helm repo add <REPO_NAME> https://charts.bitnami.com/bitnami
```

## 2. Install PostgreSQL Helm Chart

```bash
helm install <SERVICE_NAME> <REPO_NAME>/postgresql
```

This should set up a Postgre deployment at <SERVICE_NAME>-postgresql.default.svc.cluster.local in your Kubernetes cluster. You can verify it by running `kubectl get svc`.

By default, it will create a username postgres. The password can be retrieved with the following command:

```bash
export POSTGRES_PASSWORD=$(kubectl get secret --namespace default <SERVICE_NAME>-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)
echo $POSTGRES_PASSWORD
```

The instructions are adapted from Bitnami's PostgreSQL Helm Chart (shown on the terminal right after installation).

## 3. Test Database Connection

The database is only accessible from within the cluster. This means that when you will have some issues connecting to it via your local environment. You can either connect to a pod that has access to the cluster or connect remotely via `Port Forwarding`

To get the password for "postgres" run:

```bash
export POSTGRES_PASSWORD=$(kubectl get secret --namespace default db-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)
```

After installation, Helm may store some secret values that are accessible via the command `kubectl get secret`. The above line extracts the postgres password from this secret values output and store it in a variable called `POSTGRES_PASSWORD`.

We may print out this variable by running the following command:

```bash
echo $POSTGRES_PASSWORD
```

## 4. Connecting Via Port Forwarding

```bash
kubectl port-forward --namespace default svc/<SERVICE_NAME>-postgresql 5433:5432 &
```
The command above opens up port forwarding from your local environment's port 5433 to the `<SERVICE_NAME>-postgresql` instance port 5432. The `&` at the end ensures the process runs in the background.

Now that the port is opened, you may use the database instance.

## 5. Run Seed Files

We will need to run the seed files in db/ in order to create the tables and populate them with data.

```bash
PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5433 < <FILE_NAME.sql>
```

Run the above command once for each SQL file in the `db` directory. Alternatively, you may keep the commands in an initialization bash script.

## 6. Checking the tables

Run the following command to open up the psql terminal:

```bash
PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5433
```

From it, you may run queries like `select * from users;` and `select * from tokens;` to ensure they are not empty.

## 7. Closing the forwarded ports

Ports opened up are going to remain in the background of your terminal session. To release all ports created by port forwarding, run the following command (this is just an FYI, you do not need to run it):

```bash
ps aux | grep 'kubectl port-forward' | grep -v grep | awk '{print $2}' | xargs -r kill
```
</details>
