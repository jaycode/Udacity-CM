The data paths used in solution scripts are incorrect.

To correct this issue, go to the workspace, browse to this file:

```
/home/workspace/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/lesson-2-spark-essentials/exercises/concept2-reading-and-writing-data-with-spark/solution/data_inputs_and_outputs.py
```

Then replace line 17 with this code:

```
path = "/workspace/home/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/lesson-2-spark-essentials/exercises/data/sparkify_log_small.json"
```

and line 32 with this:

```
out_path = "/workspace/home/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/lesson-2-spark-essentials/exercises/data/sparkify_log_small.csv"
```
