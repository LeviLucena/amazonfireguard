# Pipeline ETL inicial

def run_etl_pipeline():
    from etl.extract_inpe import save_inpe
    save_inpe()
