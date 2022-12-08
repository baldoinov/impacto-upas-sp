# Ruth Pereira di Rada - 11764685
# Ryan Alef de Souza Costa - 11883820
# Vitor Domingos Baldoino dos Santos - 11766857

library(plm)
library(stargazer)
library(haven)
library(readxl)
library(tidyr)

#---- Visualizando os dados gerais ----# 

str(base_regressao)

summary(base_regressao)

#---- Organização ----# 


#carregando a base
df <- read_excel("base_regressao.xlsx")

#construindo painel
df <- pdata.frame(df, index = c("id_municipio_7digitos", "ano"))

#vars utilizadas:
    #id_municipio_7digitos, ano
    #obitos_pc, mortes_domicilio_pc, mortes_via_publica_pc, mortes_hospital_pc, mortes_outro_estab_saude_pc,
    #UPA_pc
    #samu_d,
    #partido,
    #pib_pc,
    #ligacoes_agua_pc
    #volume_esgoto_tratado_pc

#---- Rodando as regressões ----# 

#MQO
reg.pooling <- lm(obitos_pc ~ upa_pc + as.factor(partido) + as.factor(samu_d) + log(pib_pc) + ligacoes_agua_pc + volume_esgoto_tratado_pc,
                  data = df
)

#efeitos aleatorios
reg.random_effects <- plm(obitos_pc ~ upa_pc + as.factor(partido) + as.factor(samu_d) + log(pib_pc) + ligacoes_agua_pc + volume_esgoto_tratado_pc,
                          data = df,
                          model = "random",
)

#efeitos fixos

#EF - within - mortes totais
reg.fixed_effects <- plm(obitos_pc ~ upa_pc + as.factor(partido) + as.factor(samu_d) + log(pib_pc) + ligacoes_agua_pc + volume_esgoto_tratado_pc,
                         data = df,
                         model = "within",
)

#LSDV - mortes totais

reg.lsdv1 <- plm(obitos_pc ~ upa_pc + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido),
                 data = df,
                 model = "within"
)

reg.lsdv2 <- plm(obitos_pc ~ upa_pc  + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido) + as.factor(samu_d),
                 data = df,
                 model = "within"
)


# https://stackoverflow.com/questions/44197708/how-does-the-plm-package-handle-fixed-effects-one-dummy-for-each-individual-or
reg.lsdv3 <- plm(obitos_pc ~ upa_pc + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido) + as.factor(samu_d) + log(pib_pc) + ligacoes_agua_pc + volume_esgoto_tratado_pc,
                 data = df,
                 model = "within"
)

#LSDV - outros tipos de morte
reg.lsdv4 <- plm(mortes_domicilio_pc ~ upa_pc + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido) + as.factor(samu_d) + log(pib_pc) + ligacoes_agua_pc + volume_esgoto_tratado_pc,
                 data = df,
                 model = "within"
)

reg.lsdv5 <- plm(mortes_via_publica_pc ~ upa_pc + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido) + as.factor(samu_d) + log(pib_pc) + ligacoes_agua_pc + volume_esgoto_tratado_pc,
                 data = df,
                 model = "within"
)

reg.lsdv6 <- plm(mortes_hospital_pc ~ upa_pc + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido) + as.factor(samu_d) + log(pib_pc) + ligacoes_agua_pc + volume_esgoto_tratado_pc,
                 data = df,
                 model = "within"
)

reg.lsdv7 <- plm(mortes_outro_estab_saude_pc ~ upa_pc + as.factor(ano) + as.factor(id_municipio_7digitos) + as.factor(partido) + as.factor(samu_d) + log(pib_pc) + ligacoes_agua_pc + volume_esgoto_tratado_pc,
                 data = df,
                 model = "within"
)

#teste de Breusch-Pagan
bptest(reg.lsdv3, reg.random_effects)

#teste de Hausman
testeh <- phtest(reg.lsdv3, reg.random_effects)

#gerar tabela stargazer

stargazer(reg.pooling, reg.fixed_effects, reg.lsdv1, reg.lsdv2, reg.lsdv3, reg.lsdv4, reg.lsdv5, reg.lsdv6, reg.lsdv7,
          type="text", 
          keep=c("upa_pc", "samu", "partido", "pib_pc", "ligacoes_agua_pc","volume_esgoto_tratado_pc"),
          keep.stat=c("n","rsq", "adj.rsq"),
          column.labels = c("MQO", "EF", "LSDV1", "LSDV2", "LSDV3", "CASA", "RUA","HOSP","UPAout")) 

#1
stargazer(reg.pooling, reg.fixed_effects, reg.lsdv1, reg.lsdv2, reg.lsdv3,
          type="text", 
          keep=c("upa_pc", "samu", "partido", "pib_pc", "ligacoes_agua_pc","volume_esgoto_tratado_pc"),
          keep.stat=c("n","rsq", "adj.rsq"),
          column.labels = c("MQO", "EF", "LSDV1", "LSDV2", "LSDV3")) 

#2
stargazer(reg.lsdv4, reg.lsdv5, reg.lsdv6, reg.lsdv7,
          type="text", 
          keep=c("upa_pc", "samu", "partido", "pib_pc", "ligacoes_agua_pc","volume_esgoto_tratado_pc"),
          keep.stat=c("n","rsq", "adj.rsq"),
          column.labels = c("CASA", "RUA","HOSP","UPAout"))
