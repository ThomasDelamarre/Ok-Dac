import json
import os


class QuestionType:
    question_types = {
        'who': 0,
        'what': 0,
        'when': 0,
        'how_much': 0,
        'where': 0,
        'how': 0,
        'why': 0,
        'others': 0
    }

    def __init__(self,
                 directory_input='data/json_output/', directory_output='data/stats_output/'):
        self.directory_input = directory_input
        self.directory_output = directory_output
        self.output = {
            "stats": [{
                "question type": []
            }]
        }

    def get_question_types(self):

        for file in os.listdir(self.directory_input):
            if file[-4:] == 'json':
                with open(self.directory_input + file, 'r') as f:
                    json_file = json.load(f)

        paragraphs = json_file['data'][0]['paragraphs']

        for paragraph in paragraphs:
            for qas in paragraph['qas']:
                question = qas['question']
                first_word = question.split(' ')[0].lower()
                if first_word == 'comment':
                    self.question_types['how'] += 1
                elif first_word in ['quel', 'quelle', 'quels', 'quelles', 'que', 'qu', 'de']:
                    self.question_types['what'] += 1
                elif first_word in ['où', 'ou', 'dans']:
                    self.question_types['where'] += 1
                elif first_word == 'qui':
                    self.question_types['who'] += 1
                elif first_word == 'quand':
                    self.question_types['when'] += 1
                elif first_word == 'combien':
                    self.question_types['how_much'] += 1
                elif first_word == 'pourquoi':
                    self.question_types['why'] += 1
                else:
                    self.question_types['others'] += 1

        for question_type in self.question_types:
            self.output['stats'][0]['question type'].append(
                {'type': question_type,
                 'count': self.question_types[question_type]}
            )

        os.makedirs(self.directory_output, exist_ok=True)

        with open(self.directory_output + 'stats.json', 'w', encoding='utf8', ) as outfile:
            json.dump(self.output, outfile, indent=4, ensure_ascii=False)


questionType = QuestionType()
questionType.get_question_types()
