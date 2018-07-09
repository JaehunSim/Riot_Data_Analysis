install.packages("xlsx")
require(xlsx)
data1 <- read.xlsx("C:\\Users\\cy\\Desktop\\cs_grad_project\\riot_data_analysis\\DB_file\\champion_rate.xlsx", sheetName="Sheet1")
data1 <- data.frame(data1)
data_win_rate = data1[2]
boxplot(data_win_rate, xlab="win_rate")

data1_ordered <-data1[order(-data1[,3]),]
data1_summary <-  summary(data1[,3])
data1_ordered[data1_ordered[,3]>pickRate_1stQ]
data1_subset <- subset(data1_ordered, data1_ordered[,3]>pickRate_1stQ)

par(mfrow=c(1,3))
b1 <- boxplot(data1_subset[2], xlab="win_rate")
b2 <- boxplot(data1_subset[3], xlab="pickRate")
b3 <- boxplot(data1_subset[4],xlab= "banRate")

summary(data1_subset[2:4])

data1_win_rate_outlier <- subset(data1_subset,data1_subset[,2] > b1$stats[5])
data1_win_rate_outlier <- data1_win_rate_outlier[order(-data1_win_rate_outlier[,2]),]

data1_pick_outlier <- subset(data1_subset,data1_subset[,3] > b2$stats[5])
data1_pick_outlier <- data1_pick_outlier[order(-data1_pick_outlier[,3]),]

data1_ban_outlier <- subset(data1_subset,data1_subset[,4] > b3$stats[5])
data1_ban_outlier <- data1_ban_outlier[order(-data1_ban_outlier[,4]),]


data1_win_rate_outlier
data1_pick_outlier
data1_ban_outlier

val = c(as.numeric(unlist(data1["PickRate"])), as.numeric(unlist(data1["banRate"])))
fac = gl(n=2,k=140,labels=c("PickRate","banRate"))
aov1 <- aov(val~fac)
summary(aov1)
cor(as.numeric(unlist(data1["PickRate"])),as.numeric(unlist(data1["banRate"])))

val = c(as.numeric(unlist(data1["PickRate"])), as.numeric(unlist(data1["win_rate"])))
fac = gl(n=2,k=140,labels=c("PickRate","win_rate"))
aov1 <- aov(val~fac)
summary(aov1)
cor(as.numeric(unlist(data1["PickRate"])),as.numeric(unlist(data1["win_rate"])))


data2 <- read.csv("C:\\Users\\cy\\Desktop\\cs_grad_project\\riot_data_analysis\\DB_file\\champion_win_ban.csv")
data2 <- data.frame(data2)
val=c(as.numeric(unlist(data2["win"])), as.numeric(unlist(data2["ban"])))
#fac = gl(n=2,k=124900, labels=c("ban","win"))
data2.win <- as.numeric(unlist(data2["win"]))
data2.ban <- as.numeric(unlist(data2["ban"]))

install.packages("vcd")
by(data2[c("ban","win")],data2["ban"],function(x) summary(lm()))
require("vcd")
summary(assocstats(table(data2.win,data2.ban)))

unique_champion_id <- unique(data2["championId"])$championId
data2_id_summary = vector("list",length(unique_champion_id))
i <- 1
for(id in unique_champion_id){
  data2.id = subset(data2,data2["championId"]==id)
  data2.id.win = as.numeric(unlist(data2.id["win"]))
  data2.id.ban = as.numeric(unlist(data2.id["ban"]))
  data2_id_summary[[i]] <- summary(assocstats(table(data2.id.win,data2.id.ban)))$summary$p.value
  i <-  i+1
  }


for(id in data2["championId"]){
  print(id)
}
data2.39 = subset(data2,data2["championId"]==122)
data2.39.win = as.numeric(unlist(data2.39["win"]))
data2.39.ban = as.numeric(unlist(data2.39["ban"]))
summary(assocstats(table(data2.39.win,data2.39.ban)))$summary$p.value
