# Generating Music using an LSTM Neural Network

## Poster
![poster.png](./poster.png)

## Abstract
Music is a repetitious art form. Musical elements, such as melodic themes, rhythmic patterns, or harmonic progressions, often appear multiple times throughout a work, meaning memory and contextual understanding is critical to music composition. Prior research in LSTM music generation has primarily focused on classical music. In this study, we investigate generating more modern genres. We selected classical Chopin and Schumann as controls, and compared the performance of LSTM architectures on jazz and anime soundtracks (a type of Japanese pop music). After conducting a survey, we found our LSTM models were able to generate modern music on par with the controls.

## Data
We collected several midi datasets of Schumann pieces, Chopin mazurkas, anime soundtracks, and jazz pieces. For the Schumann and Chopin pieces, we used the piano-midi database [2]. For the anime soundtracks we scraped SheetHost [3], and for jazz we used Bushgrafts [4]. The Python library music21 was utilized to preprocess the data and isolate piano parts. The first 14,000 notes of each dataset were selected as input for our network. 


## Methods



## Results

## Conclusion

## Contributors

- [Kailash Subramanian](https://github.com/kaisubr)
- [Daniel Angel](https://github.com/danielkangel)
- [Nick Sangha](https://github.com/Nirvair-Sangha)
- [Keerthi Srilakshmidaran](https://www.linkedin.com/in/keerthi-srilakshmidaran/)
- [Viswajith Rajagopalan](https://github.com/ViswajithRajagopalan) - Research Lead
- [Dr. Doug DeGroot](https://cs.utdallas.edu/people/faculty/degroot-doug/) - Faculty Advisor
