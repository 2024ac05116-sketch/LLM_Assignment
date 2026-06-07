#!/usr/bin/env python
"""
Script to convert Jupyter notebook to HTML format
"""

import nbformat
from nbconvert import HTMLExporter
import os

def convert_notebook_to_html(notebook_path, output_path=None):
    """
    Convert a Jupyter notebook to HTML format
    
    Parameters:
    notebook_path (str): Path to the input notebook file
    output_path (str): Path for the output HTML file (optional)
    """
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Remove widget metadata that might cause issues
    if 'metadata' in notebook:
        notebook['metadata'].pop('widgets', None)
    
    # Create HTML exporter
    html_exporter = HTMLExporter()
    html_exporter.template_name = 'basic'
    
    # Convert notebook to HTML
    (body, resources) = html_exporter.from_notebook_node(notebook)
    
    # Determine output path
    if output_path is None:
        base_name = os.path.splitext(notebook_path)[0]
        output_path = base_name + '.html'
    
    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(body)
    
    print(f"Successfully converted {notebook_path} to {output_path}")
    return output_path

if __name__ == "__main__":
    notebook_file = "LLMGenAI_Group_96_Assignment_1_Submission.ipynb"
    output_file = "LLMGenAI_Group_96_Assignment_1_Submission.html"
    
    if os.path.exists(notebook_file):
        convert_notebook_to_html(notebook_file, output_file)
    else:
        print(f"Notebook file {notebook_file} not found!")
