The data path used in solution script is incorrect.

To correct this issue, go to the workspace, browse to this file:

```
/home/workspace/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/lesson-2-spark-essentials/exercises/concept4-quiz-data-wrangling-with-dataframes/solution/data_wrangling_with_dataframes.py
```

Then replace line 26 with this code:

```
logs_df = spark.read.json("/workspace/home/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/lesson-2-spark-essentials/exercises/data/sparkify_log_small.json")
```
