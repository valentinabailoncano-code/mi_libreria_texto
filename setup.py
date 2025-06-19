from setuptools import setup, find_packages

setup(
    name='mi_libreria_texto',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Valentina Bailón Cano',
    description='Una librería sencilla para limpiar y analizar texto.',
    url='https://github.com/tu_usuario/mi_libreria_texto',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
# Este archivo setup.py define la configuración para empaquetar la librería.
# Asegúrate de reemplazar 'tu_usuario' con tu nombre de usuario en GitHub o el repositorio donde alojarás la librería.
# Puedes instalar la librería localmente ejecutando:
# pip install -e .
# Esto instalará la librería en modo editable, permitiendo que los cambios se reflejen  
# inmediatamente sin necesidad de reinstalarla.
# Para publicar la librería en PyPI, necesitarás crear una cuenta en https://pypi.org/
# y seguir las instrucciones para subir tu paquete.