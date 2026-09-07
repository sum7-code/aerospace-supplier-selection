import pandas as pd
import matplotlib.pyplot as plt

# Supplier dataset
data = {
    "Supplier": [
        "AeroTech",
        "SkyParts",
        "NovaAero",
        "Falcon Components",
        "Orion Aerospace",
        "Vector Systems",
        "Titan Components",
        "Apex Aerospace"
    ],
    "Cost": [82, 76, 90, 70, 85, 78, 73, 88],
    "Quality": [91, 85, 96, 79, 89, 87, 82, 93],
    "Delivery": [88, 94, 91, 83, 96, 89, 86, 92],
    "Risk": [75, 82, 88, 65, 90, 79, 70, 85],
    "Sustainability": [80, 72, 91, 68, 86, 77, 74, 89]
}

df = pd.DataFrame(data)

# Weighted supplier score
df["Supplier Score"] = (
    df["Cost"] * 0.20 +
    df["Quality"] * 0.25 +
    df["Delivery"] * 0.20 +
    df["Risk"] * 0.20 +
    df["Sustainability"] * 0.15
)

# Rank suppliers
df["Rank"] = df["Supplier Score"].rank(
    ascending=False,
    method="min"
).astype(int)

df = df.sort_values("Rank")

print("\nSUPPLIER RANKING")
print("=" * 50)
print(df[["Rank", "Supplier", "Supplier Score"]].to_string(index=False))

# Identify the best supplier
best_supplier = df.iloc[0]

print("\nRECOMMENDED SUPPLIER")
print("=" * 50)
print(f"Supplier: {best_supplier['Supplier']}")
print(f"Score: {best_supplier['Supplier Score']:.2f}")

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Supplier"], df["Supplier Score"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("Weighted Supplier Score")
plt.xlabel("Supplier")
plt.title("Supplier Performance Ranking")
plt.tight_layout()

plt.savefig("supplier_ranking.png", dpi=300)
plt.show()
