import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\practical 10")  # 替换为实际路径
print(os.getcwd())  # 验证当前目录
print(os.listdir())  # 查看目录内容，确认数据文件存在
# 导入数据
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# 查看前5行数据
print(dalys_data.head(5))

# 查看数据信息
print(dalys_data.info())

# 查看数据统计信息
print(dalys_data.describe())
# 显示前10行的第3列(年份)
years = dalys_data.iloc[0:10, 2]  # 或 dalys_data.iloc[:10, 2]
print(years)

# 注释：阿富汗第10个有DALYs数据的年份是____(根据实际数据填写)
# 选择1990年的所有数据
year_1990 = dalys_data.loc[dalys_data["Year"] == 1990, :]
print(year_1990)

# 或者只选择DALYs列
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print(dalys_1990)
# 选择英国和法国的数据
uk= dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
france= dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]

# 计算均值
uk_mean = uk["DALYs"].mean()
france_mean = france["DALYs"].mean()

print(f"UK mean DALYs: {uk_mean}")
print(f"France mean DALYs: {france_mean}")

# 注释：英国的DALYs均值比法国大/小(根据实际结果填写)
if uk_mean>france_mean:
    print("UK mean DALYs is bigger than France mean DALYs")
plt.plot(uk.Year, uk.DALYs, 'r+')
plt.xticks(uk.Year,rotation=-90)
plt.show()

#Anser the additional question

uk_data = dalys_data[dalys_data["Entity"] == "United Kingdom"]
france_data = dalys_data[dalys_data["Entity"] == "France"]


fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))


axes[0].plot(uk_data["Year"], uk_data["DALYs"], 'b-', label="UK")
axes[0].set_title("DALYs in the United Kingdom")
axes[0].set_ylabel("DALYs")
axes[0].legend()


axes[1].plot(france_data["Year"], france_data["DALYs"], 'r-', label="France")
axes[1].set_title("DALYs in France")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("DALYs")
axes[1].legend()


plt.tight_layout()
plt.show()


         
