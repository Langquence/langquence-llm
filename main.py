from model.qwen_model import EnglishCorrectionModel

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
    main()