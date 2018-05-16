(TeX-add-style-hook
 "processing-activities"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "DIV14" "11pt" "DIN" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "ngerman") ("inputenc" "utf8") ("fontenc" "T1") ("xcolor" "dvipsnames") ("hyperref" "pdftitle={Verzeichnis von Verarbeitungstätigkeiten}" "pdfauthor={Generated with Django}" "pdfcreator={PDFLaTeX}" "pdfproducer={TeXlive}" "colorlinks" "hyperindex" "urlcolor=MidnightBlue" "linkcolor=MidnightBlue")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl11"
    "babel"
    "inputenc"
    "fontenc"
    "lmodern"
    "textcomp"
    "eurosym"
    "xcolor"
    "enumitem"
    "hyperref"))
 :latex)

