"""Write a PyMOL mutagenesis script for the selected protein chain.

    python make_mutants.py 2LZM_prep.pdb mutations_neutral.txt --chain A
    pymol -c mutagenesis.pml
"""

import argparse
from pathlib import Path

from QligFEP.resfep_setup import read_mutations, write_mutagenesis_script


def main(
    structure: str,
    mutation_file: str,
    chain: str = "A",
    output: str = "mutagenesis.pml",
) -> None:
    """Write one standard QresFEP mutagenesis block per listed mutation."""
    mutations = read_mutations(Path(mutation_file), chain)
    write_mutagenesis_script(Path(structure), mutations, Path(output))
    print(f"{output} written for {len(mutations)} mutation(s) on chain {chain}. Now run: pymol -c {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("structure", help="Input structure PDB")
    parser.add_argument("mutation_file", help="Mutation list file")
    parser.add_argument("--chain", default="A", help="Chain identifier (default: %(default)s)")
    parser.add_argument("--output", default="mutagenesis.pml", help="Output PyMOL script")
    args = parser.parse_args()
    main(args.structure, args.mutation_file, chain=args.chain, output=args.output)
