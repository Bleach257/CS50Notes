name = "传智博客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor= 1.2
groth_days = 7
finally_stock_price = stock_price*stock_price_daily_growth_factor**groth_days

print(f"公司：{name},股票代码：{stock_code},当前股价:{stock_price},")
print("每日增长系数：%f,经过 %d天增长后,股价达到了%.2f "%(stock_price_daily_growth_factor,groth_days,finally_stock_price))