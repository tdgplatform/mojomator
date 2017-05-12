import click

@click.group()
def cli():
    pass

@click.command()
@click.option('-p', '--persona',
    help="Name of the composer persona to use",
    required=True)
@click.option('-l', '--length',
    help="Integer, number of bars in the composition",
    required=True)
@click.option('-t', '--tempo',
    help="Integer, number of beats per minute",
    required=True)
@click.option('-s', '--signature',
    help="Time Signature, expressed as a fraction, e.g. 4/4 or 6/8",
    required=True)
def compose(persona, length, tempo, signature):

    # init the persona
    pers = Persona(persona)

    # init the generator
    generator = Generator(composer=pers, length=length, tempo=tempo, signature=signature)

    # generate a document
    document = generator.compose()

    # show the document
    print json.dumps()
