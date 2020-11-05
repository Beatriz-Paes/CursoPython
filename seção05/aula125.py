# OS + SHUTIL - Mover, copiar e apagar arquivos
import os
import shutil

caminho_de_origem = '/home/beah/Imagens'
caminho_de_novo = '/home/beah/Imagens2'

try:
    os.mkdir(caminho_de_novo)
except FileExistsError as e:
    print(f'O diretório {caminho_de_novo} já existe.')

# for root, dirs, files in os.walk(caminho_de_origem):
#     for file in files:
#         old_file_path = os.path.join(root, file)
#         new_file_path = os.path.join(caminho_de_novo, file)
        # print(new_file_path)

        # shutil.move(old_file_path, new_file_path)
        # print(f'Arquivo {file} movido com sucesso.')

        # if '.jpeg' in file:
        #     shutil.copy(old_file_path, new_file_path)
        #     print(f'Arquivo {file} copiado com sucesso.')

for root, dirs, files in os.walk(caminho_de_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_de_novo, file)

        os.remove(new_file_path)
