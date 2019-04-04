from __future__ import print_function
import MeCab
import en_core_web_sm
from collections import Counter
from spacy import displacy
import spacy
from nltk.tokenize import word_tokenize
import ast
import json
from matplotlib import rcParams
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os
import numpy as np
import re
from tensorflow_serving.apis import prediction_service_pb2
from tensorflow_serving.apis import predict_pb2

from tensorflow_serving.apis import prediction_service_pb2_grpc
import grpc

from grpc.beta import implementations
import tensorflow as tf
import argparse
"""Example of a translation client."""


import matplotlib
matplotlib.use('Agg')


try:
    nlp = en_core_web_sm.load()
except Exception as e:
    print(e)

m = MeCab.Tagger("-Owakati")

image_folder = "/workspace/thuannm/opennmt/translation_webbased/static/images/"
japanese_font = "/workspace/thuannm/opennmt/translation_webbased/static/fonts/IPAfont00303/ipag.ttf"
#prop = fm.FontProperties(fname=japanese_font)
#matplotlib.rcParams['font.family'] = properties.get_name()
#rcParams['font.family'] = prop.get_name()


def preprocess_raw_text(translated_text):
    # DO: correct all unnecessary space in the raw_text
    for i, sentence in enumerate(translated_text):
        sentence = re.sub("\s+[.]", '.', sentence.strip())
        sentence = re.sub("\s+[,]", ',', sentence)
        sentence = re.sub("\s+[?]", '?', sentence)
        sentence = re.sub("\s+[!]", '!', sentence)
        translated_text[i] = sentence

    return translated_text


# DO: translated_text is an array of sentences.
def format_sentences_into_subtitle(data, translated_text):
    file_content = ""  # file output
    # DO: subtitle separated by lines in type of array
    lines = data[key_sub].split('\n')
    # DO: processed translated_text
    sentences = preprocess_raw_text(translated_text)
    # print(sentences)
    # DO: split_count from client side sent to server
    split_counts = data[key_split_count]
    # DO: no need space at the end of each item in split_sentences.
    split_sentences = []

    # s = 0
    # for i in range(0, len(split_counts)):
    #     s += split_counts[i] if split_counts[i] != -1 else 0
    # print(s)

    # Note: len(split_counts) = len(sentences) = len(split_sentences)
    # print(len(split_counts))
    # print(len(sentences))
    # print(sentences)
    # print(data[key_sentences])
    # original_sub_sentence = re.split(ending_sign, data[key_sentences])
    # print(original_sub_sentence)
    # for i in range(0, len(sentences)):
    #     print(sentences[i] + "\n" + original_sub_sentence[i] + "\n\n")

    word_delimiter = re.compile(' ')
    for i in range(0, len(sentences)):
        sentence = sentences[i]
        # DO: an improved way is instead of using num_word, use len(tokenizer(sentence))
        # DO: pos_words is the position right after a word, or it is the position of the first word
        pos_words = [0]
        temp_words = [word.start()
                      for word in word_delimiter.finditer(sentence)]
        if len(temp_words) > 0:
            pos_words = np.append(pos_words, temp_words)
        # DO: the end position of the final word.
        pos_words = np.append(pos_words, len(sentence))
        # print(sentence)
        # print(pos_words)
        num_word = len(pos_words) - 1
        # print(num_word == (len(re.findall(' ', sentence)) + 1))
        # the case when a sentence just have two words.
        # if (i >= len(split_counts)):
        #     print(i)
        split_count_abs = abs(split_counts[i])
        current_num_split = 0
        if (num_word == 2 and split_count_abs > 1):
            split_sentences = np.append(
                split_sentences, re.split(sentence, ' '))
        else:
            skip_word = num_word / split_count_abs
            x = float(int(skip_word))
            y = int(skip_word)
            # DO: y - 1 to avoid number of split is not guaranteed.
            skip_word = y if skip_word < x + 0.55 else y + 1
            start_word = 0
            end_word = skip_word
            while True:
                if (current_num_split + 1 == split_count_abs):
                    end_word = num_word
                    current_num_split += 1
                    temp_sentence = sentence[pos_words[start_word]:pos_words[end_word]].strip()
                    split_sentences = np.append(
                        split_sentences, [temp_sentence])
                    break
                else:
                    current_num_split += 1
                    # print("-----------")
                    # print(current_num_split)
                    # print(split_count_abs)
                    # print(start_word)
                    # print(end_word)
                    # print(len(pos_words))

                    # DO: When we don't have enough words to reach to current_num_split
                    # with the condition below, only end_word can be larger than num_word, but end_word > start_word
                    if (end_word > num_word):
                        end_word -= skip_word  # come back to the previous position
                        # update skip_wor to guaratee num_split_sentence = split_count_abs
                        skip_word = int(
                            skip_word / (split_count_abs - current_num_split + 1))
                        end_word += skip_word  # new end_word is smaller than previous one with a suitable ratio
                        # print(end_word)
                    temp_sentence = sentence[pos_words[start_word]:pos_words[end_word]].strip()
                    split_sentences = np.append(
                        split_sentences, [temp_sentence])
                start_word += skip_word
                end_word += skip_word

    # print(len(split_sentences))
    # print(split_sentences)

    k = 0
    for i in range(0, len(lines)):
        if (re.search("^\d{2}:\d{2}:\d{2}[.]\d{3} --> \d{2}:\d{2}:\d{2}[.]\d{3}$", lines[i])):
            j = i + 1
            while True:
                connected_sentence = split_sentences[k]
                # DO: concat sentences into only one corresponds to a line.
                # DO: len(split_sentences) equals to len(split_counts)
                while ((k + 1 < len(split_counts)) and split_counts[k + 1] == -1):
                    k = k + 1
                    # DO: need a space to concat two sentences into single one.
                    connected_sentence += " " + split_sentences[k]
                # print(lines[j] + "*")
                # print(connected_sentence)
                lines[j] = connected_sentence
                j += 1
                k += 1
                if (j >= len(lines) or lines[j] == ""):
                    break
            i = j

    for i in range(0, len(lines) - 1):
        file_content += lines[i] + '\n' if len(lines[i]) > 0 else "\n"

    file_content += lines[len(lines) - 1]
    return file_content


def tokenizer(sentences, lang):
    arr = []
    for sentence in sentences:
        if lang == "en":
            sent_tok = word_tokenize(sentence)
        elif lang == "vi":
            sent_tok = word_tokenize(sentence)
        else:
            sent_tok = sentence.split()
        arr.append(sent_tok)

    return arr


def replace_english_ner(sentences):
    replaced_ner = {}
    replaced_ner_inv = {}
    replaced_sentences = []
    for sentence in sentences:
        doc = nlp(str(sentence))
        replaced_sent = []
        for token in doc:
            text, tag = str(token), str(token.ent_type_)
            replaced_name = text
            if tag in ["PERSON", "NORP", "FAC", "ORG", "GPE", "LANGUAGE", "LAW"]:
                if text not in replaced_ner:
                    replaced_name = "<UNK"+str(len(replaced_ner)+1)+'>'
                    replaced_ner[text] = replaced_name
                    replaced_ner_inv[replaced_name] = text
                else:
                    replaced_name = replaced_ner[text]
            replaced_sent.append(replaced_name)
        replaced_sentences.append(replaced_sent)
    return replaced_sentences, replaced_ner_inv


def test_ner():
    sentences = ["European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices"]
    replaced_sentences, replaced_ner_inv = replace_english_ner(sentences)
    print(replaced_sentences)
# test_ner()


def restore_ner(sentence_tok, replaced_ner_inv):
    #new_setences_tok = []
    # for sent_tok in sentences_tok:
    new_sent_tok = []
    for token in sentence_tok:
        if token in replaced_ner_inv:
            token = replaced_ner_inv[token]
        new_sent_tok.append(token)
    return new_sent_tok


def isSubtitleFileExist(file_name):
    all_files = os.listdir(
        "/workspace/thuannm/extension_translate/static/subtitles")
    if file_name in all_files:
        return URL_SUBTITLE+file_name
    else:
        return ""


def isPageFileExist(file_name):
    all_files = os.listdir(
        "/workspace/thuannm/extension_translate/static/pages")
    if file_name in all_files:
        return URL_PAGES+file_name
    else:
        return ""


ignore_tag = ["script", "noscript", "iframe",
              "svg", "header", "img", "polygon"]
class_to_translate = ["lesson-name", "caption-text"]


def translate_course(src_sentences):
    tgt_sentences = main_translate(src_sentences, "page")
    # translated_data = {}
    # for idx, src in enumerate(rawHtml):
    #   translated_data[src] = tgt_sentences[idx]
    #   print(src +" ||| "+ tgt_sentences[idx])
    # return translated_data
    return tgt_sentences


def get_translated_text(src_data):
    src_sentences = src_data["sentences"]
    # sentences = split_sentence(src_sentences)
    # print(src_sentences)
    tgt_sentences = main_translate(src_sentences, "subtitle")
    # print(tgt_sentences)
    # return " ".join(tgt_sentences)
    return tgt_sentences


def split_sentence(paragraph):
    start = -1
    sentences = []
    for i, c in enumerate(paragraph):
        if start == -1:
            start = i
        if c in ".!?":
            end = i+1
            sentences.append(paragraph[start:end])
            start = -1
    return sentences


def parse_translation_result(result):
    """Parses a translation result.

    Args:
      result: A `PredictResponse` proto.

    Returns:
      A list of tokens.
    """
    #from pudb import set_trace; set_trace()
    lengths = tf.make_ndarray(result.outputs["length"])[0]
    hypotheses = tf.make_ndarray(result.outputs["tokens"])[0]
    attention_summary = tf.make_ndarray(result.outputs["alignment"])[0]
    # print(attention_summary)

    # Only consider the first hypothesis (the best one).
    best_hypothesis = hypotheses[0]
    best_length = lengths[0]

    return best_hypothesis[0:best_length - 1], attention_summary  # Ignore </s>


def translate(stub, model_name, tokens, timeout=5.0):
    """Translates a sequence of tokens.

    Args:
      stub: The prediction service stub.
      model_name: The model to request.
      tokens: A list of tokens.
      timeout: Timeout after this many seconds.

    Returns:
      A future.
    """
    length = len(tokens)

    request = predict_pb2.PredictRequest()
    request.model_spec.name = model_name
    request.inputs["tokens"].CopyFrom(
        tf.make_tensor_proto([tokens], shape=(1, length)))
    request.inputs["length"].CopyFrom(
        tf.make_tensor_proto([length], shape=(1,)))

    return stub.Predict.future(request, timeout)


host = "118.70.81.192"
port = 8378
model_name = "envi"  # en-vi
# model_name="1538773809" #ja-vi
timeout = 60.0

# channel = implementations.insecure_channel(host, port)
# stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

channel = grpc.insecure_channel('118.70.81.192:8378')
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

batch_serving = 128
batch_size = batch_serving - 1


def main_translate(source_sentences, type):
    #parser = argparse.ArgumentParser(description="Translation client example")
    # parser.add_argument("--model_name", required=True,
    #                    help="model name")
    # parser.add_argument("--host", default="localhost",
    #                    help="model server host")
    # parser.add_argument("--port", type=int, default=9000,
    #                    help="model server port")
    # parser.add_argument("--timeout", type=float, default=10.0,
    #                    help="request timeout")
    #args = parser.parse_args()

    # host="localhost"
    # port=6008
    # model_name="1537515987"
    # timeout=10.0
    #channel = implementations.insecure_channel(host, port)
    #stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

    #source_sentences_tokenized = tokenizer(source_sentences_lower, "en")
    source_sentences_tokenized, replaced_ner_inv = replace_english_ner(
        source_sentences)
    #source_sentences_tokenized = tokenizer(source_sentences, "en")
    #from pudb import set_trace; set_trace()
    # print(source_sentences_tokenized)
    source_sentences_lower = []
    for sent in source_sentences_tokenized:
        sent_lower = []
        for token in sent:
            sent_lower.append(token.lower())
        source_sentences_lower.append(sent_lower)
    source_sentences_tokenized = source_sentences_lower
    # for sent in source_sentences:
    #  if len(sent.strip()) > 0:
    #    source_sentences_tokenized.append(word_tokenize(sent.strip().lower()))

    all_batch_tokens = []
    k = 0
    i = 0
    len_sentences = len(source_sentences_tokenized)/batch_size
    while i < len_sentences:
        all_batch_tokens.append(source_sentences_tokenized[k:k+batch_size])
        k += batch_size
        i += 1
    print(all_batch_tokens)

    target_sentences = []
    for batch_tokens in all_batch_tokens:
        # print(batch_tokens)
        futures = []
        for tokens in batch_tokens:
            future = translate(stub, model_name, tokens, timeout=timeout)
            futures.append(future)
    #  from pudb import set_trace; set_trace()

        index = 0
        for tokens, future in zip(batch_tokens, futures):
            result, attention_summary = parse_translation_result(
                future.result())
            #print("{} ||| {}".format(" ".join([str(tok) for tok in tokens]), " ".join([str(res) for res in result])))
            #print("{} ||| {}".format(" ".join(tokens), " ".join(token.decode("utf-8") for token in result)))
            source_arr = [str(token) for token in tokens]
            target_arr = [token.decode("utf-8") for token in result]
            # save image attention
            index += 1

            if (type == "subtitle") and (source_arr[len(source_arr)-1] != target_arr[len(target_arr)-1]):
                target_arr.append(source_arr[len(source_arr)-1])
            # print(target_arr)
            target_arr = restore_ner(target_arr, replaced_ner_inv)
            target = " ".join(target_arr)
            target_sentences.append(target)
            # print(source_arr)
            # print(target_arr)
        #target_sentences = restore_ner(target_sentences, replaced_ner_inv)

    return target_sentences
    # return " ".join(target_sentences)


translated_envi = {}
translated_vien = {}


def load_translated():
    f = open("translated_envi.txt", "r")
    for line in f.readlines():
        en, vi = line.strip().split(" <=> ")
        translated_envi[en] = vi
        translated_vien[vi] = en
    f.close()


# strin = "European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices"
# # strin = "what is your name? How much does it cost. Do you know her favorite"
# print([strin])
# print(main_translate([strin], ""))


def run(strin):
    ignore_tag = ["script", "noscript", "iframe",
                  "svg", "header", "img", "polygon"]
    class_to_translate = ["lesson-name", "caption-text"]

    host = "118.70.81.192"
    port = 8378
    model_name = "envi"  # en-vi
    # model_name="1538773809" #ja-vi
    timeout = 60.0

    # channel = implementations.insecure_channel(host, port)
    # stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

    channel = grpc.insecure_channel("%s:%d" % (host, port))
    stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

    batch_serving = 128
    batch_size = batch_serving - 1

    translated_envi = {}
    translated_vien = {}

    # strin = "European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices"
    # strin = "what is your name? How much does it cost. Do you know her favorite"
    print([strin])
    target_sentences = main_translate([strin], "")
    print(target_sentences)

    return target_sentences


def main():
    strin = "what is your name? How much does it cost. Do you know her favorite"
    run(strin)


if __name__ == '__main__':
    main()
