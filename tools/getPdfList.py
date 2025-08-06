import os

def get_pdf_files(directory_path):
    """
    获取指定目录下所有PDF文件的文件名
    
    参数:
        directory_path: 目录路径
    
    返回:
        list: PDF文件名列表（只包含文件名，不包含路径）
    """
    pdf_files = []
    
    try:
        # 检查目录是否存在
        if not os.path.exists(directory_path):
            print(f"错误: 目录 '{directory_path}' 不存在")
            return pdf_files
        
        # 遍历目录中的所有文件
        for filename in os.listdir(directory_path):
            # 检查文件扩展名是否为.pdf
            if filename.lower().endswith('.pdf'):
                pdf_files.append(filename)
        
        print(f"在目录 '{directory_path}' 中找到 {len(pdf_files)} 个PDF文件")
        return pdf_files
        
    except Exception as e:
        print(f"读取目录时发生错误: {e}")
        return pdf_files
