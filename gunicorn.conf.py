import multiprocessing

workers = 2  # 核心数
errorlog = '/root/cyq/log/gunicorn.error.log'  # 发生错误时log的路径
accesslog = '/root/cyq/log/gunicorn.access.log'  # 正常时的log路径
timeout = 40
