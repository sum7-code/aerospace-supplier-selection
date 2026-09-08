

## About the Project

I created this project to explore how data can be used to compare aerospace suppliers and support supplier selection.

The project looks at five areas of supplier performance:

* Cost
* Quality
* Delivery
* Risk
* Sustainability

I used Python to analyse the data and compare the suppliers across these different areas.

> The supplier data in this project is simulated and is used for portfolio purposes.

## What I Did

I:

* Loaded and organised the supplier data using Pandas
* Compared suppliers across the five criteria
* Used a weighted scoring method to calculate overall supplier performance
* Identified differences and trade-offs between suppliers
* Created charts to make the results easier to compare
* Documented the analysis and results on GitHub

## Dataset

| Supplier          | Cost | Quality | Delivery | Risk | Sustainability |
| ----------------- | ---: | ------: | -------: | ---: | -------------: |
| AeroTech          |   82 |      91 |       88 |   75 |             80 |
| SkyParts          |   76 |      85 |       94 |   82 |             72 |
| NovaAero          |   90 |      96 |       91 |   88 |             91 |
| Falcon Components |   70 |      79 |       83 |   65 |             68 |
| Orion Aerospace   |   85 |      89 |       96 |   90 |             86 |

Higher scores represent better performance.

## Method

I used a weighted scoring approach to combine the five criteria into an overall supplier score.

This allows the suppliers to be compared using several factors rather than choosing a supplier based on cost or one other measure alone.
## Results


The analysis produced the following overall supplier comparison:

<img src="Visualisations/supplier_ranking.png" alt="Supplier Ranking">

## Tools

* Python
* Pandas
* Matplotlib
* GitHub

## Project Structure

```text
aerospace-supplier-selection/
│
├── data/
│   └── suppliers.csv
│
├── analysis/
│   └── supplier_analysis.py
│
├── visualisations/
│   └── supplier_scores.png
│
└── README.md
```

## What I Learned

This project gave me practical experience using Python to work with data and turn several different measures into a structured comparison.

It also helped me understand how the way criteria are weighted can affect a supplier-selection decision.

## Future Improvements

If I continued developing the project, I would add more suppliers, test different weighting scenarios and use a larger dataset.

## Author

**Sumayah Akhter**

BSc Mathematics Student

GitHub: [sum7-code](https://github.com/sum7-code)

