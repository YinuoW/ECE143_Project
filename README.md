# ECE143_GroupProject

## Airline (top)

### Delay

#### Trends
#### Departure delay (mean)/Arrived delay, time, airlines
time = year, month, day
#### Delay frequency, airlines
#### Time slot (早中晚), delay frequency, airlines
#### < 15 min/ > 15min (percentage)
#### first few longest delay, airline, airport

#### Reasons
#### airlines(top), reasons, percentage of times

### Cancellation

#### Cancell frequency, airlines
#### Time slot (早中晚), cancell frequency, airlines


#### Arrived delay 


----

### Departure Airport

#### resons (persentage) (stack bar chart)

----

### Arrived Airport
----


To do:
- Maps: arrival (changed from departure)
- Statistical description of airlines: number of flights per airline
- Airlines vs departure delay (intervals), scatter plot
- Scoring system
	- formula
	- implementation
- Delay distribution to establish ranking of airlines
- Delay airlines by cities (heat map)
- Jupyter compliation & GitHub

Completed:
- For 18 airlines, stacked plot of reasons why the airline was delayed 
- For 18 airlines, stacked plot delay rate and on-time/advanced time (normalized)
- For 18 airlines, stacked plot delay and on-time/advanced time (not normalized), sorted ascending
- Map of all airports in US
- Departure map of airport, color maps

Outline of presentation: 
- Introduction: background, maps of airports
- Visualization:
	- Delay (day, month, year)
		- all airline & delay rate, on-time/advanced
    - reasons why airline delayed
	- Cancelations:
		- reasons
- How can this visualization help us? With a scoring system



---- lllllllll
total tips:
1) only consider departure delay time and frequency
2) only consider first 18 airlines(how to choose these 18?) 
3) only consider XX airports
4) attention to the line's colors( shadow, deep, choice of colors
## from the proposal
outlines:
① identify correkations between delays(cancellatons)between other paramaters(airlines,airports,travel seasons)
1) delay time： 
2008年到2019年的每年的average delay time ，
2018年每个月的 average delay time ， 
找六月的 average delay time
加上18个airlines， XX个airports，
plot: aera plot or line chart or 水平柱状图（x轴 delay time，y轴每个月+每个airpot） or 做成matrix 颜色深浅表示delay time多少

delay time在 airline/airport的分布
plot:stack bar： 三个bar：lagre delay>45' small delay 5'< <45‘  on time <5'  在每个airport or airline 各自占的百分比 

不同的delay reason 有不同的时间,在每次发生delay上的占比， x轴为？？？？
plot：stack bar y轴不同的航空公司 

每个airline每年的delay time 的分布
plot： box chart x轴为每个airline，y轴为 delay time 的分布 的箱线图(有grid比较清楚

每个airport每年的delay time 的分布
plot： box chart x轴为每个airline，y轴为 delay time 的分布 的箱线图(有grid比较清楚

2018年每个airline delay time对比
plot： 横向柱状图 y轴 18个airlines x轴 2018年的avg delay time（avg到每个航班

2018年每个airport delay time对比
plot： 横向柱状图 y轴 XX个airports x轴 2018年的avg delay time（avg到每个航班


2）delay frequency：
2008年到2019年的每年的average delay frequency ，
2018年每个月的 average delay frequency， 
找六月的 average delay frequency，
 加上18个airlines， XX个airports，
plot: aera plot or line chart or 做成matrix 颜色深浅表示delay frequency多少

每个airline每年的delay frequency 的分布
plot： box chart x轴为每个airline，y轴为 delay frequency 的分布 的箱线图

2018年每个airline delay frequency对比
plot： 横向柱状图 y轴 18个airlines x轴 2018年的avg delay frequency（avg到每个航班

2018年每个airport delay frequency对比
plot： 横向柱状图 y轴 XX个airports x轴 2018年的avg delay frequency（avg到每个航班


3)cancellation frequency
2008年到2019年的每年的average cancellation frequency ，
2018年每个月的 average cancellation frequency， 
找六月的 average cancellation frequency，
 加上18个airlines， XX个airports，
plot: aera plot or line chart 



② score system
1）三角图 几个元素几角

2）横向柱状图给出评分 最高分100 


#### Information Might be Useful

##### Pick up airlines

Top 10 largest US Airlines:
Source: https://en.wikipedia.org/wiki/List_of_largest_airlines_in_North_America

|Rank|Airline|Code|Passenger numbers|
|---|---|---|---|
|1|American Airlines|AA|203,745,000|
|2|Delta Air Lines|DL|192,465,271|
|3|Southwest Airlines|WN|163,605,833|
|4|United Airlines|UA|158,330,000|
|5|Alaska Airlines|AS|45,802,000|
|6|JetBlue Airways|B6|42,149,989|
|7|Spirit Airlines|NK|29,312,000|
|8|Frontier Airlines|F9|18,669,000|
||Allegiant Air||13,606,103|
|9|Hawaiian Airlines|HA|11,840,178|
||Sun Country Airlines||2,089,000|
|10|Virgin America(Not sure)|VX||

Airlines in our **2018** data (check the `airline2018_lookup.csv` in our 'data' file. This file contains airlines' codes and their names.):

|Code|Airline Name|
|---|---|
|'9E'| 'Endeavor Air Inc. (2013 - )'|
|'AA'| 'American Airlines Inc. (1960 - )'|
|'AS'| 'Alaska Airlines Inc. (1960 - )'|
|'B6'| 'JetBlue Airways (2000 - )'|
|'DL'| 'Delta Air Lines Inc. (1960 - )'|
|'EV'| 'ExpressJet Airlines Inc. (2012 - 2019)'|
|'F9'| 'Frontier Airlines Inc. (1994 - )'|
|'G4'| 'Allegiant Air (2000 - )'|
|'HA'| 'Hawaiian Airlines Inc. (1960 - )'|
|'MQ'| 'Envoy Air (2014 - )'|
|'NK'| 'Spirit Air Lines (1992 - )'|
|'OH'| 'PSA Airlines Inc. (2015 - )'|
|'OO'| 'SkyWest Airlines Inc. (2003 - )'|
|'UA'| 'United Air Lines Inc. (1960 - )'|
|'VX'| 'Virgin America (2007 - 2018)'|
|'WN'| 'Southwest Airlines Co. (1979 - )'|
|'YV'| 'Mesa Airlines Inc. (1995 - )'|
|'YX'| 'Republic Airline (2017 - )'|

##### Pick up airports

There are 359 **origin** and **destination** airports in our 2018 dataset. See the `airport2018_lookup.csv` in our 'data' file. This file contains airports' codes and their names.
