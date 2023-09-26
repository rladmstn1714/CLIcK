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
    - Korean Pop culture

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
│  │  ├─ Korean Geography
│  │  │  ├─ Geo_CSAT.json
│  │  │  └─ Geo_KIIP.json
│  │  ├─ Korean History
│  │  │  ├─ History_KHB.json
│  │  │  └─ History_PSE.json
│  │  ├─ Korean Law
│  │  │  ├─ Law_KIIP.json
│  │  │  └─ Law_PSAT.json
│  │  ├─ Korean Politics
│  │  │  └─ Politics_KIIP.json
│  │  ├─ Korean Pop culture
│  │  │  └─ Pop_KIIP.json
│  │  └─ Korean Society
│  │     └─ Society_KIIP.json
│  └─ Language
│     ├─ Contextual
│     │  ├─ context_CSAT.json
│     │  └─ context_TOPIK.json
│     ├─ Functional
│     │  ├─ func_CSAT.json
│     │  ├─ func_Kedu.json
│     │  └─ func_PSE.json
│     └─ Grammar
│        ├─ GR_CSAT.json
│        ├─ GR_Kedu.json
│        └─ GR_TOPIK.json
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
