import os
import subprocess
from datetime import datetime

# 获取当前时间
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 指定日志文件的路径
log_file = "./git_push_log.txt"

# 初始化日志文件，如果不存在则创建
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("Git Push Log\n")

# 函数来记录操作到日志文件
def log_to_file(message):
    with open(log_file, "a") as f:
        f.write(f"{current_time}: {message}\n")

# 创建新文件
new_file_name = "new_file.txt"
with open(new_file_name, "w") as f:
    f.write("This is a new file.")

log_to_file(f"Created a new file: {new_file_name}")

# 添加新文件到Git
subprocess.run(["git", "add", new_file_name])
log_to_file(f"Added {new_file_name} to Git")

# 提交更改
commit_message = "Added a new file"
subprocess.run(["git", "commit", "-m", commit_message])
log_to_file(f"Committed changes with message: '{commit_message}'")

# 切换分支并创建分支（如果分支不存在）
branch_name = "new-branch"
subprocess.run(["git", "checkout", "-b", branch_name])
log_to_file(f"Switched to branch '{branch_name}'")

# 推送更改到远程仓库
subprocess.run(["git", "push"])
log_to_file("Pushed changes to remote repository")

print("操作已记录到日志文件中。")
