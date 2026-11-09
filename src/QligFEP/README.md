# QligFEP v2.0 and QresFEP v1.0

This collection of python command line functions is designed with the
aim to facilitate a robust and fast setup of FEP calculations for the
software package **Q**. These modules use python 3, python 2 is no 
longer supported, and an old version of the code using python 2
is now only available in the python2 branch.

This package includes at the moment two main modules:  
- QligFEP.py: module to generate ligand FEP calculations using a
dual topology approach, 
see Jespers et al. (https://doi.org/10.1186/s13321-019-0348-5).  

- QresFEP.py: module to generate protein FEP calculations using a
single topology approach, 
see Jespers et al. (https://doi.org/10.1021/acs.jctc.9b00538). 

Future versions will include QLIE, dual topology QresFEP and several
translation tools for new forcefields (at the moment we support opls,
charmm,amber and openFF).

A few toplevel scripts are included in the scripts folder to facilitate
high throughput setup. Additionally, a tutorials folder is included
with a detailed description of the setup procedure as published in
Jespers et al. (QresFEP/QligFEP). This tutorial includes the generation
of ligand parameters using OPLS, how to prepare a protein system, and
how to run ligand and protein FEP calculations. These examples are 
based on ligand binding of CDk2 inhibitors.

## Whole-Chain Residue-FEP Reference

After `qprep_prot`, QresFEP can use the mutation's complete prepared chain as
the reference instead of a capped tripeptide:

```bash
qresfep -m LEU39ALA -mc A -S peptide -FF OPLSAAM -c SNELLIUS
```

Only that chain and the hybrid mutation enter the solute coordinates. Other
chains, separate cofactors and existing waters are excluded; Q adds fresh
solvent. Prepared termini are retained without new ACE/NMA caps, and `-t`
applies only to `--system tripeptide`. Intra-chain disulfides are preserved;
cysteines whose disulfide partner was excluded become free cysteines.

For mutations with different wild-type and mutant formal charges, a preliminary
Qprep build measures the physical wild-type endpoint charge, including terminal
chemistry. Sodium or chloride ions match its enclosed charge to the protein
preparation. The complete chain is retained even beyond the existing sphere,
but Q excludes outside-sphere atoms from sampling; the sphere is not enlarged.

Batch setup and analysis support explicit peptide reference selection:

```bash
setup_resFEP -i protein.pdb -m LEU39ALA -mc A -c SNELLIUS --legs protein peptide
qresfep_analyze --protein protein --reference peptide --peptide peptide
```

The batch command retains an explicit `--legs` selection with
`--manuscript-settings`. Defaults remain protein plus tripeptide. Analysis
retains the `ddG_fold` column for compatibility, but with a peptide reference it
means protein minus whole-chain peptide, not necessarily an unfolded-state
folding free energy. The `reference_leg` column records that choice.

# Installing QligFEP and QresFEP  

- Install a working version of Q, e.g.:  

    <https://github.com/esguerra/Q6>  

  
- Clone this repository:  

    git clone https://github.com/qusers/qligfep.git

- Create the shipped conda environment

    conda env create -f environment.yml

In settings.py:  

- Change SCHROD_DIR to the Schrodinger location, if you want to be
able to generate OPLS ligand parameters using ffld_server.  

- Change Q_DIR to the location of the q executables. This can be
particularly useful if you use setupFEP from a local machine on
a mounted directory. (In which case, the executables of the preparation
part and running part of Q are at several places).  

- You can add slurm specific parameters in the CLUSTER INPUTS section,
according to the given example.   

## Requirements  
- ffld_server  
- cgenff  
- Protein Preparation Wizard  
- Python3.10  
- Q  

contact: [Willem Jespers (PhD)](mailto:w.jespers@lacdr.leidenuniv.nl?subject=[QLigFEP]%20[QResFEP])

