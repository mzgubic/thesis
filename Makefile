
DOCUMENT="Hmumu"

all:
	pdflatex ${DOCUMENT}.tex;
	#bibtex ${DOCUMENT};
	#pdflatex ${DOCUMENT}.tex;
	#pdflatex ${DOCUMENT}.tex;


clean:
	rm *.aux *.dvi *.log *.out *.blg *.bbl

