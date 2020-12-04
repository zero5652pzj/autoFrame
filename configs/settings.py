import os
import logging

LOG_ACCESS_FILE = os.path.join(os.getcwd(), 'logs', "access.log") # 成功日志目录
LOG_ACCESS_FORMATTER = '%(name)s - %(asctime)-15s - %(levelname)s: %(message)s'  # 成功日志输出格式
LOG_ACCESS_LEVEL = logging.INFO  # 成功日志级别设定
LOG_ERROR_FILE = os.path.join(os.getcwd(), 'logs', 'error.log')   # 错误日志目录
LOG_ERROR_FORMATTER = '%(name)s - %(filename)s - %(asctime)-15s - %(levelname)s - %(lineno)d: %(message)s'   # 错误日志输出格式
LOG_ERROR_LEVEL = logging.ERROR  # 错误日志级别设定

REPORTS_FILE = os.path.join(os.getcwd(), 'reports')  # 生成报告目录
