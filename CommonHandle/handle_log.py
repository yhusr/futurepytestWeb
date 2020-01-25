"""
Time:2020/1/24 0024
"""
import logging
from CommonHandle.handle_os import mylog_path


class HandleLogger:

    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = mylog_path

    def get_mylogger(self):
        logger = logging.getLogger('my_web_test')
        myformat = '%(asctime)s - %(name)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        logger.setLevel('DEBUG')
        formater = logging.Formatter(myformat)

        # 控制台输出显示
        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        sh.setFormatter(formater)
        logger.addHandler(sh)

        # 文件输出显示
        fh = logging.FileHandler(self.filepath)
        fh.setFormatter(formater)
        fh.setLevel('DEBUG')
        logger.addHandler(fh)
        return logger


logger = HandleLogger().get_mylogger()