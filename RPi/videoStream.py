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
        command = "v4l2src device=/dev/video0 ! video/x-h264,width=1280,height=720,framerate=30/1 ! rtph264pay ! udpsink host=10.13.37.190 port=5004"
        vid.pipeline = Gst.parse_launch(command)
        

    # stopper videostream
    def stop(vid):
        stopstream() 


