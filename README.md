# Sound Search Questionnaire

[![arXiv](https://img.shields.io/badge/arXiv-2410.08324-b31b1b.svg)](https://arxiv.org/abs/2410.08324) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13622537.svg)](https://doi.org/10.5281/zenodo.13622537)

A streamlit-based web application for conducting a user study on possible search queries in online sound collections.
The results of the survey were used in the following [paper](https://dcase.community/documents/workshop2024/proceedings/DCASE2024Workshop_Weck_54.pdf):

> B. Weck and F. Font, ‘The Language of Sound Search: Examining User Queries in Audio Search Engines’, in Proceedings of the Detection and Classification of Acoustic Scenes and Events 2024 Workshop (DCASE2024), Tokyo, Japan, Oct. 2024, pp. 181–185.

The results of the survey are available at [Zenodo](https://doi.org/10.5281/zenodo.13622537).

## Stimuli Data
There are three types of stimuli: text descriptions, audio clips, and images.

1. The text descriptions and associated audio clips are sourced from [Clotho](https://doi.org/10.5281/zenodo.4783391) and selected using relevance judgements from the [TAU Audio-Text Graded Relevances 2023 Dataset](https://github.com/xieh97/retrieval-relevance-crowdsourcing).
2. The audio clips are selected from [Freesound](https://freesound.org/), specifically [FSD50K](https://zenodo.org/record/4060432).
3. The images were sourced from [Openverse](https://openverse.org/) to fit audio clips from [Freesound](https://freesound.org/).

## Citation

If you use this code or the results of the survey, please cite the following paper:

```bibtex
@inproceedings{Weck2024,
    author = "Weck, Benno and Font, Frederic",
    title = "The Language of Sound Search: Examining User Queries in Audio Search Engines",
    booktitle = "Proceedings of the Detection and Classification of Acoustic Scenes and Events 2024 Workshop (DCASE2024)",
    address = "Tokyo, Japan",
    month = "October",
    year = "2024",
    pages = "181--185",
    abstract = "This study examines textual, user-written search queries within the context of sound search engines, encompassing various applications such as foley, sound effects, and general audio retrieval. Current research inadequately addresses real-world user needs and behaviours in designing text-based audio retrieval systems. To bridge this gap, we analysed search queries from two sources: a custom survey and Freesound website query logs. The survey was designed to collect queries for an unrestricted, hypothetical sound search engine, resulting in a dataset that captures user intentions without the constraints of existing systems. This dataset is also made available for sharing with the research community. In contrast, the Freesound query logs encompass approximately 9 million search requests, providing a comprehensive view of real-world usage patterns. Our findings indicate that survey queries are generally longer than Freesound queries, suggesting users prefer detailed queries when not limited by system constraints. Both datasets predominantly feature keyword-based queries, with few survey participants using full sentences. Key factors influencing survey queries include the primary sound source, intended usage, perceived location, and the number of sound sources. These insights are crucial for developing user-centred, effective text-based audio retrieval systems, enhancing our understanding of user behaviour in sound search contexts."
}
```
