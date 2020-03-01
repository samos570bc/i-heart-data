#!/usr/bin/env python3

import random

# Number of worksheets
copies = 20

# Read template and word files
with open ("../Template/template.tex", "r") as myfile:
    template=myfile.readlines()
with open ("../Data/r_blends_w.txt", "r") as myfile:
    blendrw=myfile.readlines()
with open ("../Data/s_blends_w.txt", "r") as myfile:
    blendsw=myfile.readlines()
with open ("../Data/l_blends_w.txt", "r") as myfile:
    blendlw=myfile.readlines()
with open ("../Data/three_blends_w.txt", "r") as myfile:
    blendthreew=myfile.readlines()
with open ("../Data/r_blends_n.txt", "r") as myfile:
    blendrn=myfile.readlines()
with open ("../Data/s_blends_n.txt", "r") as myfile:
    blendsn=myfile.readlines()
with open ("../Data/l_blends_n.txt", "r") as myfile:
    blendln=myfile.readlines()
with open ("../Data/three_blends_n.txt", "r") as myfile:
    blendthreen=myfile.readlines()

# Save a copy of the blank worksheet template

blank_start = template.index("% Worksheet Start\n")
blank_end = template.index("% Worksheet End\n")
blank = template[blank_start:blank_end]

# Create worksheets
for copy in range(copies):

    # Add page number
    i = template.index("CCVC-M PPP \\hfill Student Copy\n")
    template[i] = template[i].replace("PPP", str(copies-copy), 1)
    j = template.index("CCVC-M PPP \\hfill Teacher Copy\n")
    template[j] = template[j].replace("PPP", str(copies-copy), 1)

    # Choose random words
    words = []
    words += random.sample(blendrw, 4)
    words += random.sample(blendsw, 3)
    words += random.sample(blendlw, 2)
    words += random.sample(blendthreew, 1)
    words += random.sample(blendrn, 4)
    words += random.sample(blendsn, 3)
    words += random.sample(blendln, 2)
    words += random.sample(blendthreen, 1)
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


