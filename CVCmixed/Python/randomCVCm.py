#!/usr/bin/env python3

import random

# Number of worksheets
copies = 20

# Read template and word files
with open ("../Template/template.tex", "r") as myfile:
    template=myfile.readlines()
with open ("../Data/short_a_w.txt", "r") as myfile:
    shortaw=myfile.readlines()
with open ("../Data/short_e_w.txt", "r") as myfile:
    shortew=myfile.readlines()
with open ("../Data/short_i_w.txt", "r") as myfile:
    shortiw=myfile.readlines()
with open ("../Data/short_o_w.txt", "r") as myfile:
    shortow=myfile.readlines()
with open ("../Data/short_u_w.txt", "r") as myfile:
    shortuw=myfile.readlines()
with open ("../Data/short_a_n.txt", "r") as myfile:
    shortan=myfile.readlines()
with open ("../Data/short_e_n.txt", "r") as myfile:
    shorten=myfile.readlines()
with open ("../Data/short_i_n.txt", "r") as myfile:
    shortin=myfile.readlines()
with open ("../Data/short_o_n.txt", "r") as myfile:
    shorton=myfile.readlines()
with open ("../Data/short_u_n.txt", "r") as myfile:
    shortun=myfile.readlines()


# Save a copy of the blank worksheet template

blank_start = template.index("% Worksheet Start\n")
blank_end = template.index("% Worksheet End\n")
blank = template[blank_start:blank_end]

# Create worksheets
for copy in range(copies):

    # Add page number
    i = template.index("CVC-M PPP \\hfill Student Copy\n")
    template[i] = template[i].replace("PPP", str(copies-copy), 1)
    j = template.index("CVC-M PPP \\hfill Teacher Copy\n")
    template[j] = template[j].replace("PPP", str(copies-copy), 1)

    # Choose random words
    words = []
    words += random.sample(shortaw, 2)
    words += random.sample(shortew, 2)
    words += random.sample(shortiw, 2)
    words += random.sample(shortow, 2)
    words += random.sample(shortuw, 2)
    words += random.sample(shortan, 2)
    words += random.sample(shorten, 2)
    words += random.sample(shortin, 2)
    words += random.sample(shorton, 2)
    words += random.sample(shortun, 2)
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


