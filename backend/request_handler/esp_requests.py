from database.user import *
from tools.global_variables import *
import time

def register_device_handler(IP, email, data):
  print("here")
  message = ''
  device_id = data['deviceID']
  if int(device_id) % 2 == 0 :
    set_device_left_ip(IP)
  else:
    set_device_right_ip(IP)
  message = update_devices_with_email(email, device_id)
  print(message)
  return message

def record_status_handler(data):
  if get_is_upload():
    device_id = data['deviceID']
    is_recording =bool(data['record'])
    if is_recording:
      start_time = time.time()
      set_is_upload(True)
      print(" Start Recording: ", device_id, start_time, True)
    else:
      set_is_upload(False)
      print(" Stop Recording: ", device_id, False)
    return "Start Uploading"
  else:
    return "Not started, is_upload is False"
  
def upload_data_handler(data):
  if get_is_upload() is False:
    return "Not authorized to upload"
  else:
    print(data)
    return "Not uploaded, is_upload is False"