from app.services.inpe import fetch_inpe_data

def save_inpe():
    df = fetch_inpe_data()
    df.to_csv("data/inpe_data.csv", index=False)
    print("Dados INPE salvos com sucesso.")

if __name__ == "__main__":
    save_inpe()
