from google import genai
from google.genai import types
import os

def process_image(filename):
    """
    处理PNG图片文档并提取文本内容
    
    参数:
        filename: 要处理的PNG文件名
    
    返回:
        str: 提取的文本内容
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt1 = """Please help me extract all the text content from this English document and output it in a reasonable format. You can think for a while longer, but don't miss any content or format.
The layout of the document may be normal or multi-column. You need to make a judgment based on logic.
You should ignore all the pictures and the engineering drawings composed of messy lines, and only focus on the English text.
For tables or other content in non-ordinary text formats, you need to maintain the original format as much as possible.
The output text must be the original text of the document, without any modification, and organized in the original format of the document.
Each piece of text usually has a title, such as Design Criteria, Design loads, Deck load, Live load, Vertical load, Stack load, Vehicle load, Berthing load Mooring load, Vertical load, etc. These will be the important information that you need to pay attention to."""

    with open(filename, 'rb') as f:
          image_bytes = f.read()

    response1 = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=[
          types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
          ),
          prompt1],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=32768),
            max_output_tokens=65536,
        )
      )

    # 获取文件名（不包含路径和扩展名）
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    
    # 确保输出目录存在
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    md_dir = os.path.join(project_root, 'static', 'md')
    if not os.path.exists(md_dir):
        os.makedirs(md_dir)
    
    # 写入文本到MD文件
    output_path = os.path.join(md_dir, f'{base_filename}.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(response1.text)
    
    print(f"文本提取完成，已保存到: {output_path}")
    return response1.text
