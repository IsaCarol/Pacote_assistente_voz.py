from setuptools import setup, find_packages

setup(
    name='myvoiceassistant',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'speechrecognition',
    ],
    description='Um assistente de voz simples em Python.',
    author='Seu Nome',
    author_email='seuemail@exemplo.com',
    url='https://github.com/seuusuario/myvoiceassistant',  # Substitua pelo URL do seu repositório
)
