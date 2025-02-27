import logging
import os
import sys

# 로그 디렉토리 생성
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 로거 설정
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 이미 핸들러가 있는 경우 제거 (중복 로깅 방지)
if logger.handlers:
    logger.handlers = []

# 로그 포맷 설정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 콘솔 출력용 핸들러
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # 콘솔에는 INFO 레벨 이상만 출력
logger.addHandler(stream_handler)

# 파일 출력용 핸들러
file_handler = logging.FileHandler(os.path.join(log_dir, 'app.log'))
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # 파일에는 모든 로그 저장
logger.addHandler(file_handler)

# 간편한 사용을 위한 래퍼 함수
def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)

def info(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)

def warning(msg, *args, **kwargs):
    logger.warning(msg, *args, **kwargs)

def error(msg, *args, **kwargs):
    logger.error(msg, *args, **kwargs)

def critical(msg, *args, **kwargs):
    logger.critical(msg, *args, **kwargs)