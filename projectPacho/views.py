from django.http import HttpResponse
from django.template import Context, Template 




def mi_template(request):
    
    cargar_archivo = open(r'D:\Users\pacho\Desktop\py\PROYECTO FINAL\templates\template.html', 'r')
    
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
        
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)
