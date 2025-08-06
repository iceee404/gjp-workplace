import fitz  # PyMuPDF
import os

def convert_pdf_to_images(pdf_filename, pdf_dir_prefix=None, output_dir=None, dpi=600):
    """
    将PDF文件的每一页转换为PNG图片
    
    Args:
        pdf_filename: PDF文件名
        pdf_dir_prefix: PDF文件目录前缀，默认为项目根目录下的static/pdf/
        output_dir: 输出目录前缀，默认为项目根目录下的static/img/
        dpi: 输出图片的DPI（分辨率）
    
    输出文件命名格式: filename_page_1.png, filename_page_2.png...
    """
    # 设置默认路径
    if pdf_dir_prefix is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        pdf_dir_prefix = os.path.join(project_root, "static", "pdf")
    
    if output_dir is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        output_dir = os.path.join(project_root, "static", "img")
    
    # 构建完整的PDF文件路径
    pdf_path = os.path.join(pdf_dir_prefix, pdf_filename)
    
    # 获取文件名（不包含扩展名）
    base_filename = os.path.splitext(pdf_filename)[0]
    
    # 构建输出目录路径
    final_output_dir = os.path.join(output_dir, f"{base_filename}_images")
    # 确保输出目录存在
    if not os.path.exists(final_output_dir):
        os.makedirs(final_output_dir)
    
    # 检查PDF文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误: 找不到PDF文件 '{pdf_path}'")
        return False
    
    # 打开PDF文件
    try:
        doc = fitz.open(pdf_path)
        print(f"成功打开PDF文件: {pdf_path}")
        print(f"PDF总页数: {len(doc)}")
        print(f"输出分辨率: {dpi} DPI")
    except Exception as e:
        print(f"打开PDF文件失败: {e}")
        return False
    
    # 设置缩放矩阵以提高分辨率
    zoom = dpi / 72.0  # 72 DPI是PDF的默认分辨率
    mat = fitz.Matrix(zoom, zoom)
    
    # 转换每一页
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # 获取页面尺寸
        rect = page.rect
        page_width = rect.width
        page_height = rect.height
        print(f"\n处理页面 {page_num + 1}:")
        print(f"  原始尺寸: {page_width:.1f} x {page_height:.1f} 点")
        
        # 渲染整页为图像
        pix = page.get_pixmap(matrix=mat)
        
        # 生成文件名: filename_page_数字.png
        filename = f"{base_filename}_page_{page_num + 1}.png"
        filepath = os.path.join(final_output_dir, filename)
        
        # 保存图片
        pix.save(filepath)
        print(f"  已保存: {filename}")
        print(f"  输出尺寸: {pix.width} x {pix.height} 像素")
        print(f"  文件大小: {os.path.getsize(filepath) / 1024 / 1024:.2f} MB")
        
        # 释放pixmap内存
        pix = None
    
    # 保存页数信息
    total_pages = len(doc)
    
    # 关闭文档
    doc.close()
    print(f"\n转换完成！")
    print(f"共转换 {total_pages} 页，PNG图片保存在 '{final_output_dir}' 目录中")
    print(f"所有图片分辨率: {dpi} DPI (高质量)")
    return True

def main():
    """测试函数"""
    # 测试PDF文件名
    test_pdf = "Example Drawing Package 1A.pdf"
    
    # 执行转换操作
    print("开始将PDF每页转换为PNG图片...")
    print("=" * 50)
    success = convert_pdf_to_images(
        pdf_filename=test_pdf,
        dpi=600  # 高分辨率600 DPI
    )
    print("=" * 50)
    
    if success:
        print("转换成功完成！")
    else:
        print("转换失败，请检查文件路径和权限。")

if __name__ == "__main__":
    main() 