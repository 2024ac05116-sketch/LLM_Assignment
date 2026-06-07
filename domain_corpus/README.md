# domain_corpus Usage

This folder must contain your domain-specific PDF documents for Part A of the notebook.

## Required files

- Place at least 5 domain-specific `.pdf` files here.
- For this assignment, the notebook expects medical domain PDFs because the current configuration uses `DOMAIN = "medical"` and `MODEL_ID = "crfm/BioMedLM"`.
- The notebook will extract text from these PDFs, clean them, de-duplicate them, and save cleaned `.txt` files back into this folder.

## Recommended content

- Medical research papers
- Clinical notes or treatment guidelines
- Disease summaries or diagnostic criteria
- Case studies and epidemiology reports
- FDA/NIH white papers or public health guidance

## How to use

1. Add your PDFs to `domain_corpus/`.
2. Open `Assignment_1B_Domain_LLM_Adaptation.ipynb`.
3. Run the Part A cells that extract and clean the PDFs.

## If you do not have real PDFs yet

Use the helper script in `scripts/generate_sample_domain_pdfs.py` to create sample medical PDFs for testing.

### Example:
```bash
cd /Users/ankitapanda/Documents/GitHub/AIMLMtech/LLMGenAi/Assignment1
pip install fpdf
python scripts/generate_sample_domain_pdfs.py
```

Then rerun the notebook Part A cells.
