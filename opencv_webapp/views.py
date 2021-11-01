from django.shortcuts import render
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face

# from .cv_functions import cv_detect_face
# cv_detect_face()
#
# import cv_functions
# cv_functions.cv_detect_face()


# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})


def simple_upload(request):

    if request.method == 'POST':

        # print(request.POST) # dict
        # print(request.FILES) # dict
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():

            myfile = request.FILES['image'] # 유저가 업로드한 파일

            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            # myfile.name : 'ses.jpg'
            # filename : 'ses_UPArih4.jpg'

            context = {'form':form, 'uploaded_file_url':uploaded_file_url}
            return render(request, 'opencv_webapp/simple_upload.html', context)

    else: # 'GET' request
        form = SimpleUploadForm()
        return render(request, 'opencv_webapp/simple_upload.html', {'form':form})



def detect_face(request):

    if request.method == 'POST':

        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False) # ImageUploadModel's instance
            # post.description = papago.translate(post.description)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            # == form.instance.document.url
            # == post.document.url
            # == '/media/images/2021/10/29/ses_XQAftn4.jpg'

            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL)

            # print('\n\n--------------------------------\n\n')
            # print('** imageURL :', imageURL)
            # print('** + ROOT_URL :', settings.MEDIA_ROOT_URL + imageURL)
            # print()
            # print('* form.instance :', form.instance)
            # print('* form.instance.document :', form.instance.document)
            # print('* form.instance.document.name :', form.instance.document.name)
            # print('* form.instance.document.url :', form.instance.document.url)
            # print('')
            # print('* post.document :', post.document)
            # print('* post.document.url :', post.document.url)
            # print('\n\n--------------------------------\n\n')

            context = {'form':form, 'post':post}
            return render(request, 'opencv_webapp/detect_face.html', context)

    else:
        form = ImageUploadForm()

        context = {'form':form}
        return render(request, 'opencv_webapp/detect_face.html', context)







# @ models.py
# class ImageUploadModel(models.Model):
#
#     description = models.CharField(max_length=255, blank=True)
#     document = models.ImageField(upload_to='images/%Y/%m/%d')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
# @ html
# <input type='text' name='description' ~~~>
# <input type='file' name='document' ~~~>
#
# def temp(request):
#
#     request.FILES['document'] ???
#
#     new_row = ImageUploadModel(description=request.POST['description'], document=request.FILES['document'])
#     new_row.save()
