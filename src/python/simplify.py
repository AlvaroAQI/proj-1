import pandas as pd

# Ruta del archivo base
input_file = "../../data/NOX-2020-ext.csv"
output_folder = "../../data/"

# Leer CSV original separado por tabuladores
df = pd.read_csv(input_file, sep="\t")

# -----------------------------
# 1️⃣ counties.csv: códigos y nombres de condados
# -----------------------------
counties = df[["State.Code", "County.Code", "County.Name"]].drop_duplicates()
counties.to_csv(f"{output_folder}counties.csv", index=False, sep="\t")

# -----------------------------
# 2️⃣ states.csv: códigos y nombres de estados
# -----------------------------
states = df[["State.Code", "State.Name"]].drop_duplicates()
states.to_csv(f"{output_folder}states.csv", index=False, sep="\t")

# -----------------------------
# 3️⃣ methods.csv: códigos y nombres de métodos
# -----------------------------
methods = df[["Method.Code", "Method.Name"]].drop_duplicates()
methods.to_csv(f"{output_folder}methods.csv", index=False, sep="\t")

print("CSV generados correctamente en la carpeta 'data/'")