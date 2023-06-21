import uvicorn
import os
import glob
import subprocess
import sys
import time
import signal
from fastapi import FastAPI
from count import countPeople
from fastapi.responses import FileResponse

detect_path = "yolov5/yolov5-master/detect.py"
virtualenv_path = "venv\Scripts\python.exe"  # Windows 系统下的虚拟环境 Python 解释器路径
txt = '--weights runs/exp1/weights/best.pt --source inference/images/ --device 0 --save-txt'


# 启动 detect.py 进程
# subprocess.run([virtualenv_path, detect_path,])
# 终止 detect.py 进程


# 在运行一段时间后停止的时间间隔（以秒为单位）
time_interval = 5  # 例如：运行1小时后停止

# 获取当前时间
start_time = time.time()

# 运行循环
while True:
    # 执行运行的代码
    subprocess.run([virtualenv_path, detect_path,])

    # 检查是否超过时间间隔
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_interval:
        print("达到指定的运行时间，停止运行。")
        sys.exit()


app = FastAPI()

@app.post("/upload_latest")
async def upload_latest_video(video: bytes = File(...)):
    # 获取最新生成的exp文件夹路径
    exp_folder_path = get_latest_exp_folder_path()

    # 生成新的视频文件路径
    video_path = os.path.join(exp_folder_path, "uploaded_video.mp4")

    # 将视频保存到新的文件路径
    with open(video_path, "wb") as f:
        f.write(video)

    return {"message": "Video uploaded successfully"}

@app.get("/download_latest")
async def download_latest_video():
    # 获取最新生成的exp文件夹路径
    exp_folder_path = get_latest_exp_folder_path()

    # 生成视频文件路径
    video_path = os.path.join(exp_folder_path, "uploaded_video.mp4")

    # 返回保存在最新exp文件夹中的视频文件
    return FileResponse(video_path, media_type="video/mp4", filename="video.mp4")

def get_latest_exp_folder_path():
    runs_dir = "yolov5/yolov5-master/runs/detect"
    exp_folders = [folder for folder in os.listdir(runs_dir) if folder.startswith("exp")]
    latest_exp_folder = max(exp_folders, key=lambda f: int(f.lstrip("exp")))
    exp_folder_path = os.path.join(runs_dir, latest_exp_folder)
    return exp_folder_path




# @app.post("/api")
# async def api(data: dict):
#     # 调用Python程序处理数据
#     result = countPeople(data)
#
#     # 返回结果给API调用方
#     return result


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)



