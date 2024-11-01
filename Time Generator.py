from datetime import datetime
import pytz, os, time
a = 0
while a<=100:
    utc_time = datetime.now(pytz.utc)
    beijing_tz = pytz.timezone('Asia/Shanghai')
    beijing_time = utc_time.astimezone(beijing_tz)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# " + beijing_time.strftime('%Y-%m-%d %H:%M:%S'))
    os.system("git add .")
    os.system("git commit -S -m auto-run")
    os.system("git pull --rebase")
    os.system("git push")
    print("本次为第",a,"次")
    a = a + 1
    time.sleep(1)
print("已成功执行 100 次")