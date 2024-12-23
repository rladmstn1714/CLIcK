<div align="center">
  <h1>CLIcK 🇰🇷🧠</h1>
  <p>CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean</p>
  <p>
    <a href="https://huggingface.co/datasets/EunsuKim/CLIcK"><img src="https://img.shields.io/badge/Huggingface-CLIcK-blue" alt="Dataset"></a>
    <a href="https://arxiv.org/abs/2403.06412"><img src="https://img.shields.io/badge/Paper-LREC--COLING-green" alt="Paper"></a>
  </p>
</div>


## Introduction 🎉

CLIcK (Cultural and Linguistic Intelligence in Korean) is a comprehensive dataset designed to evaluate cultural and linguistic intelligence in the context of Korean language models. In an era where diverse language models are continually emerging, there is a pressing need for robust evaluation datasets, especially for non-English languages like Korean. CLIcK fills this gap by providing a rich, well-categorized dataset focusing on both cultural and linguistic aspects, enabling a nuanced assessment of Korean language models.

## News 📰

- **[LREC-COLING]** Our paper introducing CLIcK has been accepted to LREC-COLING 2024!🎉
- **[3/20]** We revise some grammatical errors in the dataset. Test with the new version of CLIcK!
  
## Dataset Description 📊

The CLIcK benchmark comprises two broad categories: Culture and Language, which are further divided into 11 fine-grained subcategories.

### Categories 📂

- **Language** 🗣️
  - Textual Knowledge
  - Grammatical Knowledge
  - Functional Knowledge

- **Culture** 🌍
  - Korean Society
  - Korean Tradition
  - Korean Politics
  - Korean Economy
  - Korean Law
  - Korean History
  - Korean Geography
  - Korean Popular Culture (K-Pop)


### Construction 🏗️

CLIcK was developed using two human-centric approaches:

1. Reclassification of **official and well-designed exam data** into our defined categories.
2. Generation of questions using ChatGPT, based on **official educational materials** from the Korean Ministry of Justice, followed by our own validation process.

### Structure 🏛️

The dataset is organized as follows, with each subcategory containing relevant JSON files:

```
📦CLIcK
 └─ Dataset
    ├─ Culture
    │  ├─ [Each cultural subcategory with associated JSON files]
    └─ Language
       ├─ [Each language subcategory with associated JSON files]
```

### Exam Code Descriptions 📜

- KIIP: Korea Immigration & Integration Program ([Website](www.immigration.go.kr))
- CSAT: College Scholastic Ability Test for Korean ([Website](https://www.suneung.re.kr/))
- Kedu: Test of Teaching Korean as a Foreign Language exams ([Website](https://www.q-net.or.kr/man001.do?gSite=L&gId=36))
- PSE: Public Service Exam for 9th grade
- TOPIK: Test of Proficiency in Korean ([Website](https://www.topik.go.kr/))
- KHB: Korean History Exam Basic ([Website](https://www.historyexam.go.kr/))
- PSAT: Public Service Aptitude Test in Korea

## Results

| Models            | Average Accuracy (Korean Culture) | Average Accuracy (Korean Language) |
|-------------------|-----------------------------------|------------------------------------|
| Polyglot-Ko 1.3B  | 32.71%                            | 22.88%                             |
| Polyglot-Ko 3.8B  | 32.90%                            | 22.38%                             |
| Polyglot-Ko 5.8B  | 33.14%                            | 23.27%                             |
| Polyglot-Ko 12.8B | 33.40%                            | 22.24%                             |
| KULLM 5.8B        | 33.79%                            | 23.50%                             |
| KULLM 12.8B       | 33.51%                            | 23.78%                             |
| KoAlpaca 5.8B     | 32.33%                            | 23.87%                             |
| KoAlpaca 12.8B    | 33.80%                            | 22.42%                             |
| LLaMA-Ko 7B       | 33.26%                            | 25.69%                             |
| LLaMA 7B          | 35.44%                            | 27.17%                             |
| LLaMA 13B         | **36.22%**                        | **26.71%**                         |
| GPT-3.5           | 49.30%                            | 42.32%                             |
| Claude2           | **51.72%**                        | **45.39%**                         |


## Dataset Link 🔗

The CLIcK dataset is available on the Hugging Face Hub: [CLIcK Dataset](https://huggingface.co/datasets/EunsuKim/CLIcK)


## Citation 📝

If you use CLIcK in your research, please cite our paper:

```bibtex
@misc{kim2024click,
      title={CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean}, 
      author={Eunsu Kim and Juyoung Suk and Philhoon Oh and Haneul Yoo and James Thorne and Alice Oh},
      year={2024},
      eprint={2403.06412},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Contact 📧

For any questions or inquiries, please contact [kes0317@kaist.ac.kr](mailto:kes0317@kaist.ac.kr).
