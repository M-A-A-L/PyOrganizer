import fileOrganizer

folder = input("Digite o diretório que deseja organizar: ")
if fileOrganizer.is_valid_folder(folder):
    fileOrganizer.organize_folder(folder)
    print("Diretório organizado")
else:
    print("ERRO: Diretório inválido!")