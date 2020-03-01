#!/usr/bin/env python3

import random

# Number of worksheets
copies = 20

# Read template and word files
with open ("../Template/template.tex", "r") as myfile:
    template=myfile.readlines()
with open ("../Data/ft_words.txt", "r") as myfile:
    words_ft=myfile.readlines()
with open ("../Data/lpd_words.txt", "r") as myfile:
    words_lpd=myfile.readlines()
with open ("../Data/lt_words.txt", "r") as myfile:
    words_lt=myfile.readlines()
with open ("../Data/mp_words.txt", "r") as myfile:
    words_mp=myfile.readlines()
with open ("../Data/nd_words.txt", "r") as myfile:
    words_nd=myfile.readlines()
with open ("../Data/nk_words.txt", "r") as myfile:
    words_nk=myfile.readlines()
with open ("../Data/nt_words.txt", "r") as myfile:
    words_nt=myfile.readlines()
with open ("../Data/sk_words.txt", "r") as myfile:
    words_sk=myfile.readlines()
with open ("../Data/sp_words.txt", "r") as myfile:
    words_sp=myfile.readlines()
with open ("../Data/st_words.txt", "r") as myfile:
    words_st=myfile.readlines()

# Save a copy of the blank worksheet template

blank_start = template.index("% Worksheet Start\n")
blank_end = template.index("% Worksheet End\n")
blank = template[blank_start:blank_end]

# Create worksheets
for copy in range(copies):

    # Add page number
    i = template.index("CVCC PPP \\hfill Student Copy\n")
    template[i] = template[i].replace("PPP", str(copies-copy), 1)
    j = template.index("CVCC PPP \\hfill Teacher Copy\n")
    template[j] = template[j].replace("PPP", str(copies-copy), 1)

    # Choose random words
    words = []
    words += random.sample(words_st, 5)
    words += random.sample(words_sk, 3)
    words += random.sample(words_sp, 1)
    words += random.sample(words_nd, 3)
    words += random.sample(words_nt, 2)
    words += random.sample(words_nk, 3)
    words += random.sample(words_mp, 2)
    words += random.sample(words_lpd, 2)
    words += random.sample(words_lt, 2)
    words += random.sample(words_ft, 2)

    random.shuffle(words)
    words = [ s[:-1] for s in words ]

    # Add chosen words to template
    for w in words:
        for line in template:
            if "AAA" in line:
                i = template.index(line)
                newline = line.replace("AAA", w.lower(), 1)
                template[i] = newline
                break

    # Duplicate student table for teacher table
    student_table_start = template.index("% Student Table\n")+1
    teacher_table_start = template.index("% Teacher Table\n")+1
    template[teacher_table_start:teacher_table_start] = template[student_table_start:student_table_start+13]

    # Prepend a blank worksheet
    if copy < copies-1:
        template[blank_start-1:blank_start-1] = ["\\newpage\n","\n"]
        template[blank_start-1:blank_start-1] = blank

# Write to file
outF = open("../Worksheet/worksheet.tex", "w")
for line in template:
    outF.write(line)
outF.close()


