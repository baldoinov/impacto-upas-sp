<div style="display: flex; justify-content: space-between; align-items: center;">
   <div>
        <a href="README.md"><img src="assets/us-flag.svg" alt="US Flag" style="width:30px; height:auto;"></a>
        <a href="README_PTBR.md"><img src="assets/brazil-flag.svg" alt="Brazil Flag" style="width:30px; height:auto; margin-left: 10px;"></a>
    </div> 
</div>

# Qual o impacto da presença de UPAs no nº de mortes dos municípios de São Paulo?

Recentemente, a pandemia da covid-19 destacou a importância das questões de saúde pública, trazendo à tona preocupações sobre o colapso dos atendimentos de emergência hospitalar. Tendo como referência os estudos [5](#referências) e [6](#referências), este trabalho procura avaliar empiricamente o impacto das Unidades de Pronto Atendimento (UPAs) 24h nas taxas de mortalidade dos municípios do estado de São Paulo, utilizando uma estrutura de dados em painel para o período de 2010-2019.

*O trabalho foi desenvolvido no âmbito do curso de Econometria II ministrado no 2º semestre de 2022 na FEA-USP*.

## Conteúdos

- _O impacto das Unidades de Pronto Atendimento (UPAs) 24h sobre indicadores de mortalidade: uma análise para o Estado de São Paulo no período 2010–2019_
  - [Versão em `.pdf`](/reports/IMPACTO_DAS_UPAS_NA_MORTALIDADE_EM_SP.pdf).
  - [Versão em `.ipynb`](/notebooks/impacto-upas-sp-econometria-ii.ipynb).
  - [Apresentação](/reports/APRESENTACAO_IMPACTOS_DAS_UPAS.pdf).

- _Scripts_
   - [Extração da `Base dos Dados`](/src/dataset.sql).
   - [Tratamento dos arquivos `.csv` do Datasus](/src/dataset.py).
   - [Geração das tabelas de regressão](/src/models.R).


## Estrutura do Repositório

```text
├── LICENSE
├── README.md 
├── requirements.txt   <- O arquivo de requisitos para reproduzir o ambiente
├── setup.py           <- Torna o projeto instalável via pip (`pip install -e .`) para que src possa ser importado
│
├── data
│   ├── interim        <- Dados intermediários que foram transformados.
│   ├── processed      <- Os conjuntos de dados finais para modelagem.
│   └── raw            <- Dados originais e imutáveis.
│
├── notebooks          <- Jupyter Notebooks.
│
├── reports            <- Análises geradas em HTML, PDF, LaTeX, etc.
│
├── src                <- Código-fonte para uso neste projeto.
│   │
│   ├─ dataset.py      <- Script para tratar dados
│   ├─ dataset.sql     <- Queries usadas para baixar dados da Base dos Dados
│   ├─ models.R        <- Script para rodar os modelos
│   ├─ results.py      <- Script para exibir tabelas no notebook
│ 
```

## Referências

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

Em caso de dúvidas ou quaisquer outras questões, você pode me mandar um [e-mail](mailto:vdbaldoino@gmail.com?subject=GitHub%20-%20Econometria) ou me mandar uma mensagem pelo [LinkedIn](https://www.linkedin.com/in/vitorbaldoino/).
