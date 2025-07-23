import os
import subprocess
from datetime import datetime, timedelta
import random

# Boshlanish va tugash sanalari
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 5, 1)

# Har kuni 5 commit
commits_per_day = 5

while start_date <= end_date:
    for i in range(commits_per_day):
        # Har bir commit uchun ozgina vaqt farqi
        commit_time = start_date.replace(
            hour=random.randint(8, 20),  # 08:00 dan 20:00 gacha
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )
        formatted_time = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

        # Faylga yozamiz
        with open("activity.txt", "a") as f:
            f.write(f"{formatted_time} - Commit #{i+1}\n")

        # Git add
        subprocess.run(["git", "add", "activity.txt"])

        # Git env bilan commit
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = formatted_time
        env["GIT_COMMITTER_DATE"] = formatted_time

        subprocess.run(["git", "commit", "-m", f"Auto commit on {formatted_time}"], env=env)

    start_date += timedelta(days=1)

# Oxirida push qilamiz
subprocess.run(["git", "push"])
