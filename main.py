def elektr_energiyasi_hisobi(kwt):
    if 0 <= kwt <= 100:
        return kwt * 5
    else:
        return 800

kwt = float(input("Elektr energiyasi kuchi (kWt): "))
print(f"Elektr energiyasi hisobi: {electr_energiyasi_hisobi(kwt)} so'm")
```

```python
def elektr_energiyasi_hisobi(kwt):
    return min(800, max(kwt * 5, 500))

kwt = float(input("Elektr energiyasi kuchi (kWt): "))
print(f"Elektr energiyasi hisobi: {electr_energiyasi_hisobi(kwt)} so'm")
