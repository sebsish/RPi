from threading import Thread
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject


class videoStream(Thread):
    def __init__(vid):
        Thread.__init__(vid)

    def video(vid):
        #Video streaming, gstreamer              
        Gst.init(None)
        command = "v4l2src device=/dev/video0 ! video/x-h264,width=1280,height=720,framerate=30/1 ! rtph264pay ! udpsink host=192.168.1.187 port=5004"
        vid.pipeline = Gst.parse_launch(command)
        vid.pipeline.set_state(Gst.State.PLAYING)


    # stopper videostream
    def stop(vid):
        stopstream() 

# kommando som ma kjores pa pc er(NB! husk korrekt path til fil): 
# C:\gstreamer\1.0\x86_64\bin\gst-launch-1.0 udpsrc port=5004 ! ' application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96' ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink
