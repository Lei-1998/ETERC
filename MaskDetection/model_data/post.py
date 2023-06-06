import datetime
import os
import requests
import shutil
def post_json(device_dict):
    arch_list = [
    ("idc001skl", "Intel Xeon Gold 6258R CPU"),
    ("core", "Intel Core i7-1065G7 CPU"),
    ("xeon", "Intel Xeon 6338 v5 CPU"),
    ("gpu", " Intel Core i7-1185G7E HD530 GPU"),
    ("ncs2", "Intel VPU i5-6500TE NCS2 VPU"),
    ("atom", "Intel Atom x6425RE HD505 GPU"),
    ]
    hwName = {}
    for i in range(6):
        hwName[arch_list[i][0]] =[]
        hwName[arch_list[i][0]].append(arch_list[i][1])
    envX = os.environ
    username = envX.get('JUPYTERHUB_USER')
    for key in device_dict:
        if key == username:
            continue
        DeviceName = hwName.get(device_dict.get(key)[0])[0]
        with open('results/'+device_dict.get(key)[0]+'/stats_' + device_dict.get(key)[1]+'.txt','r') as f:
            lines=f.readlines()
        inf_time = lines[0].rstrip()
        inf_fps = float(lines[1].rstrip()) / float(inf_time)
        cur_time = (datetime.datetime.now()+ datetime.timedelta(hours=15)).strftime("%Y-%m-%d %H:%M:%S") 
        res = {
                "devUserId": "u151935",
                "courseId": device_dict.get(username)[1],
                "email": device_dict.get(username)[0],
                "deviceName": DeviceName,
                "inferenceTime": float(inf_time),
                "fps": int(inf_fps),
                "uploadTime": cur_time,
        }
        r = requests.post("https://ai.eterc.cn/eterc-ai-boot/third-party/devcloud/add",json=res)
        print(r.text)
        print(res)

def queryEmail(email):
    cur_time = (datetime.datetime.now()+ datetime.timedelta(hours=15)).strftime("%Y-%m-%d %H:%M:%S") 
    res = {
        "devUserId": "u151935",
        "courseId": "01",
        "deviceName": "jiaolei",
        "inferenceTime": 0,
        "uploadTime": cur_time,
        "email": email,
        "fps": 0
    }
    r = requests.post("https://ai.eterc.cn/eterc-ai-boot/third-party/devcloud/query",json=res)
    print(r.text)
    
def download_file(url, object_name, output_folder):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        filename = os.path.join(output_folder, object_name)
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
def nextUrl():
    print("https://notebooks.edge.devcloud.intel.com/hub/login?next=/lab&RefURL=/content/www/cn/zh/developer/tools/devcloud/edge/build/overview.html")