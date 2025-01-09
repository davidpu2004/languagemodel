
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
import os

class MetaM2M:
    def __init__(self, model_id="facebook/m2m100_418M"):
        self.model = M2M100ForConditionalGeneration.from_pretrained(model_id)
        self.tokenizer = M2M100Tokenizer.from_pretrained(model_id)


    #src_lang: "zh"  ( chinese)
    #dest_lang: "en"
    def translate(self,src_lang,dest_lang,text):
        self.tokenizer.src_lang = src_lang
        encoded_text = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(**encoded_text, forced_bos_token_id=self.tokenizer.get_lang_id(dest_lang))
        decoded_text = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return decoded_text[0]


    def get_tanscript(self, path, file_name):
        try:
            decoded_text="";
            file = os.path.join(path, file_name)
            with open(file, 'r') as f:
               for line in f:
                   decoded_text +=self.translate("en", "zh", line)
            return decoded_text

        except FileNotFoundError:
            print(f"The file {file_name} does not exist.")


def main():


    m2m = MetaM2M()
    decoded_text= m2m.get_tanscript(".","speech_en.txt")
    print("*****Meta M2M100 Model***** \n\n")
    print("*****the translated transcript***** \n\n", decoded_text)


if __name__ == "__main__":
    main()
