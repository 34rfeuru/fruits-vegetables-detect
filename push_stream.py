import cv2
import subprocess


def get_pipe_process():
    video = cv2.VideoCapture(0)
    fps_copy = video.get(cv2.CAP_PROP_FPS)
    width_copy = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height_copy = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    command = [
        'ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', '{}x{}'.format(width_copy, height_copy),
        '-r', str(fps_copy),
        '-i', '-',
        '-an',
        '-vcodec', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'flv',
        'rtmp://159.75.66.34:1935/live'
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    return process


