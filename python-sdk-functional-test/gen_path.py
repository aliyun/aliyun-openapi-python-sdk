# -*- coding: UTF-8 -*-

import sys
import os
import string
# 打开文件
path = ".."
dirs = os.listdir(path)


# 输出所有文件和文件夹
for file in dirs:
    if (file.startswith("aliyun-python-sdk-") and not file.endswith("core-v3")):
        sys.path.append(os.path.abspath("../" + file))

print(string.join(sys.path, ":"))
