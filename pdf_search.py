import sys, pathlib, fitz, os

# Getting the arguments
pdf = sys.argv[1]
search_text = sys.argv[2]

# Creating a directory for output results
output = "./output"
if not os.path.exists(output):
  os.mkdir(output)

# Parsing the PDF document
doc = fitz.open(pdf)

number_of_pages = 0

# Searching for the searched text
for page in doc:
    quads = page.search_for(search_text, quads=True)

    if len(quads) > 0:
        number_of_pages += 1

        # Highlighting the results and saving as image
        page.add_highlight_annot(quads)
        pix = page.get_pixmap(dpi=300)
        pix.save("%s/page-%i.png" % (output, page.number))

print("Found %i pages in '%s' which contain '%s'" % (number_of_pages, pdf, search_text))