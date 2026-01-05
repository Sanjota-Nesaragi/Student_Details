FROM python:3.13.3
WORKDIR / docker_grade
COPY . .
CMD ["python", "grade.py"]