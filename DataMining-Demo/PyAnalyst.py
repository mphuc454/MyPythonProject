import pandas as pd


df = pd.read_csv(r'D:\ThuMucCuaTui\Programmer\PythonProject\DataMining-Demo\File\chipotle.csv', sep="\t")
# df.fillna(df["choice_description"]=="Something", inplace=True)
# print(df.to_string())
print(df.head(10))
# print(df.tail().to_string())
# print(df.info())
# new_df = df.dropna()
# print(new_df.info())
# a = [0,5,6]
# my_num = pd.Series(a)
# print(my_num)
# data = {
#     "Height":[340,200, 150],
#     "Weight":[1009, 2001,None]
# }
# df = pd.DataFrame(data)
# # print(df)
# print(df.loc[0])

