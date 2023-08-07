tasks = """
Imports the data into a data structure of your choice
Loops over the rows in the dataset
For each row in the dataset checks to see if the ear length is large (>10 cm) or small (<=10 cm) and determines the GC-content of the DNA sequence (i.e., the percentage of bases that are either G or C)
Stores this information in a table where the first column has the ID for the individual, the second column contains the string ‘large’ or the string ‘small’ depending on the size of the individuals ears, and the third column contains the GC content of the DNA sequence.
Prints the average GC-content for both large-eared elves and small-eared elves to the screen.
Exports the table of individual level GC values to a CSV (comma delimited text) file titled grangers_analysis.csv.
"""

import urllib.request
from collections import Counter

import pandas as pd

url = "https://nyu-cds.github.io/courses/data/houseelf_earlength_dna_data.csv"


def get_data(url) -> pd.DataFrame:
    response = urllib.request.urlopen(url)
    return pd.read_csv(response)


def gc_percent(seq: str) -> float:
    counter = Counter(seq)
    return (counter["G"] + counter["C"]) / len(seq) * 100


def categorize_earlengths(df: pd.DataFrame) -> pd.Series:
    return df.earlength.apply(lambda length: "large" if length > 10 else "small")


def get_percent_gc(df: pd.DataFrame) -> pd.Series:
    return df.dnaseq.apply(gc_percent).rename("percent_gc")


def combine_results(
    original_df: pd.DataFrame, ear_length_categories: pd.Series, percent_gc: pd.Series
) -> pd.DataFrame:
    return pd.concat(
        [original_df["id"], ear_length_categories, percent_gc], axis="columns"
    )


df = get_data(url)
earlength_categories = categorize_earlengths(df)
percent_gc = get_percent_gc(df)
individual_gc_content = combine_results(df, earlength_categories, percent_gc)
print("See results for fun:\n", individual_gc_content, "\n")

print(
    individual_gc_content.groupby("earlength").agg(
        avg_gc_percent=("percent_gc", "mean")
    )
)

individual_gc_content.to_csv("grangers_analysis.csv", index=False)
