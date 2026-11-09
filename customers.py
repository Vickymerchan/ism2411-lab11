# 1. I would use bracket notation when the key has to be there, because a KeyError tells me something is wrong with
#    the data. I would use .get() when a key might be missing because it gives me a default and my program
#    keeps running. 
# 2. The summary dictionary reminds me of a pivot table  Excel, where you add up amounts for each category like region. The
#    Python version could be more useful for large datasets because the same loop works on millions of rows without freezing, and I can
#    rerun it automatically on new data instead of rebuilding the sheet.




# ---------------- EXERCISE 1: One customer ----------------
print("EXERCISE 1")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
 
# ---------------- EXERCISE 2: Update and add ----------------
print("\nEXERCISE 2")
customer["phone"] = "555-123-4567"      # add a new field
print(customer)
customer["tier"] = "platinum"           # update an existing field
print(customer)
del customer["email"]                   # delete a field
print(customer)
 
# ---------------- EXERCISE 3: Safe lookup ----------------
print("\nEXERCISE 3")
# .get() returns the default instead of crashing when the key is missing
print(customer.get("email", "no email on file"))
 
# bracket notation raises a KeyError when the key is missing
try:
    print(customer["email"])
except KeyError:
    print("KeyError: 'email' is not in the dictionary")
 
# ---------------- EXERCISE 4: Iterate ----------------
print("\nEXERCISE 4")
for key, value in customer.items():
    print(f"{key}: {value}")
 
# Looping without .items() only gives the keys, not the values.
# .items() gives (key, value) pairs, so we can print both.
for key in customer:
    print(key)
 
# ---------------- EXERCISE 5: Lookup table ----------------
print("\nEXERCISE 5")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
discount = tier_discounts.get(customer["tier"], 0)   # default 0 if tier is unknown
price = 200
final_price = price * (1 - discount)
print(f"Tier: {customer['tier']} | Discount: {discount:.0%} | Final price: ${final_price:.2f}")
 
# ---------------- EXERCISE 6: List of dicts ----------------
print("\nEXERCISE 6")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Ben", "tier": "silver"},
    {"name": "Carla", "tier": "bronze"},
]
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    saved = 300 * rate
    print(f"{c['name']} ({c['tier']}): discount ${saved:.2f} on a $300 purchase")
 
# ---------------- EXERCISE 7: Nested catalog ----------------
print("\nEXERCISE 7")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")
 
# ---------------- EXERCISE 8: Sales by region ----------------
print("\nEXERCISE 8")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]
 
for region in sorted(summary):
    print(f"{region}: {summary[region]}")
 