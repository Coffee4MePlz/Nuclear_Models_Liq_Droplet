# Nuclear_Models_Liq_Droplet
This is a simple code for calculating the valence bands of a nucleus, according to the Liquid Droplet Model in Nuclear Physics. We also calculate the binding energy of the nuclides and plot for certain values.

I developed this code with the help of [AnthonyAposta](https://github.com/AnthonyAposta) for our Nuclear Physics Course at our home university (Universidade Federal de Santa Catarina - UFSC), if you like what we are doing, you should also check his profile. 

## In detail:

We took our raw data (the isotopes descriptions) from the [Nuclear Energy Agency](https://www.oecd-nea.org/dbdata/data/mass-evals2003/mass.mas03) website. The archive is originally a .txt (which is a poor choice of structured data). So we filtered the information we found relevant and built an [.csv archive](https://gist.githubusercontent.com/AnthonyAposta/3a4457b2e23ffce13c133ba8a97d3149/raw/ae38df1e49607b76cbc263bc914bb112429eb737/isotopos.csv), under the name of *isotopos.csv* in this repository. 

The binding energy can be calculated under the Bond.py code. If one wishes to calculate the plot for the valence band, the function is under the name "gota_liquida". 

## Maind Script ModNucl.py

General information on specific Isotopes can be calculated in the main script of this repository "ModNucl.py". There is also an option for writing it directly as a LateX table, if necessary.

## Here are some plots, enjoy:

Binding Energy with deleted parameters: 

![Binding Energy with choice of parameters](https://github.com/Coffee4MePlz/Nuclear_Models_Liq_Droplet/blob/master/Bond_Plot.png)

Liquid Droplet Plots: With R=1,beta=1,gamma=1

![R=1,beta=1,gamma=1](https://github.com/Coffee4MePlz/Nuclear_Models_Liq_Droplet/blob/master/LiquidD_111.png)

Liquid Droplet Plots: With R=1,beta=4,gamma=30

![R=1,beta=4,gamma=30](https://github.com/Coffee4MePlz/Nuclear_Models_Liq_Droplet/blob/master/LiquidD_3041.png)

Liquid Droplet Plots: With R=1,beta=8,gamma=60

![R=1,beta=8,gamma=60](https://github.com/Coffee4MePlz/Nuclear_Models_Liq_Droplet/blob/master/LiquidD_60081.png)




