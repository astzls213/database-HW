#!/bin/sh
 
# 进入虚拟 Python 环境
source venv/bin/activate

# 运行 Flask 服务器 放到后台
python3 manage.py &
sleep 3     #  给服务器一点时间^ ^

# 运行 Electron
npm start

# 停止 Flask
kill %1