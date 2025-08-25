import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    person = pd.merge(person, address, how="left")
    return person[['firstName', 'lastName', 'city', 'state']]