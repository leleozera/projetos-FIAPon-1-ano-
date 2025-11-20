# install.packages("tidyverse")

install.packages("tidyverse")
library(tidyverse)

# Lê o CSV
dados <- read.csv("dados/dados_bem_estar.csv", sep = ",", dec = ".", encoding = "UTF-8")

# Olhar a estrutura
str(dados)
summary(dados)

# Converter variáveis categóricas
dados$cargo <- as.factor(dados$cargo)
dados$trabalho_remoto <- factor(dados$trabalho_remoto,
                                levels = c(0,1,2),
                                labels = c("Presencial", "Remoto", "Híbrido"))
dados$risco_burnout <- as.factor(dados$risco_burnout)

# Histograma de horas trabalhadas
ggplot(dados, aes(x = horas_trabalhadas_semanais)) +
  geom_histogram(bins = 20) +
  labs(title = "Distribuição das horas trabalhadas semanais",
       x = "Horas trabalhadas",
       y = "Quantidade de funcionários")

# Boxplot de horas por risco de burnout
ggplot(dados, aes(x = risco_burnout, y = horas_trabalhadas_semanais)) +
  geom_boxplot() +
  labs(title = "Horas trabalhadas x Risco de burnout",
       x = "Risco de Burnout (0 = baixo, 1 = alto)",
       y = "Horas semanais")

# Humor médio por risco de burnout
dados %>%
  group_by(risco_burnout) %>%
  summarise(humor_medio = mean(humor_diario),
            engajamento_medio = mean(pontuacao_engajamento)) %>%
  print()
