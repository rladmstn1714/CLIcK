# CLIcK: Evaluation of Cultural and Linguistic Intelligence in Korean

## Introduction
CLIcK (Cultural and Linguistic Intelligence in Korean) is a comprehensive dataset designed to evaluate cultural and linguistic intelligence in the context of Korean language models. In an era where diverse language models are continually emerging, there is a pressing need for robust evaluation datasets, especially for non-English languages like Korean. CLIcK fills this gap by providing a rich, well-categorized dataset focusing on both cultural and linguistic aspects, enabling a nuanced assessment of Korean language models.
[paper link](https://arxiv.org/abs/2403.06412) 

## Dataset Description
The CLIcK benchmark comprises two broad categories: Culture and Language, which are further divided into 11 fine-grained subcategories.

### Categories
- **Language**
  - Textual Knowledge
  - Grammatical Knowledge
  - Functional Knowledge
- **Culture**
  - Korean Society
  - Korean Tradition
  - Korean Politics
  - Korean Economy
  - Korean Law
  - Korean History
  - Korean Geography
  - Korean Popular Culture (K-Pop)

### Construction
CLIcK was developed using two human-centric approaches:
1. Reclassification of **official and well-designed exam data** into our defined categories.
2. Generation of questions using ChatGPT, based on **official educational materials** from the Korean Ministry of Justice, followed by our own validation process.

### Structure
The dataset is organized as follows, with each subcategory containing relevant JSON files:
```
📦CLIcK
 └─ Dataset
    ├─ Culture
    │  ├─ [Each cultural subcategory with associated JSON files]
    └─ Language
       ├─ [Each language subcategory with associated JSON files]
```

### Exam Code Descriptions
- KIIP: Korea Immigration & Integration Program ([Website](www.immigration.go.kr))
- CSAT: College Scholastic Ability Test for Korean ([Website](https://www.suneung.re.kr/))
- Kedu: Test of Teaching Korean as a Foreign Language exams ([Website](https://www.q-net.or.kr/man001.do?gSite=L&gId=36))
- PSE: Public Service Exam for 9th grade
- TOPIK: Test of Proficiency in Korean ([Website](https://www.topik.go.kr/))
- KHB: Korean History Exam Basic ([Website](https://www.historyexam.go.kr/))
- PSAT: Public Service Aptitude Test in Korea
- KIIP: Korea Immigration & Integration Program 
