
import os
import torch
from simpletransformers.question_answering import QuestionAnsweringModel
import json

from transformers import BertModel

train_args = {
    'fp16':False,
    'learning_rate': 3e-5,
    'num_train_epochs': 2,
    'max_seq_length': 384,
    'doc_stride': 128,
    'overwrite_output_dir': True,
    'reprocess_input_data': False,
    'train_batch_size': 2,
    'gradient_accumulation_steps': 8,
}

model = QuestionAnsweringModel(
    'flaubert', './outputs/flaubert/checkpoint-2650-epoch-2/', args=train_args, use_cuda=True)

with open('./data/illiun/json_output/third_output.json', 'r') as f:
    sur_train_data = json.load(f)

sur_train_data = [item for topic in sur_train_data['data']
              for item in topic['paragraphs']]

model.train_model(sur_train_data)