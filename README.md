<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Author List</title>
    <style>
        .author-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            text-align: center;
            margin: 0 auto;
            max-width: 800px; /* Adjust as needed */
        }
        .author {
            flex: 1 1 25%;
            box-sizing: border-box;
            padding: 10px;
        }
        .single-author {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
        }
    </style>
</head>

<div style="display: flex; justify-content: space-between; align-items: center;">
   <div>
        <a href="README.md"><img src="assets/us-flag.svg" alt="US Flag" style="width:30px; height:auto;"></a>
        <a href="README_PTBR.md"><img src="assets/brazil-flag.svg" alt="Brazil Flag" style="width:30px; height:auto; margin-left: 10px;"></a>
    </div> 
</div>

# What is the impact of the presence of Emergency Care Units (UPAs) on the number of deaths in cities of São Paulo?

<body>
    <div class="author-container">
        <div class="author">
            <strong>Ruth Pereira di Rada</strong><br>
        </div>
        <div class="author">
            <strong>Ryan Alef de Souza Costa</strong><br>
        </div>
        <div class="author">
            <strong>Vitor Baldoino</strong><br>
        </div>
    </div>
</body>
<br>


Recently, the COVID-19 pandemic has highlighted the importance of public health issues, bringing to light concerns about the collapse of emergency hospital services. Based on studies [5](#references) and [6](#references), this paper aims to evaluate the impact of 24-hour Emergency Care Units (UPAs) on mortality rates in municipalities in the state of São Paulo, using a panel data structure for the period from 2010 to 2019.

_The work was developed within the scope of the Econometrics II course taught in the 2nd semester of 2022 at FEA-USP._

## Contents

- _What is the impact of the presence of Emergency Care Units (UPAs) on the number of deaths in municipalities of São Paulo?_
  - [`.pdf` version](/reports/IMPACTO_DAS_UPAS_NA_MORTALIDADE_EM_SP.pdf).
  - [`.ipynb` version](/notebooks/impacto-upas-sp-econometria-ii.ipynb).
  - [Presentation](/reports/APRESENTACAO_IMPACTOS_DAS_UPAS.pdf).

- _Scripts_
   - [Data extraction from `Base dos Dados`](/src/dataset.sql).
   - [`.csv` files processing](/src/dataset.py).
   - [Regression tables](/src/models.R).

## Folder Structure

```text
├── LICENSE
├── README.md 
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
│
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── notebooks          <- Jupyter notebooks.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── src                <- Source code for use in this project.
│   │
│   ├─ dataset.py      <- Script to download or generate data
│   ├─ dataset.sql     <- Queries used to download data from Base dos Dados
│   ├─ models.R        <- Script to fit models
│   ├─ results.py      <- Script to display tables in notebooks
│ 

```


## References

> 1. Heiss F. Using R for Introductory Econometrics. Düsseldorf: Independently published; 2020.
> 
> 2. Heiss F, Brunner D. Using Python for Introductory Econometrics. New York: Independently published; 2020.
> 
> 3. Wooldridge JM. Introductory Econometrics: A Modern Approach. Sixth edition, student edition. Boston, MA: Cengage Learning; 2016.
> 
> 4. Mendonça MJC de, Motta RS da. Saúde e saneamento no Brasil. Texto para Discussão (TD) 1081: Saúde e saneamento no Brasil. Disponível em: https://repositorio.ipea.gov.br/handle/11058/2079
> 
> 5. Rocha R, Fernandes LM da S. O Impacto das Unidades de Pronto Atendimento (UPAs) 24h sobre indicadores de mortalidade: evidências para o Rio de Janeiro. Disponível em: https://repositorio.ipea.gov.br/handle/11058/7503
> 
> 6. Silva MF da, Santos JO, Alves J da S. Impacto das Unidades de Pronto Atendimento 24h sobre indicadores de morbimortalidade: uma análise com dados em painel para o estado do Rio Grande do Norte e região metropolitana de Natal no período 2010-2016. Revista Meta: Avaliação. 31 de agosto de 2020.

*** 

If you have any questions or any other issues, please email me at [vdbaldoino@gmail.com](mailto:vdbaldoino@gmail.com?subject=Hi!%20I%20saw%20your%20GitHub!) or send me a message on [LinkedIn](https://www.linkedin.com/in/vitorbaldoino/).
