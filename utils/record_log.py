from logging import warn
import autoFrame.base.settings as setting
from logzero import setup_logger, logger, logfile, logging, loglevel
from functools import wraps

#成功日志普通函数
def record_access_log(msg):
    loglevel(setting.LOG_ACCESS_LEVEL)
    logfile(setting.LOG_ACCESS_FILE, maxBytes=1e6, backupCount=3)
    logger.info(msg)

#成功日志装饰器
def decorator_access_log(func):
    @wraps(func)
    def wrapper():
        print('准备开始执行：{} 函数:'.format(func.__name__))
        loglevel(setting.LOG_ACCESS_LEVEL)
        logfile(setting.LOG_ACCESS_FILE, maxBytes=1e6, backupCount=3)
        logger.info(func())
    return wrapper

#错误日志普通函数
def record_error_log(msg):
    loglevel(setting.LOG_ERROR_LEVEL)
    logfile(setting.LOG_ERROR_FILE, maxBytes=1e6, backupCount=6)
    logger.error(msg)

# 错误日志装饰器
def decorator_error_log(func):
    @wraps(func)
    def wrapper():
        print('准备开始执行：{} 函数:'.format(func.__name__))
        loglevel(setting.LOG_ERROR_LEVEL)
        logfile(setting.LOG_ERROR_FILE, maxBytes=1e6, backupCount=3)
        logger.info(func())
    return wrapper

#定制日志，可导入直接使用如：access_log.info(msg)
access_log = setup_logger(name="Access", logfile=setting.LOG_ACCESS_FILE, maxBytes=10240000000, backupCount=3, formatter=logging.Formatter(setting.LOG_ACCESS_FORMATTER), level=setting.LOG_ACCESS_LEVEL)
error_log = setup_logger(name="Error", logfile=setting.LOG_ERROR_FILE, maxBytes=10240000000, backupCount=3, formatter=logging.Formatter(setting.LOG_ERROR_FORMATTER), level=setting.LOG_ERROR_LEVEL)
