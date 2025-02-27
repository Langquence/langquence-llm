import sys
import os

# 프로젝트 루트 디렉토리를 파이썬 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.qwen_model import EnglishCorrectionModel

def main():
    # 모델 초기화
    model = EnglishCorrectionModel()
    
    # 테스트 문장 목록
    test_sentences = [
        "I have work in this company for 5 years.",
        "I am good at solve difficult problems.",
        "In my previous job, I was responsible to develop new features.",
        "I am interesting in machine learning and data science."
    ]
    
    print("영어 교정 테스트 시작\n")
    
    for sentence in test_sentences:
        print(f"원문: {sentence}")
        corrected = model.correct_text(sentence)
        print(f"교정: {corrected}")
        print("-" * 50)

if __name__ == "__main__":
    main()