from docx import Document
from docx.text.paragraph import Paragraph
from .models import *
from django.shortcuts import render, redirect
import xml.etree.ElementTree
from .views import *

def create_docx(request,project_id):
    indexhead = "Generate Project Document"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        document = Document()
        document.add_heading(project.project_title, 0)
        p = document.add_paragraph(project.description.join(xml.etree.ElementTree.fromstring(project.description).itertext()))
        
        path =r'/docs' + project.project_title+'.docx'
        document.save(path)
        notification(request)
        create_document = GeneratedDocs.objects.create(
            project=project,docx=project.project_title+'.docx'
        )
        create_document.save()
        
    docs = enumerate(GeneratedDocs.objects.filter(project=project).order_by('-id'), start=1)
    
    return render(request,'projects/my_projects/generate_docs.html',{
        'project':project,
        'project_id':project.id,
        'notification':notification,
        'indexhead':indexhead,
        'hidesearch':hidesearch,
        'docs':docs,
        'member':member
    })