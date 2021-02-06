from django.db import models
import os
import os.path
from os.path import splitext

# Create your models here.

class Document (models.Model):
  title = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)
  doc = models.FileField(upload_to='Media')

  def __str__ (self):
    return self.title

  def delete(self, *args, **kwargs):
    self.doc.delete()
    super().delete(*args, **kwargs)  
  
  def extension(self):
    # extension = os.path.splitext(file_path)[1]
    file = self.doc
    if file:
      filename = file.name
      print (filename)
      if filename.endswith('.jpg'):
        extension = 'JPEG'
      elif filename.endswith('.pdf'):
        extension = 'PDF'
      elif filename.endswith('.docx') or filename.endswith('.doc') or filename.endswith('.docm'):
        extension = 'DOC'
      elif filename.endswith('.ppt') or filename.endswith('.pptx'):
        extension = 'PowerPoint'
      else:
        extension = 'file'
    return extension

  # def clean(self):
  #       cleaned_data = super(, self).clean()
  #       file = cleaned_data.get('file')

  #       if file:
  #           filename = file.name
  #           print (filename)
  #           if filename.endswith('.mp3'):
  #               print ('File is a mp3')
  #           else:
  #               print ('File is NOT a mp3')
  #               raise forms.ValidationError("File is not a mp3. Please upload only mp3 files")

  #       return file


