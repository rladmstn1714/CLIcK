<div align="center">
  <h1>CLIcK 🇰🇷🧠</h1>
  <p>Evaluation of Cultural and Linguistic Intelligence in Korean</p>
  <p>
    <a href="https://huggingface.co/datasets/scottsuk0306/CLIcK"><img src="https://img.shields.io/badge/Dataset-CLIcK-blue" alt="Dataset"></a>
    <a href="https://arxiv.org/abs/2403.06412"><img src="https://img.shields.io/badge/Paper-LREC--COLING-green" alt="Paper"></a>
    <a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey" alt="License"></a>
  </p>
</div>


## Introduction 🎉

CLIcK (Cultural and Linguistic Intelligence in Korean) is a comprehensive dataset designed to evaluate cultural and linguistic intelligence in the context of Korean language models. In an era where diverse language models are continually emerging, there is a pressing need for robust evaluation datasets, especially for non-English languages like Korean. CLIcK fills this gap by providing a rich, well-categorized dataset focusing on both cultural and linguistic aspects, enabling a nuanced assessment of Korean language models.

## News 📰

- **[LREC-COLING]** Our paper introducing CLIcK has been accepted to LREC-COLING 2024!🎉

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
- KIIP: Korea Immigration & Integration Program

## Dataset Link 🔗

The CLIcK dataset is available on the Hugging Face Hub: [CLIcK Dataset](https://huggingface.co/datasets/your_username/CLIcK)

## License 📜

This dataset is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

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

For any questions or inquiries, please contact [your_email@example.com](mailto:your_email@example.com).
