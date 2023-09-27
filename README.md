# CLICK: Evaluation of Cultural and Linguistic IntelligenCe in Korean

The CLICK is the dataset for evaluating cultural and linguistic intelligence in Korea.
With the emergence of numerous LLMs trained on diverse corpora, comprehensive evaluation datasets for comparing them have become crucial. The same holds for Korean LLMs as Korean LLMs are continually released. However, there is no comprehensive open-sourced evaluation dataset for Koreans.
The CLICK, which contains well-categorized data from culture and language parts, can figure out those and find fine-grained limitations of LLMs in Korean.

## **Dataset Description**

CLICK benchmark is composed of 2 course-grained categories, Culture and Language, and 11 fine-grained categories. 

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

### Description of Exam code
- KIIP : Korea Immigration & Integration Program, www.immigration.go.kr
- CSAT : College Scholastic Ability Test for Korean, https://www.suneung.re.kr/
- Kedu : Test of Teaching Korean as a Foreign Language exams, https://www.q-net.or.kr/man001.do?gSite=L&gId=36
- PSE : Public Service Exam for 9 grad 
- TOPIK : Test of Proficiency in Korean, https://www.topik.go.kr/
- KHB : Korean History Exam Basic, https://www.historyexam.go.kr/

## Status

- 230908 [Version 1] Upload
    - The questions of the following categories are uploaded, but they are not yet validated by humans.
        - Language: Contextual Knowledge, Functional Knowledge
        - Culture: Korean Tradition, Korean Politics, Korean Economy, Korean Law, Korean History, Korean Geography
- 230925 [Version 2] Upload
    - The questions of each category are all validated by 3 human annotators and uploaded.
    - Data from all categories except culture/Korean tradition are uploaded.
    - "Korean pop culture" is added as a new subcategory of Korean culture.
    - "Sociallinguistic" category is deleted. 
- 230927 [Version 3] Upload
    - Data of culture/Korean tradition are uploaded.
    - Additional data from the 'Test of Teaching Korean as a Foreign Language exams' are added. 

