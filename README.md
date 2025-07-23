# 🔬 Research Code for Style Matters: Improving Authorship Classification with Personalized Linguistic Style in Spoken Language

> ⚠️ **Note**: The full codebase will be made publicly available after the publication of the article.
> For now, **only the dataset preprocessing module is included** in this repository. Please check back after the official release of the paper.

## 🧾 Abstract

Personalized linguistic style (PLS) is one modality that manifests the phenomenon of interpersonal synchrony. This topic has recently attracted researchers' interest primarily because it has the potential to enhance the human-like features of natural language processing applications. Despite this growing attention, there exist very few methodologies capable of effectively representing an individual's linguistic style in the context of spoken language.
In this paper, we highlight the importance of PLS through its application to the authorship classification problem. In this context, our work introduces a novel perspective by incorporating stylistic information to enhance classification performance.
To achieve this, we integrate PLS into pre-trained transformer-based models using two key techniques: fine-tuning with cross-entropy loss and contrastive learning via a Siamese architecture. 
We show that integrating personalized linguistic style into embeddings leads to improved classification accuracy compared to baseline models that do not consider spoken stylistic features. These findings reinforce the hypothesis that each individual exhibits a unique linguistic style, which can be used to improve authorship classification.

## 🗂️ Repository Structure
This repository is organized into four main components:
├── Preprocess/ # Dataset preprocessing pipeline 
│ └── dataset_source.txt
│ └── code_general.py
│
├── baseline/ # Baseline model implementation 
├── first_approach/ # First proposed approach
└── second_approach/ # Second proposed approach


## Requirements
- Python >= 3.10
- PyTorch >= 2.0.0	
- pandas	>= 1.5.3
- sentence-transformers 5.0.0
- Wandb
