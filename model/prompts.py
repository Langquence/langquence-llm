def get_correction_prompt(input_text):
    """교정을 위한 프롬프트를 생성합니다."""
    return f"""
As an AI English correction assistant for Korean speakers preparing for English interviews, 
your task is to make their English expressions more natural and professional.

Here are some examples:

Example 1:
Korean speaker: "I have three years experience in marketing field."
Corrected: "I have three years of experience in the marketing field."

Example 2:
Korean speaker: "I am confidence about my skill to solve this problem."
Corrected: "I am confident in my ability to solve this problem."

Example 3:
Korean speaker: "Let me introduce about myself."
Corrected: "Let me introduce myself."

Now, please correct the following expression to make it sound more natural:

Korean speaker: "{input_text}"
Corrected:
"""

def get_detailed_correction_prompt(input_text):
    """교정 이유를 함께 제공하는 프롬프트를 생성합니다."""
    return f"""
As an AI English correction assistant for Korean speakers preparing for English interviews, 
your task is to make their English expressions more natural and professional.

Here are some examples:

Example 1:
Korean speaker: "I have three years experience in marketing field."
Corrected: "I have three years of experience in the marketing field."
Explanation: Added "of" before "experience" and "the" before "marketing field" to make it grammatically correct.

Example 2:
Korean speaker: "I am confidence about my skill to solve this problem."
Corrected: "I am confident in my ability to solve this problem."
Explanation: Changed "confidence" (noun) to "confident" (adjective), replaced "about" with "in", and "skill to solve" with "ability to solve" for more natural expression.

Now, please correct the following expression to make it sound more natural and explain why:

Korean speaker: "{input_text}"
Corrected:
Explanation:
"""