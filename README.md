# SciDigest

With the growth of many fields, more papers are published annually. Researchers need to read tons of journals, but reading through hundreds of unstructured abstracts is time-consuming and irritating. 

SciDigest is a deep learning model that structures abstracts to help researchers save time when reading scientific journals. This model receives abstracts as inputs and turns them into a structured abstract.

**SciDigest** will be trained on [PubMed 200k and 20k RCT dataset](https://github.com/Franck-Dernoncourt/pubmed-rct).

Some of the model architecture will be referenced and based on:
* [Paper 1](https://arxiv.org/pdf/1710.06071.pdf)
* [Paper 2](https://arxiv.org/pdf/1612.05251.pdf)

**Note:** There's no source code given from the paper, everything here will my take on the paper's explaination

## Goal
The goal of this project:
1. Replicate the model architecture in **Paper 2**
2. Beat the F1-Score of the model in **Paper 1**, that is **91.6**

## Model Architecture from [Paper 2](https://arxiv.org/pdf/1612.05251.pdf)

![image](https://drive.google.com/uc?export=view&id=1237sz70ncTkzRxKoIufBSh3Q-xkUcuHt)

## My Implementation
![image](https://drive.google.com/uc?export=view&id=11XziiCR8e1CGwj_ecwCiuOJN_t_rvUcS)

Aside from the things that are not explained in the paper, and I decide on myself, here's a few changes:
1. My implementation of label optimization
2. Using Adam optimizer instead of SGD
3. Using a custom-trained embedding layer instead of GloVe


The best model's F1-score is **0.890/89.0** which is **0.026/2.6** lower than the target of **91.6**. This model didn't succeed in reaching the goal. There are several things that can be improved with more time and computing power:
1. Adding some batch normalization layers
2. Adapting embedding layers on all the training sentences
3. Experimenting with the learning rate
4. Experiment with batch size.

## Results
The best model's F1-score is **0.890/89.0** which is **0.026/2.6** lower than the target of **91.6**. This model didn't succeed in reaching the goal. There are several things that can be improved with more time and computing power:
1. Adding some batch normalization layers
2. Adapting embedding layers on all the training sentences
3. Experimenting with the learning rate
4. Experiment with batch size.

![image](https://drive.google.com/uc?export=view&id=1-4-U0t7Q6zCS-YroKJCkIiSGo0yINlbD)

![image](https://drive.google.com/uc?export=view&id=1-4tpBMgiPMCTqIhPYcaTZNJixcn9mtHl)

## Example Output
Soon coming
