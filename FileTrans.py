# coding=utf-8

import os
import sys
import json
import urllib
import random
import hashlib
import http.client

global_width = os.get_terminal_size().columns
global_ext_type = {'.wav', '.mp3', '.wma', '.mov', '.aac', '.flac', '.ogg', '.aac', '.aiff'}

# 输出分隔符
def output_separator():
    print("=" * global_width, end='')

# 检查字符串
def check_string(str):
    return not str.strip()

# 重命名文件
def rename_file(filePath, srcName, dstName):
    src = os.path.join(filePath, srcName)
    dst = os.path.join(filePath, dstName)
    os.rename(src, dst)

# 关闭Http连接
def close_http(httpClient):
    if httpClient:
        httpClient.close()

def trans(user_path, appid, secretKey):
    httpClient = None
    q = ""
    api_url = "/api/trans/vip/translate"
    fromLang = 'auto'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    count = 0

    path = user_path
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')

    # 遍历目录下所有文件
    for root, dirs, files in os.walk(path):
        for file in files:
            # 判断文件后缀
            file_name = os.path.splitext(file)[0]
            file_ext = os.path.splitext(file)[1]
            if file_ext.lower() in global_ext_type:
                # 签名
                q = file_name
                sign = appid + q + str(salt) + secretKey
                sign = hashlib.md5(sign.encode()).hexdigest()
                myurl = f"{api_url}?appid={appid}&q={urllib.parse.quote(q)}&from={fromLang}&to={toLang}&salt={str(salt)}&sign={sign}"

                # 调用百度API
                httpClient.request('GET', myurl)
                response = httpClient.getresponse()
                result_all = response.read().decode("utf-8")
                result = json.loads(result_all)

                if 'error_code' in result and result['error_code'] != '52000':
                    print("API调用失败, error_code : " + result['error_code'] + ", error_msg : " + result['error_msg'])
                    print("可前往官方API文档(http://api.fanyi.baidu.com/product/113)查看错误详情")
                    close_http(httpClient)
                    input("Press Enter to exit…")
                    sys.exit()
                
                transResult = result['trans_result'][0]['dst']
                transLog = file + ' >>> ' + transResult + file_ext
                # 打印翻译结果
                print(transLog)

                rename_file(root, file, transResult + file_ext)
                count += 1

    close_http(httpClient)
    print("Github: https://github.com/Beadd/MusicDownloader")
    print("翻译完成! 已翻译%s个文件, 感谢使用!" % str(count))
    print("继续使用或输入 q 以退出")

def main():
    print('''
  ______ _ _    _______                    
 |  ____(_) |  |__   __|                   
 | |___  _| | ___ | | _ __ __ _ _ __  ___  
 |  ___|| | |/ _ \| || '__/ _` | '_ \/ __| 
 | |    | | |  __/| || | | (_| | | | \__ \ 
 |_|    |_|_|\___||_||_|  \__,_|_| |_|___/ 
    ''')
    output_separator()

    config = json.load(open('./config.json', 'r'))
    appid = config['appid']
    secretKey = config['secretKey']

    if check_string(appid) or check_string(secretKey):
        print("请在config中正确配置百度API的appid和secretKey")
        input("Press Enter to exit…")
        sys.exit()

    while True:
        path = input("输入需要翻译的路径：")
        if path == 'q' or path == 'quit' or path == 'exit': 
            sys.exit()
        if os.path.exists(path):
            trans(path, appid, secretKey)

        output_separator()


if __name__ == "__main__":
    main()