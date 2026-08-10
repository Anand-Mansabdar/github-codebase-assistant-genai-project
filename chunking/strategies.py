from langchain_text_splitters import RecursiveCharacterTextSplitter


LANGUAGE_SEPARATORS = {
  "Python": [
    "\nclass ",
    "\ndef ",
    "\n\n",
    "\n",
    " ",
    "",
  ],

    "JavaScript": [
        "\nclass ",
        "\nfunction ",
        "\nconst ",
        "\nlet ",
        "\nvar ",
        "\n\n",
        "\n",
        " ",
        "",
    ],

    "TypeScript": [
        "\nclass ",
        "\nfunction ",
        "\nconst ",
        "\nlet ",
        "\ninterface ",
        "\ntype ",
        "\n\n",
        "\n",
        " ",
        "",
    ],

    "Java": [
        "\nclass ",
        "\ninterface ",
        "\npublic ",
        "\nprivate ",
        "\nprotected ",
        "\n\n",
        "\n",
        " ",
        "",
    ],

    "Go": [
        "\ntype ",
        "\nfunc ",
        "\n\n",
        "\n",
        " ",
        "",
    ],

    "Rust": [
        "\nstruct ",
        "\nenum ",
        "\nimpl ",
        "\nfn ",
        "\n\n",
        "\n",
        " ",
        "",
    ],

    "Markdown": [
        "\n# ",
        "\n## ",
        "\n### ",
        "\n\n",
        "\n",
        " ",
        "",
    ],
}


def create_splitter(
  language: str, chunk_size: int=1200, chunk_overlap: int=200
) -> RecursiveCharacterTextSplitter:
  separators = LANGUAGE_SEPARATORS.get(language, [
    "\n\n",
    "\n",
    " ",
    "",
  ],
)
  
  return RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separators=separators, length_function=len)