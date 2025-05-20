import subprocess

def run_all_etl():
    subprocess.run(["python", "etl/extract_firms.py"])
    subprocess.run(["python", "etl/extract_inpe.py"])

if __name__ == "__main__":
    run_all_etl()
