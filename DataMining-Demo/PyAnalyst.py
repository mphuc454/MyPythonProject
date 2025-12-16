import pandas as pd

df = pd.read_csv(r'D:\ThuMucCuaTui\Programmer\DataMining\File\chipotle.csv', sep="\t")
# print(df.head(5))
# print(df.shape)
# print(df.info())
# print(df.columns.tolist())
print(df.describe(include='all'))
# print(df.index)
# print(df.loc[(df.quantity == 2) & (df.item_name == "Chicken Bowl"), ['order_id','quantity','item_name']])
# print(df.iloc[:11, 0:3])
# print(df.item_price.apply(lambda x : x.replace('$','')))
# df.item_price = df.item_price.apply(lambda x : float(x.replace('$','')))
# df["total_price"] = df["quantity"] * df["item_price"]
# s =df.groupby("item_name")["quantity"].sum()
# print(s.sort_values())
# print(df.item_name.value_counts().count())
# print(df.item_name.nunique())

