> **Change 1:** Add the following content right above the code.

**Note:** The code in the video (1:03) incorrectly referenced `COPY_ALL_TRIPS_SQL` (notice that it does not actually have `{year}` and `{month}` parameters). The correct one should be `COPY_MONTHLY_TRIPS_SQL`.

> **Change 2:** Update the code where it says COPY_ALL_TRIPS_SQL to COPY_MONTHLY_TRIPS_SQL.

> **Change 3:** If possible, also update these files in the workspace:
> - `/home/workspace/airflow/dags/cd0031-automate-data-pipelines/lesson-4-data-quality/solution/l4_e3_data_partitioning.py` line 27.
> - `/home/workspace/airflow/dags/cd0031-automate-data-pipelines/lesson-4-data-quality/starter/l4_e3_data_partitioning.py` line 42.
