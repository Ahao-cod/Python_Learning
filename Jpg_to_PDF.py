from PIL import Image

def convert_jpg_to_pdf(image_path, output_path, quality=80):
    image = Image.open(image_path)
    pdf_path = output_path + ".pdf"
    image.save(pdf_path, "PDF", quality = quality)
    print(f"成功将 {image_path} 转换为 {pdf_path}")

convert_jpg_to_pdf("E:\\pc1.jpg", "E:\\十四届蓝桥杯证书")