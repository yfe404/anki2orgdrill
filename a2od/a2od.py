#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Convert Anki style flashcards to Emacs org-drill format."""


from pathlib import Path
import click


@click.group()
def cli():
    """Convert Anki style flashcards to Emacs org-drill format."""
    pass


@cli.command('convert')
@click.argument('src', type=click.Path(exists=True))
@click.argument('dst', type=click.Path())
def convert(src, dst):
    """Convert Anki style flashcards to Emacs org-drill format.

    params:
      src: Anki Cards in plain text export.
      dst: Destination org file.
    """
    source_path = Path(src).expanduser().resolve()
    destination_path = Path(dst).expanduser().resolve()

    with open(source_path, 'r') as fd_src:
        with open(destination_path, 'w') as fd_dest:
            for line in fd_src.readlines():
                question, answer = [x.strip() for x in line.split('\t')]

                fd_dest.write("* Question :drill:")
                fd_dest.write("\n")
                fd_dest.write(question)
                fd_dest.write("\n")
                fd_dest.write("\n")
                fd_dest.write("** Answer")
                fd_dest.write("\n")
                fd_dest.write(answer)
                fd_dest.write("\n")
                fd_dest.write("\n")

    fd_src.close()
    fd_dest.close()


if __name__ == "__main__":
    cli()
