import cv2

def get_realsense_devices():
    """Return a list of connected RealSense serial numbers."""
    try:
        import pyrealsense2 as rs
    except ImportError:
        return []
    ctx = rs.context()
    return [d.get_info(rs.camera_info.serial_number) for d in ctx.devices]

def get_usb_cameras(max_index=5):
    """Return indices of openable V4L2 / USB cameras."""
    found = []
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            found.append(i)
            cap.release()
    return found