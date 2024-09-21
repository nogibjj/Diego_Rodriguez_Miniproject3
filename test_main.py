import os


def test_main():
    "Checking files"
    assert os.path.isfile("images/plot.png")
    assert os.path.isfile("Data_summary.md")


if __name__ == "__main__":
    test_main()
