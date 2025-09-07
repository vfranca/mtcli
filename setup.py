from setuptools import setup, find_packages

setup(
    name="mtcli",
    version="2.0.0",
    description="Aplicativo CLI para exibir gráficos do MetaTrader 5 em texto acessível ao leitor de telas",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Valmir França da Silva",
    author_email="vfranca3@gmail.com",
    url="https://github.com/vfranca/mtcli",
    license="GPL-3.0",
    python_requires=">=3.10,<3.14.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.2.0,<9.0.0",
        "python-dotenv>=1.1.0,<2.0.0",
        "metatrader5>=5.0.4993,<6.0.0",
        "numpy>=2.2.5,<3.0.0",
    ],
    extras_require={
        "build": ["pyinstaller"]
    },
    entry_points={
        "console_scripts": [
            "mt = mtcli.mt:mt",
        ],
        "mtcli.plugins": [
            "media_movel = mtcli.plugins.media_movel:mm",
            "range_medio = mtcli.plugins.range_medio:rm",
            "volume_medio = mtcli.plugins.volume_medio:vm",
        ],
    },
classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Homepage": "https://pypi.org/project/mtcli",
        "Repository": "https://github.com/vfranca/mtcli",
        "Documentation": "https://vfranca.github.io/mtcli",
        "Issues": "https://github.com/vfranca/mtcli/issues",
    },
    include_package_data=True,
    zip_safe=False,
)
