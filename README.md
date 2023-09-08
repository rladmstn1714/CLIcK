# CLIcK:evaluation of Cultural and Linguistic Intelligence in Korean

The CLIcK is the dataset for evaluating cultural and linguistic intelligence in Korean. It is known that LLMs are not working well in low resourced language, including Korean. To emphasize these problems, it is needed to figure out where LLMs works good and where they don’t in the view of culture and language. The CLIcK, which contains the well-categorized data from culture and language parts, can figure out those and find fine-grained limitations of LLMs in Korean.

## **Dataset Description**

CLIcK benchmark is composed of 2 course-grained categories,Culture and Language, and 11 fine-grained categories. 

### Category

- Language
    - Contextual Knowledge
    - Grammatical Knowledge
    - Functional Knowledge
    - Sociallinguistic Knowledge
- Culture
    - Korean Society
    - Korean Tradition
    - Korean Politics
    - Korean Economy
    - Korean Law
    - Korean History
    - Korean Geography
- Culture
    - Korean Society
    - Korean Tradition
    - Korean Politic

### **Construction**

We constructed the CLIcK in two human-centric ways;

1. We utilized **official and well-designed exam data** and reclassified it according to our categories
2. Based on the **official educational materials** from Korean Ministry of Justice, We let **ChatGPT** create questions. We will then validate the questions on our own.

## Current Status

- 230908 [Version 1] Upload
    - The questions of following categories are uploaded, but they are not yet validated by human.
        - Language: Contextual Knowledge, Functional Knowledge
        - Culture: Korean Tradition, Korean Politics, Korean Economy, Korean Law,Korean History,Korean Geography
    - The questions of following categories will be updated soon, with more official exam data.
        - Language: Grammatical Knowledge, Sociallinguistic Knowledge
        - Culture: Korean Tradition, Korean Politics, Korean Economy, Korean Law,Korean History,Korean Geography
