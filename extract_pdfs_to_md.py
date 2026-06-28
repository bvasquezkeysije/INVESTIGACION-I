from __future__ import annotations

from pathlib import Path
import re

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "pdfs_contenido.md"


def clean_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        if page_text.strip():
            pages.append(page_text)
    return clean_text("\n\n".join(pages))


def main() -> None:
    pdf_files = sorted(ROOT.rglob("*.pdf"), key=lambda path: str(path.relative_to(ROOT)).lower())

    sections: list[str] = ["# Contenido de PDFs"]
    for pdf_file in pdf_files:
        relative_path = pdf_file.relative_to(ROOT)
        title = pdf_file.stem.strip()
        try:
            content = extract_pdf_text(pdf_file)
        except Exception as exc:
            content = f"[No se pudo extraer el texto: {exc}]"

        if not content:
            content = "[El PDF no devolvió texto extraíble.]"

        sections.append(f"## {title}\n")
        sections.append(f"**Archivo:** `{relative_path}`\n")
        sections.append(content)
        sections.append("")

    OUTPUT.write_text("\n".join(sections), encoding="utf-8")


if __name__ == "__main__":
    main()
