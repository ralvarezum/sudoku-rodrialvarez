FROM python:3

RUN git clone https://github.com/ralvarezum/sudoku-rodrialvarez
WORKDIR /sudoku-rodrialvarez

RUN pip install -r requirements.txt

CMD [ "python3", "test_final.py" ] && [ "python3", "Interfaz_Sudoku.py" ]