from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from utils.log import info, debug, error

class EnglishCorrectionModel:
    def __init__(self, model_name="Qwen/Qwen2.5-1.5B-Instruct"):
        info(f"Loading model: {model_name}")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"
        )
        
        info("Model loaded successfully")
        
    def correct_text(self, input_text, max_new_tokens=512):
        """
        영어 인터뷰 텍스트를 교정합니다.
        
        Args:
            input_text (str): 교정할 영어 텍스트
            max_new_tokens (int): 생성할 최대 토큰 수
            
        Returns:
            str: 교정된 텍스트
        """
        from model.prompts import get_correction_prompt
        prompt = get_correction_prompt(input_text)
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # 프롬프트 부분 제거
        response = response.replace(prompt, "").strip()
        return response