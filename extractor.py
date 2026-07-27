import os
import zipfile
import tarfile

class CapyExtractor:
    def __init__(self):
        pass

    def extract_archive(self, file_path, dest_dir):
        """📦 智慧辨識主流壓縮格式，以低記憶體串流方式解壓縮"""
        if not os.path.exists(file_path):
            print(f"錯誤：找不到檔案 {file_path}")
            return False

        os.makedirs(dest_dir, exist_ok=True)
        
        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zf:
                zf.extractall(dest_dir)
            print("【完成】ZIP 解壓成功，記憶體保持極低！")
            return True
        elif file_path.endswith(('.tar.gz', '.tgz', '.tar.bz2', '.tar.xz', '.tar')):
            with tarfile.open(file_path, 'r:*') as tar:
                tar.extractall(path=dest_dir, set_attrs=False)
            print("【完成】TAR 系列解壓成功！")
            return True
        else:
            print("【錯誤】不支援的壓縮格式！")
            return False