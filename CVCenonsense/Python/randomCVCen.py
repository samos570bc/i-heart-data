#!/usr/bin/env python3

import random

# Number of worksheets
copies = 20

# Read template and word files
with open ("../Template/template.tex", "r") as myfile:
    template=myfile.readlines()
with open ("../Data/short_a.txt", "r") as myfile:
    shorta=myfile.readlines()
with open ("../Data/short_i.txt", "r") as myfile:
    shorti=myfile.readlines()
with open ("../Data/short_o.txt", "r") as myfile:
    shorto=myfile.readlines()
with open ("../Data/short_u.txt", "r") as myfile:
    shortu=myfile.readlines()


# Save a copy of the blank worksheet template

blank_start = template.index("% Worksheet Start\n")
blank_end = template.index("% Worksheet End\n")
blank = template[blank_start:blank_end]

# Create worksheets
for copy in range(copies):

    # Add page number
    i = template.index("CVCe-N PPP \\hfill Student Copy\n")
    template[i] = template[i].replace("PPP", str(copies-copy), 1)
    j = template.index("CVCe-N PPP \\hfill Teacher Copy\n")
    template[j] = template[j].replace("PPP", str(copies-copy), 1)

    # Choose random words
    words = []
    words += random.sample(shorta, 6)
    words += random.sample(shorti, 6)
    words += random.sample(shorto, 6)
    words += random.sample(shortu, 2)
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


