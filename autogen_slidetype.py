import json
import re
import os
from tqdm import tqdm
import click


def get_num_hashtags(string):
    """count the number of hashtags in beginning of string

    :param string: string to count hashtags in
    :type string: str
    :return: number of consecutive hashtags followed by a white space
    :rtype: int
    """
    num = 0
    match = re.match(r"^[#]{1,}[\s]", string)
    if match:
        num = len(match[0])-1
    return num


def set_slide_type(metadata, celltype):
    """adds slide type to global "notebook" (side-effect)

    :param cell_idx: index of the cell to consider
    :type cell_idx: int
    :param celltype: type of slideshow type to designate this cell
    :type celltype: str
    """
    if 'slideshow' not in metadata.keys():
        metadata['slideshow'] = {}
    metadata['slideshow']['slide_type'] = celltype
    return metadata


@click.command()
@click.option("--in", "-i", "basename", default="", type=click.STRING, show_default=False, required=True,
              help="input file name to be loaded, autodetects jupytext")
@click.option("--out", "-o", "outname", default="", type=click.STRING, show_default=False, required=True,
              help="output file name to be saved as, autodetects jupytext")
@click.option("--order", "slide_order", default=2, type=click.IntRange(0,), show_default=True, required=False,
              help="Number of # above which all are done as subslides")
def main(basename, outname, slide_order):
    """automatically generate slide_type metadata for ipynb files

    :param basename: input ipynb name without .ipynb
    :type basename: str
    :param outname: output ipynb name without .ipynb
    :type outname: str
    :param slide_order: numbers of #s above which sections are considered sub-slides
    :type slide_order: int > 0
    """
    # Decoding jupyter notebooks as jsons
    with open(f"{basename}.ipynb", "r", encoding="utf-8") as infile:
        notebook = json.load(infile)

    # Adjusting metadata for each cell
    for cell_idx in tqdm(range(len(notebook["cells"]))):
        if len(notebook["cells"][cell_idx]["source"]):
            num_hashtags = max(
                map(get_num_hashtags, notebook["cells"][cell_idx]["source"]))
            metadata = notebook["cells"][cell_idx]['metadata']
            if not isinstance(metadata, dict):
                print(metadata)
                metadata = {}
            if num_hashtags == 0:
                metadata = set_slide_type(metadata, "fragment")
            elif num_hashtags > slide_order:
                metadata = set_slide_type(metadata, "subslide")
            else:
                metadata = set_slide_type(metadata, "slide")
        else:
            metadata = set_slide_type(metadata, "skip")
        notebook["cells"][cell_idx]['metadata'] = metadata

    # Saving new file
    with open(f"{outname}.ipynb", "w", encoding="utf-8") as outfile:
        json.dump(notebook, fp=outfile)
    # Ensure time for jupytext is preserved
    if f"{basename}.py" in os.listdir():
        with open(f"{basename}.py", "r", encoding="utf-8") as infile:
            loaded = json.load(infile)
        with open(f"{outname}.py", "w", encoding="utf-8") as outfile:
            json.dump(loaded, fp=outfile)


if __name__ == "__main__":
    main()
