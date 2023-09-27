# CLICK: Evaluation of (C)ultural and (L)inguistic (I)ntelligen(C)e in (K)orean

The CLICK is the dataset for evaluating cultural and linguistic intelligence in Korean. It is known that LLMs are not working well in low resourced language, including Korean. To emphasize these problems, it is needed to figure out where LLMs works good and where they don’t in the view of culture and language. The CLICK, which contains the well-categorized data from culture and language parts, can figure out those and find fine-grained limitations of LLMs in Korean.

## **Dataset Description**

CLICK benchmark is composed of 2 course-grained categories,Culture and Language, and 11 fine-grained categories. 

### Category

- Language
    - Contextual Knowledge
    - Grammatical Knowledge 
    - Functional Knowledge
- Culture
    - Korean Society
    - Korean Tradition
    - Korean Politics
    - Korean Economy
    - Korean Law
    - Korean History
    - Korean Geography
    - Korean Popular Culture (Korean Popular)

### **Construction**

We constructed the CLICK in two human-centric ways;

1. We utilized **official and well-designed exam data** and reclassified it according to our categories
2. Based on the **official educational materials** from Korean Ministry of Justice, We let **ChatGPT** create questions. We will then validate the questions on our own.


### Structure
```
📦 
├─ .gitignore
├─ Dataset
│  ├─ Culture
│  │  ├─ Korean Economy
│  │  │  └─ Economy_KIIP.json
│  │  │  └─ Economy_Kedu.json
│  │  ├─ Korean Geography
│  │  │  ├─ Geography_CSAT.json
│  │  │  └─ Geography_KIIP.json
│  │  │  └─ Geography_Kedu.json
│  │  ├─ Korean History
│  │  │  ├─ History_KHB.json
│  │  │  └─ History_PSE.json
│  │  │  └─ History_Kedu.json
│  │  ├─ Korean Law
│  │  │  ├─ Law_KIIP.json
│  │  │  └─ Law_PSAT.json
│  │  ├─ Korean Politics
│  │  │  └─ Politics_KIIP.json
│  │  │  └─ Politics_Kedu.json
│  │  ├─ Korean Pop culture
│  │  │  └─ Pop_KIIP.json
│  │  │  └─ Pop_Kedu.json
│  │  └─ Korean Society
│  │     └─ Society_KIIP.json
│  │     └─ Society_Kedu.json
│  │  └─ Korean Tradition
│  │     └─ Tradition_KIIP.json
│  │     └─ Tradition_Kedu.json
│  └─ Language
│     ├─ Contextual
│     │  ├─ Contextual_CSAT.json
│     │  └─ Contextual_TOPIK.json
│     ├─ Functional
│     │  ├─ Functional_CSAT.json
│     │  ├─ Functional_Kedu.json
│     │  └─ Functional_PSE.json
│     └─ Grammar
│        ├─ Grammar_CSAT.json
│        ├─ Grammar_Kedu.json
│        └─ Grammar_TOPIK.json
└─ README.md
```



## Current Status

- 230908 [Version 1] Upload
    - The questions of following categories are uploaded, but they are not yet validated by human.
        - Language: Contextual Knowledge, Functional Knowledge
        - Culture: Korean Tradition, Korean Politics, Korean Economy, Korean Law,Korean History,Korean Geography

## TBD
- The questions of following categories will be updated soon, with more official exam data.
    - Language: Grammatical Knowledge, Sociallinguistic Knowledge
    - Culture: Korean Tradition, Korean Politics, Korean Economy, Korean Law,Korean History,Korean Geography
- The questions from each categories will be classified into two,high & low, based on difficulties.
