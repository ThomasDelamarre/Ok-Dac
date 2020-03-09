import os, sys, shutil
import time
from simpletransformers.question_answering import QuestionAnsweringModel
import json
from contextlib import contextmanager

# @contextmanager
# def timer(name):
#     t0 = time.time()
#     yield
#     print(f'[{name}] done in {time.time() - t0:.0f} s')


# USE_APEX = True

# if USE_APEX:
#             with timer('install Nvidia apex'):
#                 # Installing Nvidia Apex
#                 os.system('git clone https://github.com/NVIDIA/apex; cd apex; pip install -v --no-cache-dir' + 
#                           ' --global-option="--cpp_ext" --global-option="--cuda_ext" ./')
#                 os.system('rm -rf apex/.git') # too many files, Kaggle fails
#                 from apex import amp

with open('data/fquad-train.json', 'r') as f:
    train_data = json.load(f)

train_data = [item for topic in train_data['data']
              for item in topic['paragraphs']]


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
    'flaubert', 'flaubert-base-cased', args=train_args, use_cuda=True)

model.train_model(train_data)


with open('data/dev-v2.0.json', 'r') as f:
    dev_data = json.load(f)

dev_data = [item for topic in dev_data['data'] for item in topic['paragraphs']]

preds = model.predict(dev_data)

os.makedirs('results', exist_ok=True)

submission = {pred['id']: pred['answer'] for pred in preds}

with open('results/submission.json', 'w') as f:
    json.dump(submission, f)
