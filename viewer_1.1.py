#Any problem,please contact Kris, dqdrwdrw@126.com
import os
import gradio as gr
from PIL import Image
print(gr.__version__)
j=0
text=str()
o0=str()
the_path_txt=str()

def write_to_file_head(folder_path,filename, content):
    """
    将内容写入到文件头部
    :param filename: 文件名，不存在会创建
    :param content: 写入的内容
    :return:
    """
    # 如果不存在，会报错：IOError: [Errno 2] No such file or directory
    if os.path.exists(os.path.join(folder_path, filename,)):
        #print(os.path.dirname(filename))
        with open(os.path.join(folder_path, filename,),"r+") as f:
            f.seek(0)
            old = f.read()
 
            f.seek(0)
            f.write(content+old)

            #f.write(old)
            f.close()
    else:
        with open(os.path.join(folder_path, filename,), "w") as f:
            f.write(content)
            f.close()

def txt_plus(folder_path,img_suffix,txt_suffix,o99):
    #filelist = os.listdir(path)
    if img_suffix == '':
        img_suffix = '.png'
    img_suffix = img_suffix.split(',')
    png_files = []

    for suffixpict in img_suffix:
        png_files = [f for f in os.listdir(folder_path) if f.endswith(suffixpict)]
    if txt_suffix == '':
        txt_suffix='.txt'
    txt_suffix = txt_suffix.split(',')
    txt_files = []

    for suffixtxt in txt_suffix:
        txt_files = [f for f in os.listdir(folder_path) if f.endswith(suffixtxt)]
    
    for txttext in txt_files:
#       # print(file)
#         a =txttext.split('.')[0]
#       # print(a)
#         file_txt =  a + '.txt'
#       #print(file_txt)
      
        write_to_file_head(folder_path,txttext, o99)
        #file1 = open(os.path.join(folder_path, file_txt),'a').close()#folder_path +file_txt

def img_generate_txt(folder_path,img_suffix,txt_suffix):
    #filelist = os.listdir(path)
    if img_suffix == '':
        img_suffix = '.png'
    img_suffix = img_suffix.split(',')
    png_files = []

    for suffixpict in img_suffix:
        png_files = [f for f in os.listdir(folder_path) if f.endswith(suffixpict)]
    if txt_suffix == '':
        txt_suffix='.txt'
    txt_suffix = txt_suffix.split(',')
    txt_files = []

    for suffixtxt in txt_suffix:
        txt_files = [f for f in os.listdir(folder_path) if f.endswith(suffixtxt)]
    
    for pngimg in png_files:
        # print(file)
        a = pngimg.split('.')[0]
        # print(a)
        file_txt =  a + '.txt'
        #print(file_txt)

        file1 = open(os.path.join(folder_path, file_txt),'a').close()#folder_path +file_txt

def show_images(folder_path,img_suffix,txt_suffix):
#     count=0
#     for txt in os.listdir(folder_path): 
#         count = count+1
    # 获取目标文件夹中所有的PNG和TXT文件
    # input = 'png, jpg'
    if img_suffix == '':
        img_suffix = '.png'
    img_suffix = img_suffix.split(',')
    png_files = []

    for suffixpict in img_suffix:
        png_files = [f for f in os.listdir(folder_path) if f.endswith(suffixpict)]
    if txt_suffix == '':
        txt_suffix='.txt'
    txt_suffix = txt_suffix.split(',')
    txt_files = []

    for suffixtxt in txt_suffix:
        txt_files = [f for f in os.listdir(folder_path) if f.endswith(suffixtxt)]
#     png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
#     txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    # 按照文件名排序
    png_files.sort()
    txt_files.sort()
    global num
    num=0
    # 遍历文件并展示
    for i, (png_file, txt_file) in enumerate(zip(png_files, txt_files)):
    #for png_file, txt_file in zip(png_files, txt_files):
        num += 1
    #print(num)
    for i, (png_file, txt_file) in enumerate(zip(png_files, txt_files)):
        if i==j:
            # 打开PNG文件并展示
            image = Image.open(os.path.join(folder_path, png_file))
            #image.show()

            # 打开TXT文件并展示内容
            with open(os.path.join(folder_path, txt_file), 'r',errors = 'ignore') as f:
                text = f.read()
                f.close()
                #print(text)
            the_path=os.path.join(os.getcwd(),folder_path,png_file)
            global the_path_txt
            the_path_txt=os.path.join(os.getcwd(),folder_path,txt_file)
            o0=str(j+1)+"/"+str(num)

            return o0,the_path,image,text
def jminus(folder_path,img_suffix,txt_suffix):
    #上一页
    global j
    j=j-1
    if j<0:
        j=num-1
    return show_images(folder_path,img_suffix,txt_suffix)
def jplus(folder_path,img_suffix,txt_suffix):
    #下一页
    global j
    j=j+1
    if j>num-1:
        j=0
    return show_images(folder_path,img_suffix,txt_suffix)
def save_txt(o3):
    with open(the_path_txt, 'w') as f:
        f.write(o3)
        f.close()
# # 创建Gradio界面
# iface = gr.Interface(fn=show_images, inputs=["text"], outputs=["text","image","text",])#,gr.Number(label="lalu")
if __name__ == "__main__":
    with gr.Blocks() as iface:#live False
        with gr.Row():
            folder_path=gr.Textbox(label="Folder_path")
            button0=gr.Button(value="View")
            botton1=gr.Button(value="👈")
            botton2=gr.Button(value="👉")
            button9=gr.Button(value="Genenrate_txt")
        with gr.Row():
            with gr.Column():
                o2=gr.Image()
                o99=gr.Textbox(label="Top_txt")
            with gr.Column():
                o0=gr.Textbox(label="Order/Total")
                o1=gr.Textbox(label="png_path")
                o3=gr.Textbox(lines=3,interactive=True)
                botton3=gr.Button(value="Save")
        with gr.Row():
            button99=gr.Button(value="txt_plus_to_top")
            img_suffix=gr.Textbox(label="Pict_suffixs,example:.png,.jpg default:.png")
            txt_suffix=gr.Textbox(label="Text_suffixs,example:.txt,.txt1 default:.txt")
        button0.click(fn=show_images,inputs=[folder_path,img_suffix,txt_suffix],outputs=[o0,o1,o2,o3])
        botton1.click(fn=jminus, inputs=[folder_path,img_suffix,txt_suffix], outputs=[o0,o1,o2,o3])
        botton2.click(fn=jplus, inputs=[folder_path,img_suffix,txt_suffix], outputs=[o0,o1,o2,o3])
        botton3.click(fn=save_txt, inputs=o3, outputs=None)
        button9.click(fn=img_generate_txt,inputs=[folder_path,img_suffix,txt_suffix],outputs=None)
        button99.click(fn=txt_plus,inputs=[folder_path,img_suffix,txt_suffix,o99],outputs=None)
    iface.launch()