import big_o
from os import mkdir, path
from main import group_files_languages, generate_dir


generate_dir("tests")
data_generator = lambda n: big_o.datagen.strings(3)
print("Running Big O tests ...")
best, others = big_o.big_o(group_files_languages, data_generator)
print("Best result: ", best)
print("Full Report: ")
print(big_o.reports.big_o_report(best, others))
