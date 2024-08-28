from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_folder, output_folder, watermark_text):
    # 判断输出文件夹是否存在，不存创建一个
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历文件夹文件
    for filename in os.listdir(input_folder):
        # 如果是图片格式
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path).convert("RGBA")

            # 创建相同大小的透明图层
            txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
            # 创建Draw对象
            d = ImageDraw.Draw(txt)
            print(d)
            
            # 设置字体格式及大小
            font = ImageFont.truetype("simhei.ttf", 50)
            
            # 获取文本宽高
            text_bbox = d.textbbox((0, 0), watermark_text, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            
            # 设置水印的位置及颜色
            position = (image.width - text_width - 10, image.height - text_height - 10)
            d.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)

            # 合并图层
            watermarked = Image.alpha_composite(image, txt)

            # 转化为RGB模式，并保存到输出文件夹
            output_image_path = os.path.join(output_folder, filename)
            watermarked.convert("RGB").save(output_image_path, "PNG")

            print(f"水印添加成功: {output_image_path}")
            

# 批量添加水印
add_watermark(".\input", ".\out", "Test水印")