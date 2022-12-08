# https://github.com/ycroissant/plm
# https://www.rdocumentation.org/packages/plm/versions/2.6-2/topics/plm
# https://stackoverflow.com/questions/44197708/how-does-the-plm-package-handle-fixed-effects-one-dummy-for-each-individual-or

library(plm)
library(stargazer)
library(haven)
library(readxl)

# Carregando base
df <- read_excel("base_regressao.xlsx")
df <- pdata.frame(df, index = c("id_municipio_7digitos", "ano"))

# Pooling MQO
reg_mqo <- lm(obitos_pc ~ upa_pc + populacao + samu + pib,
    data = df
)

# Regressões LSDV
lsdv_1 <- lm(obitos_pc ~ upa_pc + populacao + samu + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido),
    data = df
)

# Inserir variáveis de controle
lsdv_2 <- lm(obitos_pc ~ upa_pc + populacao + samu + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido),
    data = df
)

### A partir daqui eu mudo as variáveis dependentes

# Óbitos em casa 
lsdv_3 <- lm(mortes_domicilio_pc ~ upa_pc + populacao + samu + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido),
    data = df
)

# Na rua
lsdv_4 <- lm(mortes_via_publica_pc ~ upa_pc + populacao + samu + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido),
    data = df
)

# No hospital
lsdv_5 <- lm(mortes_hospital_pc ~ upa_pc + populacao + samu + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido),
    data = df
)

# Em outros estabelecimentos de saúde
lsdv_6 <- lm(mortes_outro_estab_saude_pc ~ upa_pc + populacao + samu + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido),
    data = df
)


stargazer(lsdv_1,
    lsdv_2,
    lsdv_3,
    type = "text",
    title= "",
    out.header = TRUE,
    model.names = FALSE,
    model.numbers = TRUE,
    multicolumn = TRUE,
    keep = c("upa_pc", "Constante")

)
