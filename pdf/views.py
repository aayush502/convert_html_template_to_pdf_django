from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import CreateView
import datetime
import pdb
from pdf.models import Student
from pdf_convert.settings import BASE_DIR, MEDIA_ROOT, MEDIA_URL
from .forms import StudentForm
import pdfkit

from pdf_convert.utils import render_to_pdf


class GeneratePdf(View):
    def get(self, request,*args, **kwargs):
        pdf = render_to_pdf('pdf.html')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("1")
            # content = "filename='%s'" %(filename)
            # download = request.GET.get('download')
            # if download:
            content = "attachment; filename='%s'" %(filename)                  
            response['Content-Disposition'] = content
            return response
        return HttpResponse("No pdf")
class TemplateView(View):
    def get(self, request):
        return render(request, template_name="pdf/invoice.html")

class HomeView(View):
    def get(self, request):
        return render(request, template_name="index.html")

class DownloadView(View):
    def get(self, request):
        return render(request, template_name="pdf/link.html")

class StudentView(View):
    # model = Student
    # fields = ['name', 'roll_no','address']
    # template_name = "student/student.html"
    def get(self, request):
        return render(request, template_name="student/student.html")

    def post(self, request,*args, **kwargs):
        student_name = request.POST.get('name')
        roll_no = request.POST.get('roll')
        address = request.POST.get('address')
        reg = Student.objects.create(name=student_name, roll_no = roll_no, address=address)
        pdfkit.from_url(f'127.0.0.1:8000/student/{reg.id}', f'{BASE_DIR}/static/media/{reg.name}_{reg.id}.pdf')
        # data = {
        #     'name' : student_name,
        #     'roll_no': roll_no,
        #     'address': address,
        # }
            # return render(request, template_name=" ", context={'data':data})
        return redirect(f'student/{reg.id}')
        # return GeneratePdf.as_view()(self.request)


# def pdf_download():
#     pdfkit.from_url('localhost:8000/student', 'out.pdf')

class DetaiView(View):
    def get(self,request, id):
        student = Student.objects.get(id=id)
        return render(request, template_name="pdf.html", context={'data':student})
        

class InsuranceView(View):
    def get(self, request):
        return render(request, template_name="student/certificate.html")