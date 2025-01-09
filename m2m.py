from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer


chinese_text ='''
福克斯新闻称，特朗普当地时间1月8日在其自创社交平台上发文指责纽森拒绝签署“水资源恢复宣言”，
并批评纽森在遏制山火方面应对不力。同日，特朗普在国会山出席会议后对记者表示，加州缺少水资源，这是州长的错，
也可以说是州政府的错。
'''

model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")


# translate Chinese to English
tokenizer.src_lang = "zh"
encoded_zh = tokenizer(chinese_text, return_tensors="pt")
generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id("en"))
english= tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print( "*****translated to following english*****\n\n")
print(english)