import numpy as np
import seaborn.objects as so
import polars as pl


def summary_statistics(df, x):
    summary_stats = df[x].describe()
    return summary_stats


def log_func(df, x):
    if x[0:3] == "log" or x[0:3] == "Log":
        # Update the DataFrame using with_columns
        df = df.with_columns(pl.Series(np.log(df[x[4:]].to_numpy())).alias(x))

    elif x[0:2] == "ln" or x[0:2] == "Ln":
        df = df.with_columns(pl.Series(np.log(df[x[3:]].to_numpy())).alias(x))

    return df


def scatter_plot(df, x, y, title, plot="plot.png"):
    df = df.to_pandas()
    my_chart = (
        so.Plot(
            df,
            x=x,
            y=y,
        )
        .add(so.Line(), so.PolyFit(order=2))
        .add(so.Dot())
        .label(title=title)
    )
    try:
        if "ipykernel" in str(type(get_ipython())):
            my_chart.show()
    except NameError:
        pass
    return my_chart.save("images/" + plot)


# def table_format(text):
#     """format to md pandas describe function"""
#     table = "| Statistics | Value |\n| ----- | ----- |\n"
#     for i in text.split(" "):
#         for j in i.split("\n"):
#             if j == "Name:":
#                 return table
#             elif j == "":
#                 pass
#             elif j[0].isdigit() and j[-1].isdigit():
#                 digit = float(j)
#                 table += f"{digit:.2f} |\n"

#             else:
#                 table += f"| {j} | "


def generate_general_markdown(df, x, y):
    """generate an md file with outputs"""
    markdown_table1 = summary_statistics(df, x)
    markdown_table2 = summary_statistics(df, y)
    markdown_table1 = str(markdown_table1)
    markdown_table2 = str(markdown_table2)

    # Write the markdown table to a file
    with open("Data_summary.md", "w", encoding="utf-8") as file:
        file.write(f"### Describe {x}:\n")
        file.write(f"{markdown_table1}")
        file.write("\n\n")  # Add a new line
        file.write(f"### Describe {y}:\n")
        file.write(markdown_table2)
        file.write("\n\n")  # Add a new line
        file.write("![scatter_plot](images/plot.png)\n")
