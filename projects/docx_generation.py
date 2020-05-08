from docx import Document
from docx.text.paragraph import Paragraph
from .models import *
from .views import viewMyproject

def create_docx(request,project_id):
    project = Project.objects.get(id=project_id)
    document = Document()
    document.add_heading(project.project_title, 0)
    p = document.add_paragraph(project.description)
    print(document)
    document.save('projectDocs.docx')
    return viewMyproject(request,project_id=project_id)