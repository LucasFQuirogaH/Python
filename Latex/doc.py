import os
import pypandoc
for root, dirs, files in os.walk('./'):
    for name in files:
        if name[-3:] == '.md':
            name_tex = str(name[:-3]+'.tex')
            try:
                pypandoc.convert_file(os.path.join(root, name), 'latex', format='markdown', \
                outputfile = os.path.join(root, name[:-3]+'.tex'))
                # print(f'El archivo {os.path.join(root, name[:-3])} esta disponible')
            except:
                print(f'El archivo {os.path.join(root, name[:-3])} debe pasarse a mano')
#%%
for root, dirs, files in os.walk('./'):
    for name in files:
        if name[-3:] == '.md' and str(name[:-3]+'.tex') in files:
            os.remove(os.path.join(root, name))

"""Buenas. Usando el codigo que dejo abajo y un archivo de formato de latex
al que le hice algunas modificaciones estoy terminando de armar el pdf en overleaf.
Ya están todos los archivos subidos, solo quedan incluirlos y corregir a mano las
figuras y algunos overfullbox. Los vinculos internos no creo que los haga porque son
muchos y sería mucho tiempo."""