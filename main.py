from simpletransformers.question_answering import QuestionAnsweringModel
import json


with open('data/train-v2.0.json', 'r') as f:
    train_data = json.load(f)

train_data = [item for topic in train_data['data']
              for item in topic['paragraphs']]


train_args = {
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
    'bert', 'bert-base-cased', args=train_args, use_cuda=False)

model.train_model(train_data)


with open('data/dev-v2.0.json', 'r') as f:
    dev_data = json.load(f)

dev_data = [item for topic in dev_data['data'] for item in topic['paragraphs']]

preds = model.predict(dev_data)

os.makedirs('results', exist_ok=True)

submission = {pred['id']: pred['answer'] for pred in preds}

with open('results/submission.json', 'w') as f:
    json.dump(submission, f)
