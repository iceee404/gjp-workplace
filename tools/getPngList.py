import os

def get_png_files(filename):
    """
    获取指定文件名对应目录下所有PNG文件的相对路径
    
    参数:
        filename: 文件名（不含扩展名）
    
    返回:
        list: PNG文件的相对路径数组（从img目录开始的路径）
    """
    png_files = []
    
    try:
        # 构建目标目录路径
        # 从tools目录运行时，需要定位到项目根目录下的static/img目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        img_base_dir = os.path.join(project_root, "static", "img")
        
        # 构建具体的目录名（文件名_images）
        target_dir_name = f"{filename}_images"
        target_dir_path = os.path.join(img_base_dir, target_dir_name)
        
        # 检查目录是否存在
        if not os.path.exists(target_dir_path):
            print(f"错误: 目录 '{target_dir_path}' 不存在")
            return png_files
        
        # 遍历目录中的所有文件
        for file in os.listdir(target_dir_path):
            # 检查文件扩展名是否为.png
            if file.lower().endswith('.png'):
                # 返回从img目录开始的相对路径
                relative_path = os.path.join(target_dir_name, file)
                png_files.append(relative_path)
        
        # 按文件名排序，确保顺序一致
        png_files.sort()
        
        print(f"在目录 '{target_dir_name}' 中找到 {len(png_files)} 个PNG文件")
        return png_files
        
    except Exception as e:
        print(f"读取目录时发生错误: {e}")
        return png_files

def main():
    """测试函数"""
    # 测试获取PNG文件列表
    test_filename = "Example Drawing Package 1A"
    png_list = get_png_files(test_filename)
    
    if png_list:
        print("找到的PNG文件:")
        for png_file in png_list:
            print(f"  - {png_file}")
    else:
        print("未找到任何PNG文件")

if __name__ == "__main__":
    main()
