# 应用程序部分
import tkinter as tk
from tkinter import ttk,messagebox
# 操作水印部分
from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark():
    # 如果未填写默认为out文件夹，不存在时进行创建
    output = input2.get("1.0","end").strip()
    if output == "":
        output=".\out"
    if not os.path.exists(output):
        os.makedirs(output)
    
    input = input1.get("1.0","end").strip()
    if input == "":
        messagebox.showinfo("错误提示","输入文件夹的路径不能为空")
        return
    # 遍历文件夹文件
    for filename in os.listdir(input):
        # 如果是图片格式
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input, filename)
            image = Image.open(image_path).convert("RGBA")

            # 创建相同大小的透明图层
            txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
            # 创建Draw对象
            d = ImageDraw.Draw(txt)
            print(d)
            
            # 设置字体格式及大小
            font = ImageFont.truetype("simhei.ttf", 50)
            
            # 获取文本宽高
            watermark = input3.get("1.0","end").strip()
            if(watermark==""):
                messagebox.showinfo("错误提示","水印文字不能为空")
                return
            text_bbox = d.textbbox((0, 0), watermark, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            
            # 设置水印的位置及颜色
            position = (image.width - text_width - 10, image.height - text_height - 10)
            d.text(position, watermark, fill=(255, 255, 255, 128), font=font)

            # 合并图层
            watermarked = Image.alpha_composite(image, txt)

            # 转化为RGB模式，并保存到输出文件夹
            output_image_path = os.path.join(output, filename)
            watermarked.convert("RGB").save(output_image_path, "PNG")

            print(f"水印添加成功: {output_image_path}")
            

# 创建主窗口
root = tk.Tk()
root.title("图片批量水印")
root.geometry("400x200")

# 输入文件夹部分
label = tk.Label(root, text="请输入要加水印图片的文件夹")
label.pack()
input1 = tk.Text(root, height=2)
input1.pack()

# 输出文件夹部分()
label = tk.Label(root, text="请输入输出图片的文件夹(不填写默认out文件夹)")
label.pack()
input2 = tk.Text(root, height=2)
input2.pack()

# 输入水印部分
label = tk.Label(root,text="请输入水印文字")
label.pack()
input3 = tk.Text(root,height=2)
input3.pack()

# 确然按钮
button = ttk.Button(root, text="插入水印", command=add_watermark)
button.pack(side=tk.BOTTOM)

root.mainloop()