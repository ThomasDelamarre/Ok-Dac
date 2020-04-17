# Ok-Dac

Projet de développement d'un système de questions-réponses automatique en français dans le cadre du cours des Données à la Connaissance de l'option OSY de l'école CentraleSupélec.
Ce système utilise des modèles pré-entraînés de compréhension du langage naturel en français s'inspirant du modèle pour l'anglais Bert (flauBert et camemBert) et permettra tout particulièrement de donner des réponses sur le thème d'Harry Potter.

- Le fichier *__configure__* permet de bien configurer le projet pour l'utilisation des machines du mésocentre qui nous était fourni.
Les fichiers *__.pbs__* permettent d'executer sur ces machines les scripts qui leurs sont associés (train_dual_gpu.pbs éxécute le script main.py).

- Le dossier *__data__* contient les données ayant permis l'entraînement de notre modèle.
Plus précisément, les sets de données de *__fquad*__ (dev-v2.0.json, etc.) et, dans le sous-dossier *__annotations*__, les questions que nous avons annoté nous-même sur le thème d'Harry Potter.
Le dossier *__json_output*__ contient la concaténation de nos annotations.
Le dossier *__stats_output*__ contient les données de quelques statistiques enregistrées dans un fichier json.

- *__script_json.py*__: permet la concaténation des annotations en un seul fichier json.

- *__stats.py*__ et *__statDataset.py*__: donne quelques statistiques sur nos annotations.

- *__train_camembert.py*__: permet l'entraînement d'un modèle Camembert grâce à la libraire simpletransformers sur le set de fsquad

- *__train_flaubert.py*__: permet l'entraînement d'un modèle Flaubert grâce à la libraire simpletransformers sur le set de fsquad

- *__sur_train_flaubert.py*__: permet le surentraînement du modèle Flaubert grâce à la libraire simpletransformers sur nos annotations

- *__main.py*__: permet l'entraînement d'un modèle Bert sur le set de fsquad et de tester une prédiction
