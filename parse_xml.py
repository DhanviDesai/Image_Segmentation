import xml.etree.ElementTree as ET
import cv2

def parseXML(file_name):
   tree = ET.ElementTree(file=file_name)
   root = tree.getroot()

   image = cv2.imread(".\\images\\page_3.jpg")

   page = root[0]
   page_width = int(page.get('width'))
   page_height = int(page.get('height'))
   scaling_factor = (image.shape[0]+image.shape[1])/(page_width+page_height)
   x = int(page.get('top'))
   y = int(page.get('left'))
   width = int(int(page.get('width'))*scaling_factor)
   height = int(int(page.get('height'))*scaling_factor)
   cv2.rectangle(image,(x,y),(x+width,y+height),(0,255,0),2)
   cv2.imwrite("editedPage2.jpg",image)

   text_list = page.findall('text')

   for i,text in enumerate(text_list):
       x = int(int(text.get('left'))*scaling_factor)
       y = int(int(text.get('top'))*scaling_factor)
       width = int(int(text.get('width'))*scaling_factor)
       height = int(int(text.get('height'))*scaling_factor)
       if(len(text)>0):
           for j,child in enumerate(text):
               text1 = child.text.strip()
               if(text1=="" or None):
                   continue
               if(not(j==0) and not(j==len(text)-1)):
                   if(text[j-1].get('height')>child.get('height') and child.get('height')<text[j+1].get('height')):
                       cv2.rectangle(image,(x,y),(x+width,y+height),(0,0,255),2)
               else:
                   print(text1)
                   cv2.rectangle(image,(x,y),(x+width,y+height),(255,0,0),2)
               cv2.imwrite("editedPage2.jpg",image)
       else:
           print_text = text.text.strip()
           if(print_text == "" or None):
               continue
           if(not(i==0) and not(i==len(text_list)-1)):
               if(text_list[i-1].get('height')>text.get('height') and text.get('height')<text_list[i+1].get('height')):
                   cv2.rectangle(image,(x,y),(x+width,y+height),(0,0,255),2)
               else:
                   print(print_text)
                   cv2.rectangle(image,(x,y),(x+width,y+height),(255,0,0),2)
           cv2.imwrite("editedPage2.jpg",image)

if __name__ == "__main__":
   parseXML(".\\PyPdf\\document.xml")
