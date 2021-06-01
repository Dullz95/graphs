import matplotlib.pyplot as plt

temp = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
soup_sales = [220, 330, 190, 340, 410, 445, 415]

plt.scatter(temp, soup_sales)
plt.title("soup sales in relation to temperatures")
plt.xlabel("temperature")
plt.ylabel("price in (R)")
plt.show()
