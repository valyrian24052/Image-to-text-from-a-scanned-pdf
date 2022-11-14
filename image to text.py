import io
import csv

from PIL import Image
import pytesseract as tess 
import fitz

#tesseract setup
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSDATA_PREFIX = r'C:\Program Files\Tesseract-OCR'

path=r"C:\Users\Valyr\Downloads\assignment_img_vrf\label.pdf"
pdf = fitz.open(path)

r=[]

for page_index in range(len(pdf)):
    page = pdf[page_index]
    image_list=page.get_images()

    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = pdf.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        text_data = tess.image_to_string(image.convert('RGB'), lang='eng')
        array=str.split(text_data, "\n")
        lst = [x  for x in array[1:] if ('Device Name:' in x or 'LOT:' in x or 'REF' in x)]
        lst.append(array[0])
        lst[0] = lst[0][13:]
        lst[1] = lst[1][4:]
        lst[2] = lst[2][5:]
        r.append(lst)

with open('projectdata.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in r:
        writer.writerow(row)
        
        

        
        
                
        




