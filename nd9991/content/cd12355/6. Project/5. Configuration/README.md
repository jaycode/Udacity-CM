<details open>
<summary><b>Change 1:</b> Replace svc</summary>

> Replace `kubectl svc` with:

```
kubectl get svc
```

</details>

<details open>
<summary><b>Change 2:</b> Replace content starting and including <i>The instructions are adapted from Bitnami's PostgreSQL Helm Chart.</i></summary>

The instructions are adapted from Bitnami's PostgreSQL Helm Chart (shown on the terminal right after installation).

```bash
PostgreSQL can be accessed via port 5432 on the following DNS names from within your cluster:

    db-postgresql.default.svc.cluster.local - Read/Write connection
```

```

To get the password for "postgres" run:

    export POSTGRES_PASSWORD=$(kubectl get secret --namespace default db-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)

To connect to your database run the following command:

    kubectl run db-postgresql-client --rm --tty -i --restart='Never' --namespace default --image docker.io/bitnami/postgresql:16.2.0-debian-11-r1 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
      --command -- psql --host db-postgresql -U postgres -d postgres -p 5432

    > NOTE: If you access the container using bash, make sure that you execute "/opt/bitnami/scripts/postgresql/entrypoint.sh /bin/bash" in order to avoid the error "psql: local user with ID 1001} does not exist"

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/db-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432
```

* Test Database Connection The database is accessible within the cluster. This means that when you will have some issues connecting to it via your local environment. You can either connect to a pod that has access to the cluster or connect remotely via `Port Forwarding`

Connecting Via Port Forwarding

```bash
kubectl port-forward --namespace default svc/<SERVICE_NAME>-postgresql 5432:5432 &
```

```
PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432
```

Connecting Via a Pod

```undefined
kubectl exec -it <POD_NAME> bash
PGPASSWORD="<PASSWORD HERE>" psql postgres://postgres@<SERVICE_NAME>:5432/postgres -c <COMMAND_HERE>
```

* Run Seed Files We will need to run the seed files in db/ in order to create the tables and populate them with data.

```
kubectl port-forward --namespace default svc/<SERVICE_NAME>-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432 < <FILE_NAME.sql>
```

2. Running the Analytics Application Locally

In the analytics/ directory:

* Install dependencies

```undefined
pip install -r requirements.txt
```

* Run the application (see below regarding environment variables)

```undefined
<ENV_VARS> python app.py
```

There are multiple ways to set environment variables in a command. They can be set per session by running export KEY=VAL in the command line or they can be prepended into your command.

```undefined
DB_USERNAME
DB_PASSWORD
DB_HOST (defaults to 127.0.0.1)
DB_PORT (defaults to 5432)
DB_NAME (defaults to postgres)
```

If we set the environment variables by prepending them, it would look like the following:

```undefined
DB_USERNAME=username_here DB_PASSWORD=password_here python app.py
```

The benefit here is that it's explicitly set. However, note that the DB_PASSWORD value is now recorded in the session's history in plaintext. There are several ways to work around this including setting environment variables in a file and sourcing them in a terminal session.

3. Verifying The Application

Generate report for check-ins grouped by dates 

```undefined
curl <BASE_URL>/api/reports/daily_usage
```

Generate report for check-ins grouped by users 

```undefined
curl <BASE_URL>/api/reports/user_visits
```
</details>
