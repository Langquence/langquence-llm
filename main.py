from model.qwen_model import EnglishCorrectionModel

import platform
import torch
from utils.log import get_logger

logger = get_logger(__name__)

def log_system_info():
    """시스템 환경 정보를 로깅합니다."""
    logger.info("=" * 50)
    logger.info("Application starting")
    logger.info(f"Python version: {platform.python_version()}")
    logger.info(f"Platform: {platform.platform()}")
    logger.info(f"Torch version: {torch.__version__}")
    
    # CUDA 정보
    if torch.cuda.is_available():
        logger.info(f"CUDA available: Yes")
        logger.info(f"CUDA version: {torch.version.cuda}")
        logger.info(f"GPU device: {torch.cuda.get_device_name(0)}")
        logger.info(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
    else:
        logger.warning("CUDA available: No - Using CPU mode (slower)")
    
def main():
    # 모델 초기화
    model = EnglishCorrectionModel()
    
    print("영어 인터뷰 표현 교정 서비스")
    print("종료하려면 'exit' 또는 'quit'를 입력하세요\n")
    
    while True:
        user_input = input("교정할 영어 문장을 입력하세요: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("프로그램을 종료합니다.")
            break
            
        if not user_input.strip():
            continue
            
        corrected = model.correct_text(user_input)
        print(f"\n교정 결과: {corrected}\n")

if __name__ == "__main__":
    log_system_info()

    main()