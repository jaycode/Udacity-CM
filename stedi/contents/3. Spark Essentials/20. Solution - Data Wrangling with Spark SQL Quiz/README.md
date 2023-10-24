we
> Issue 1

The data path used in solution script is incorrect.

To correct this issue, go to the workspace, browse to this file:

```
/home/workspace/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/lesson-2-spark-essentials/exercises/concept4-quiz-data-wrangling-with-dataframes/solution/data_wrangling_with_dataframes.py
```

Then replace line 18 with this code:

```
path = "/workspace/home/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/lesson-2-spark-essentials/exercises/data/sparkify_log_small_2.json"
```

---

> Issue 2

Also, running the code gave me the following error:

```
ImportError: Pandas >= 1.0.5 must be installed; however, it was not found.
```

To fix this, the pandas module needs to be installed in the workspace: `python3 -m pip install pandas`.
