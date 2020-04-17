# Ok-Dac

Projet de développement d'un système de questions-réponses automatique en français dans le cadre du cours des Données à la Connaissance de l'option OSY de l'école CentraleSupélec.
Ce système utilise des modèles pré-entraînés de compréhension du langage naturel en français s'inspirant du modèle pour l'anglais Bert (flauBert et camemBert) et permettra tout particulièrement de donner des réponses sur le thème d'Harry Potter.

- Le fichier configure permet de bien configurer le projet pour l'utilisation des machines du mésocentre qui nous était fourni.
Les fichiers .pbs permettent d'executer sur ces machines les scripts qui leurs sont associés (train_dual_gpu.pbs éxécute le script main.py).

- Le dossier data contient les données ayant permis l'entraînement de notre modèle.
Plus précisément, les sets de données de fquad (dev-v2.0.json, etc.) et, dans le sous-dossier annotations, les questions que nous avons annoté nous-même sur le thème d'Harry Potter.
Le dossier json_output contient la concaténation de nos annotations.

- script_json.py: permet la concaténation des annotations en un seul fichier json.

- train_camembert.py: permet l'entraînement d'un modèle Camembert grâce à la libraire simpletransformers sur le set de fsquad

- train_flaubert.py: permet l'entraînement d'un modèle Flaubert grâce à la libraire simpletransformers sur le set de fsquad

- sur_train_flaubert.py: permet le surentraînement du modèle Flaubert grâce à la libraire simpletransformers sur nos annotations

- main.py: permet l'entraînement d'un modèle Bert sur le set de fsquad et de tester une prédiction