import subprocess
import time

program_ffmpeg = (
        'ffmpeg -rtsp_transport tcp -i "rtsp://admin:qwerty12345@192.168.1.64:554/Streaming/Channels/101" -r 25 -c copy -map 0 vid.mp4'
)  # the entire line looks like
# ffmpeg -rtsp_transport tcp -i "rtsp://login:password@ip:port/Streaming/Channels/101" -c copy -map 0 vid.mp4
# more on ffmpeg.org
process_ffmpeg = subprocess.Popen(
    "exec " + program_ffmpeg,
    shell=True,  # execute in shell
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE,  # to get access to all the flows
)
print("start")
time.sleep(10)
process_ffmpeg.kill()
