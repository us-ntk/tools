import os

def create_structure_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            path = line.strip()
            if path.endswith('/'):
                # ディレクトリを作成
                os.makedirs(path, exist_ok=True)
            else:
                # ファイルを作成
                dir_path = os.path.dirname(path)
                if dir_path:
                    os.makedirs(dir_path, exist_ok=True)
                with open(path, 'w') as f:
                    pass

if __name__ == "__main__":
    structure_file = 'structure.txt'
    create_structure_from_file(structure_file)
    print("ディレクトリ構造とファイルが作成されました。")