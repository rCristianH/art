{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMGfZHiw8oCqaAl/88xY4Ob",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rCristian21/art/blob/master/EmailExport.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Q2Vw5RhlHVD_"
      },
      "outputs": [],
      "source": [
        "from ast import pattern\n",
        "import re\n",
        "\n",
        "str = \"Please contact info@sololearn.com.co ccrhdbj@outlook.com for assistance\"\n",
        "pattern = r\"[\\w\\.-]+@[\\w\\.-]+\\.[\\w\\.]+\"\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "#DOC\n",
        "\n",
        "([\\w\\.-]+): Coincide con uno o mas caracteres alfanumericos punto o barra    \n",
        "Contiene una cadena con plabras y barra y punto permitido\n",
        "\n",
        "@: Seguido de un @\n",
        "\n",
        "([\\w\\.-]+): Coincide con uno o mas caracteres alfanumericos punto o barra \n",
        "(\\.[\\w\\.]+): Un punto y otra palabra\n",
        "1. La primera parte de la direcion de correo\n",
        "2. El nombre de dominio sin el subfijo\n",
        "3. Subfijo del dominio\n",
        "\n"
      ],
      "metadata": {
        "id": "SdSqHbYjHcIf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#Varias direciones\n",
        "match = re.findall(pattern, str)\n",
        "if match:\n",
        "    for i in match:\n",
        "        print(i)\n"
      ],
      "metadata": {
        "id": "NBWB11HtHeLb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#One direcion\n",
        "\"\"\" match = re.search(pattern, str)\n",
        "if match:\n",
        "    print(match.group())\n",
        " \"\"\""
      ],
      "metadata": {
        "id": "na3QUfLvHge2"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}