import json
import pprint
import run_translate_test as translate
import re


class utils:
    def read_json(self, file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data

    def write_json(self, file_path, data):
        with open(file_path, 'w') as outfile:
            json.dump(data, outfile)

    def merge_sentence_json(self, data):
        # content = ""
        # for para in data:
        #     if para == data[1]:
        #         print(para)
        #         content = '.'.join(para).replace("..", ".")
        #         content = re.sub(r"\s+[.]", '.', content.strip())
        #         content = re.sub(r"\s+[,]", ',', content)
        #         content = re.sub(r"\s+[?]", '?', content)
        #         content = re.sub(r"\s+[!]", '!', content)
        #         content = re.sub(r"\s", " ", content)

        #         print(content)
        #         print("===========================")

        #         translated_data = translate.run(content)
        #         print("===========================")

        i = 0
        for para in data:
            if para == data[1]:
                for sentence in para:
                    if sentence == "":
                        continue
                    sentence = re.sub(r"\s+[.]", '.', sentence.strip())
                    sentence = re.sub(r"\s+[,]", ',', sentence)
                    sentence = re.sub(r"\s+[?]", '?', sentence)
                    sentence = re.sub(r"\s+[!]", '!', sentence)
                    sentence = re.sub(r"\s", " ", sentence)
                    translated_data = translate.run(sentence)
                    i += 1
                    print(str(i) + ":===========================")

    def read_txt(self, file_path):
        with open(file_path, encoding='utf-8') as text_file:
            data = json.load(text_file)
            return data

    def write_txt(self, file_path, data):
        with open(file_path, mode='w', encoding='utf-8') as text_file:
            json.dump(data, text_file)

    def merge_sentence_txt(self, data):
        content = '.'.join(data).replace("..", ".")
        content = re.sub(r"\s+[.]", '.', content.strip())
        content = re.sub(r"\s+[,]", ',', content)
        content = re.sub(r"\s+[?]", '?', content)
        content = re.sub(r"\s+[!]", '!', content)
        content = re.sub(r"\s", " ", content)
        translated_data = translate.run(content)
        return translated_data
    def TranslateText(self, TextFileInput):
        data = utils.read_txt(self, TextFileInput)
        print(data)
        translated_data = utils.merge_sentence_txt(self, data)        
        output_filepath = TextFileInput
        utils.write_txt(self, output_filepath, translated_data)
        return output_filepath
        

#def main():
 #   test = utils()

    # data = test.read_json('./Test.json')
    # pprint.pprint(data)
    # print("===========================")
    # test.merge_sentence_json(data)

  #  data = test.read_txt("./DocxText.txt")
   # print(data)
    #output_filepath = "DocxTextOut.txt"
    #test.write_txt(output_filepath, translated_data)

   # with open("./DocxTextOut.txt") as text_file:
    #    data_out = json.load(text_file)
     #   pprint.pprint(data_out)


#if __name__ == '__main__':
 #   main()
