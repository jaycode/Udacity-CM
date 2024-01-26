<details open>

<summary><b>Change 1:</b> Right </b>above</b> the heading <span style="background:yellow">Creating a Synapse Analytics Workspace:</span>, add the following content:</summary>

**Allowlist IP ...** link may not show in your Query Editor and you get the following message instead:

![Cannot login to SQL DB](error-need-public.png)

To fix this, you need to enable public network access from the **Networking** option. First, go to the overview of your SQL database, and click on the **Set server firewall** link:

![Set server firewall link](login-ip-1.png)

Then, enable public network access to your database server and add your computer's IP address. Also, enable the **Allow Azure services and resources to access this server** option since we will need to do that later in this project:

![Enable public network and Azure services access to your database server](login-ip-2.png)

</details>