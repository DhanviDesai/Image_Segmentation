import xml.etree.ElementTree as ET
import cv2

def get_element_tree_root(file_name):
    tree = ET.ElementTree(file=file_name)
    root = tree.getroot()
    return root

def get_image(page_number):
    image = cv2.imread(".\\images\\page_1"+str(page_number)+".jpg")
    return image

def draw_outlines(scaling_factor,text_bound,image,color_point):
    x = int(int(text_bound.get('left'))*scaling_factor)
    y = int(int(text_bound.get('top'))*scaling_factor)
    width = int(int(text_bound.get('width'))*scaling_factor)
    height = int(int(text_bound.get('height'))*scaling_factor)
    cv2.rectangle(image,(x,y),(x+width,y+height),color_point,1)

def save_image(image,page_number):
    cv2.imwrite(".\\output_folder\\editedPage_"+str(page_number)+".jpg")

def get_color_point(j,holding_list):
    if(j==0):
        if(holding_list[j].get('height') < holding_list[j+1].get('height')):
            return False,(0,0,255)
        else:
            return True,(255,0,0)
    elif(j==len(holding_list)-1):
        if(holding_list[j-1].get('height') > holding_list[j].get('height')):
            return False,(0,0,255)
        else:
            return True,(255,0,0)
    else:
        if(holding_list[j-1].get('height') > holding_list[j].get('height') and holding_list[j].get('height') < holding_list[j+1].get('height')):
            return False,(0,0,255)
        else:
            return True,(255,0,0)

root = get_element_tree_root(".\\PyPdf\\document - Copy.xml")
# tree = ET.ElementTree(".\\PyPdf\\document - Copy.xml")
# root = tree.getroot()
for i,page in enumerate(root.findall('page')):
    page_width = int(page.get('width'))
    page_height = int(page.get('height'))
    page_number = int(page.get('number'))
    image = get_image(page_number)
    image_width = image.shape[0]
    image_height = image.shape[1]
    scaling_factor = (image_width+image_height)/(page_width+page_height)
    draw_outlines(scaling_factor,page,image,(0,255,0))
    text_list = page.findall('text')
    for i,text_child in enumerate(text_list):
        this_text = text_child.text.strip()
        if(this_text==None):
            if(len(text_child)>0):
                for j,inner_child in enumerate(text_child):
                    inner_this_text = inner_child.text.strip()
                    if(inner_this_text == ""):
                        continue
                    status,color_point = get_color_point(j,text_child)
                    draw_outlines(scaling_factor,inner_child,image,color_point)
                    if(status):
                        print(inner_this_text)
        else:
            status,color_point = get_color_point(i,text_list)
            draw_outlines(scaling_factor,text_child,image,color_point)
            if(status):
                print(this_text)
    save_image(image,page_number)
