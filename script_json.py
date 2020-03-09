import json
import os


class JsonTransformer:
    question_counter = 0

    def __init__(self,
                 directory_input='json_input/',
                 directory_output='json_output/'):
        self.directory_input = directory_input
        self.directory_output = directory_output
        self.output = {
            "data": [{
                "paragraphs": []
            }]}

    def transform_all_json(self):

        for file in os.listdir(self.directory_input):
            if file[-4:] == "json":

                print("Doing " + file)

                with open(self.directory_input + file, 'r') as f:
                    json_file = json.load(f)

                if len(json_file["annotations"]) > 0:
                    questions = json_file["annotations"][0]["value"]
                    if len(questions) > 0:
                        qas = []
                        context = json_file["rawString"].replace("\n", " ")
                        for i in questions:
                            if (len(i["question"]) > 0) & (len(i["answer"]) > 0) & (i["answer_start"] < len(context)):
                                buff = {"question": i["question"],
                                        "id": self.question_counter,
                                        "answers": [{"text": i["answer"].replace("\n", " "),
                                                     "answer_start": i["answer_start"]}]}
                                self.question_counter += 1
                                qas.append(buff)

                        transformed = {'qas': qas, 'context': context}
                        self.output["data"][0]["paragraphs"].append(transformed)
                    print("Done for " + file + "\n")

        with open(self.directory_output + "output.json", 'w', encoding='utf8') as outfile:
            json.dump(self.output, outfile, indent=4, ensure_ascii=False)

        print("All done")


jt = JsonTransformer(directory_input='data/annotations/', directory_output='data/json_output/')
jt.transform_all_json()
