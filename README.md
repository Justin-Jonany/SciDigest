# SciDigest

With the growth of many fields, more papers are published annually. Researchers need to read tons of journals, but reading through hundreds of unstructured abstracts is time-consuming and irritating. 

SciDigest is a deep learning model that structures abstracts to help researchers save time when reading scientific journals. This model receives abstracts as inputs and turns them into a structured abstract.

### [Example 1](https://iopscience.iop.org/article/10.1088/1751-8121/ac4b13)
**Input:**
> We classify four qubit states under SLOCC operations, that is, we classify the orbits of the group on the Hilbert space . We approach the classification by realising this representation as a symmetric space of maximal rank. We first describe general methods for classifying the orbits of such a space. We then apply these methods to obtain the orbits in our special case, resulting in a complete and irredundant classification of -orbits on . It follows that an element of is conjugate to an element of precisely 87 classes of elements. Each of these classes either consists of one element or of a parameterised family of elements, and the elements in the same class all have equal stabiliser in . We also present a complete and irredundant classification of elements and stabilisers up to the action of where Sym4 permutes the four tensor factors of .

**Output:**
> BACKGROUND
> 
> We classify four qubit states under SLOCC operations, that is, we classify the orbits of the group on the Hilbert space. We approach the classification by realising this representation as a symmetric space of maximal rank. We first describe general methods for classifying the orbits of such a space. We then apply these methods to obtain the orbits in our special case, resulting in a complete and irredundant classification of -orbits on.
> 
> RESULTS
> 
> It follows that an element of is conjugate to an element of precisely 87 classes of elements.
> 
> METHODS
> 
> Each of these classes either consists of one element or of a parameterised family of elements, and the elements in the same class all have equal stabiliser in .
> 
> RESULTS
> 
> We also present a complete and irredundant classification of elements and stabilisers up to the action of where Sym4 permutes the four tensor factors of .

### [example 3](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6078146/)
**Input:**
> The aim of this paper is to map the scientific landscape related to cancer research worldwide between 2012 and 2017. We use scientific publication data from Web of Science Core Collection and combine bibliometrics and social network analysis techniques to identify the most relevant journals, research areas, countries and research organizations in cancer scientific landscape. The results show: Oncotarget as the journal with most publications; a significant increase in China’s publications, reaching United States’ publications in 2017; MD Cancer Center, University of California and Harvard University as organizations with most publications; cell biology as the most frequent research area; breast, lung and colorectal cancer as the most frequent keywords; high density of co-authorship between organizations in the West, especially in the US, and low density between organizations in Asian and lower and medium income countries. Our findings can be used to guide a global knowledge platform guiding policy, planning and funding decisions as well as to establish new institutional collaborations.

**Output:**
>BACKGROUND
>
> The aim of this paper is to map the scientific landscape related to cancer research worldwide between 2012 and 2017. We use scientific publication data from Web of Science Core Collection and combine bibliometrics and social network analysis techniques to identify the most relevant journals, research areas, countries and research organizations in cancer scientific landscape.
> 
> 
> RESULTS
>
> The results show: Oncotarget as the journal with most publications; a significant increase in China’s publications, reaching United States’ publications in 2017; MD Cancer Center, University of California and Harvard University as organizations with most publications; cell biology as the most frequent research area; breast, lung and colorectal cancer as the most frequent keywords; high density of co-authorship between organizations in the West, especially in the US, and low density between organizations in Asian and lower and medium income countries.
> 
> CONCLUSIONS
>
> Our findings can be used to guide a global knowledge platform guiding policy, planning and funding decisions as well as to establish new institutional collaborations.

**SciDigest** is trained on [PubMed 200k RCT dataset](https://github.com/Franck-Dernoncourt/pubmed-rct).

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

## Usage
Refer to the [**Usage.ipynb**](https://github.com/Justin-Jonany/SciDigest/blob/4d9cae9a452b49270c993894f83132208b0f9323/Usage.ipynb)

1. Download the [**model**](https://github.com/Justin-Jonany/SciDigest/blob/4d9cae9a452b49270c993894f83132208b0f9323/best_model.keras)
2. Download the [**structurizer module**](https://github.com/Justin-Jonany/SciDigest/blob/main/structurizer_module.py)
3. Call the `preprocess_and_strucurizer` function from the module passing it the **model from 1.** and the **abstract** to structurize
