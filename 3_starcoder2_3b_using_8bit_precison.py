# pip install bitsandbytes accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

print("이 파일을 최초 실행 시 StarCoder2-3b 모델이 local에 설치됩니다. \n필요한 disk 용량은 약 12GB이므로 참고하십시오. ")
print("설치된 모델 경로: /home/username/.cache/huggingface/hub/models--bigcode--starcoder2-3b")

# to use 4bit use `load_in_4bit=True` instead
quantization_config = BitsAndBytesConfig(load_in_8bit=True)

checkpoint = "bigcode/starcoder2-3b"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained("bigcode/starcoder2-3b", quantization_config=quantization_config)

#inputs = tokenizer.encode("[생성할 함수명 입력]", return_tensors="pt").to("cuda")
inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to("cuda")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))

