from docx import Document
from docx.text.paragraph import Paragraph
from .models import *
from django.shortcuts import render, redirect
import xml.etree.ElementTree
from .views import *
import os.path
from datetime import datetime

def create_docx(request,project_id):
    indexhead = "Generate Project Document"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    
    if request.method == "POST":
        document = Document()
        document.add_heading(project.project_title, 0)
        p = document.add_paragraph(''.join(xml.etree.ElementTree.fromstring(str(project.description)).itertext()))

        # Then Adding Viewpoints
        viewpoints = enumerate(Viewpoint.objects.filter(project=project), start=1)
        if Viewpoint.objects.filter(project=project).exists():
             document.add_heading(project.project_title+'` Viewpoints', level=2)
        for num, viewpoint in viewpoints:
           document.add_heading(str(num)+': ' + viewpoint.viewpoint_name, level=3)
           document.add_paragraph(''.join(xml.etree.ElementTree.fromstring(viewpoint.description).itertext()))
        # getting project goals
        
        goals = enumerate(Goal.objects.filter(project=project), start=1)
        if Goal.objects.filter(project=project).exists():
            document.add_heading(project.project_title+'` Goals', level=2)
        for num, goal in goals:
            document.add_heading(str(num)+': ' + goal.goal_name, level=3)
            document.add_paragraph('A Goal from ' + str(goal.viewpoint))
            document.add_paragraph(''.join(xml.etree.ElementTree.fromstring(goal.description).itertext()))
        # getting requirements
        
        requirements = enumerate(Requirement.objects.filter(project=project), start=1)
        if Requirement.objects.filter(project=project).exists():
            document.add_heading(project.project_title+'` Requirements', level=2)
        for num, requirement in requirements:
            document.add_heading(str(num)+': ' + requirement.name, level=3)
            document.add_paragraph('A Requirement from Goal ' + str(requirement.goal) + " of Viewpoint " +str(requirement.goal.viewpoint) )
            document.add_paragraph(''.join(xml.etree.ElementTree.fromstring(requirement.description).itertext()))
        
        # getting scenarios
       
        scenarios = enumerate(Scenario.objects.filter(project=project), start=1)
        if Scenario.objects.filter(project=project).exists():
             document.add_heading(project.project_title+'` Scenarios', level=2)
        for num, scenario in scenarios:
            document.add_heading(str(num)+': ' + scenario.name, level=3)
            document.add_paragraph('A Scenario from Requirement ' + str(scenario.requirement.goal) + " of Goal " +str(scenario.requirement.goal) + ' from Viewpoint ' +str(scenario.requirement.goal.viewpoint))
            document.add_paragraph(''.join(xml.etree.ElementTree.fromstring(scenario.description).itertext()))
        
        # getting processes
        processes = enumerate(Process.objects.filter(project=project), start=1)
        if Process.objects.filter(project=project).exists():
            document.add_heading(project.project_title+'` Processes', level=2)
        for num, process in processes:
            document.add_heading(str(num)+': ' + process.process_name, level=3)
            document.add_paragraph('A Process  from scenario'+ str(process.scenario) +  ' of  Requirement ' + str(process.scenario.requirement) + " from Goal " +str(process.scenario.requirement.goal) + ' of Viewpoint ' +str(process.scenario.requirement.goal.viewpoint))
            document.add_paragraph(''.join(xml.etree.ElementTree.fromstring(process.description).itertext()))
        now = datetime.now()
        filename = str(now)+project.project_title+'.docx'
        
        path = '/root/CORES/core/docs/'+filename
        print(path)
        
        document.save(path)
        notification(request)
        create_document = GeneratedDocs.objects.create(
            project=project,docx=filename
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

def delete_file(request,file_id):
    file = GeneratedDocs.objects.get(id=file_id)
    delete = GeneratedDocs.objects.filter(id=file_id).delete()
    return redirect('projects:generatedocs',project_id=file.project.id)