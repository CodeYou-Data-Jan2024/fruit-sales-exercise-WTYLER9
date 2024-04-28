import pandas as pd

fruits_sales = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]},  index = ["2017 Sales","2018 Sales"])
fruits_sales.to_csv("fruit.csv", encoding="utf-8")


