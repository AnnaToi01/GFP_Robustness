# cgreGFP Robustness and Physiochemical Stability
This repository contains code for the data analysis for Bachelor's Thesis "Mutational Robustness and Physical Stability of Fluorescenct Proteins" conducted at Institute of Science and Technology in Evolutionary Genomics Laboratory under supervision of [Prof. Dr. Fyodor Kondrashov](https://ist.ac.at/en/research/kondrashov-group/) and [Louisa Gonzalez Somermeyer](https://github.com/aequorea238). The work is based on [*Gonzalez Somermeyer et al.*](https://elifesciences.org/articles/75842) (see [GitHub](https://github.com/aequorea238/Orthologous_GFP_Fitness_Peaks)).

# Table of contents
1. [Introduction](#introduction)
    * [Hypothesis](#hypothesis)
    * [Testing](#testing)
2. [Methods](#methods)
    * [Protein purification and concentration](#proteins)
    * [Urea sensitivity assays](#methods_urea)
    * [Thermosensitivity assays](#methods_thermo)
3. [Resluts and Discussion](#res_dis)
    * [Mutational robustness](#mut_rob)
    * [Urea sensitivity assays](#dis_urea)
    * [Thermosensitivity assays](#dis_thermo)
4. [Conclusion](#conclusion)
5. [Code availability](#code)
6. [Usage](#usage)
    * [Software requirements](#Software)
    * [Installation](#installation)
7. [References](#references)

# Introduction <a name="introduction"></a>

<div style="text-align: justify">
One of the main goals of biology is to describe how genotype determines the phenotype
and the evolutionary success, the fitness, of an organism [3, 4, 12]. In 1932, Sewall Wright
introduced the concept of a fitness landscape, also called adaptive landscape [12, 13]. Fitness
landscape relates the genotype to the fitness and can be visualized in a simplified way as a
3D representation, where the high-dimensional space of all possible genotypes is reduced to
a 2D plane and the fitness is plotted on the z-axis. Evolution can be interpreted as a ‘walk‘ on the fitness surface
and the adaptation as a ‘climb‘ on the hill [2, 12].
</div>


<p align="center" width="100%">
    <img src="https://github.com/AnnaToi01/GFP_Robustness/blob/main/Abs_Fluor_analysis/Intro_figures/random_fitness_landscape.png" width="60%">
</p>
<p align="center">
  <b>
  Fig. 1: 
  </b> 
  Conceptual representation of a fitness landscape. One hundred different random
hills were generated using mathematical function $c \cdot exp(−((x − a)^2 + (y + b)^2 ))$, as parameters a, b
and c were chosen randomly and the hills visualized using 
    <a href="https://github.com/AnnaToi01/GFP_Robustness/blob/main/Abs_Fluor_analysis/Intro_figures/random_fitness_landscape.ipynb">
    custom Python script
    </a>.
</p>
  
<div style="text-align: justify">

A protein fitness landscape relates the changes in the amino acid sequence to the general
function of the studied protein [5]. In this study, green fluorescent proteins (GFPs) were
investigated. GFPs make up a structurally homologous protein family with weak sequence
identities, first discovered in coelenterates in 1962 with the unique structure of a β-barrel
of eleven strands surrounding a central helix (see Fig. 2) [7, 8, 9, 10]. The helical 
segments on the barrel ends shield the chromophore from the solvent [10]. GFP has found many applications in biotechnology due to its valuable properties, such as posttranslational autocatalytic chromophore formation without requirement of substractes, its ability to serve as a fusion partner, and low sensitivity to enironmental factors [10, 11, 14]. Therefore, it is also a good model for the adaptive landscapes as its fitness can be directly quantified by measuring its fluorescence [4, 5, 11].


Four extant GFPs (avGFP (Aequorea victoria, Hydrozoa), amacGFP (Aequorea macrodactyla, Hydrozoa), cgreGFP (Clytia gregaria, Hydrozoa), and ppluGPF2 (Pontellina plumata, Copepoda)) with different sequence identities ranging from 17 % till 82 % have been explored by deep mutational scanning
and used for building a predictive neural network [4, 11].  For each protein a library of random mutants was generated and labelled with
a random combination of nucleotides (barcodes) using error-prone PCR. Each library was sorted according to the intensity of green
fluorescence and sequenced by HTS using barcodes. Finally, statistical analysis of all four fitness peaks was performed and the data was
used to train a neural network to predict functional genotypes many mutations away from the wild type sequence.


The neural network showed higher accuracy for predictions using the sharp cgreGFP fitness peak, as the deleterious effect of specific mutations as well as negative epistatic interactions were easier to detect. It has been suggested, that these observed differences in
mutational robustness could be explained by the difference in thermodynamic stability [1,
6, 11]. cgreGFP is a dimeric 27 kDa protein with an absorbance peak at 485 nm and a
fluorescence maximum at 500 nm (see Fig. 2) [7, 8]. It has been observed to be the most
kinetically unstable protein out of 4 previously mentioned GFPs, furthermore, reinforcing
the idea that the fitness peaks could also be characterized by the thermodynamic stability
of the proteins [4].
</div>




<p align="center" width="100%">
    <img src="https://github.com/AnnaToi01/GFP_Robustness/blob/main/Abs_Fluor_analysis/Pymol/cgreGFP.png" alt="cgreGFP" width="30%">
</p>
<p align="center">
  <b>
  Fig. 2: 
  </b> 
  Visualization of the β-barrel structure of 27 kDa cgreGFP generated by <a href="https://github.com/AnnaToi01/GFP_Robustness/tree/main/Abs_Fluor_analysis/Pymol">custom Python script in PyMOL</a>.
</p>


## Hypothesis <a name="hypothesis"></a>

The mutational robustness of a protein can be correlated to its physiochemical stability. 

## Testing <a name="testing"></a>
<div style="text-align: justify">

In order to test the hypothesis, 16 fluorescing cgreGFP variants were predicted at
differing distance from the wild-type (WT) cgreGFP sequence. Two different sequences were
predicted at each distance of 6 to 48 mutations with increments of 6 mutations. For each
protein, mutational stability was estimated by generating mutant libraries and sorting the
cells based on the intensity of green fluorescence. The structural stability was estimated by
urea sensitivity and thermosensitivity assays. Finally, the thermodynamic and mutational
robustness were compared to each other.
</div>

# Methods <a name="methods"></a>


16 cgreGFP variants with differing distances from the WT cgreGFP were predicted to
fluoresce by the neural network. The variants had from 6 to 48 amino acid changes (in-
cremented by 6 mutations, 2 predictions at each step) from the WT sequence. Random
mutant libraries were constructed for each variant by error-prone PCR and sorted using
fluorescence-activated cell sorting (FACS). The generated data was filtered using custom
Python scripts and provided by the host group to estimate the mutational robustness of
each variant (see [data](https://github.com/AnnaToi01/GFP_Robustness/tree/main/Abs_Fluor_analysis/Mut_robustness/data)). 

##  Protein Purification and Concentration <a name="proteins"></a>


Coding sequences for neural network-generated cgreGFP variants with N-terminal
His-tags and flanked by BsaI restriction sites were cloned into T7 expression vectors with KanR via modular cloning strategy, MoClo. DH5α *E. coli* cells were transformed with MoClo reaction mixture via heat shock and grown on LB agar supplemented with 50 µg/mL kanamycin and 20 µM IPTG. From each plate two colonies were screened for possible errors during MoClo by polymerase chain reaction (PCR) as well as sequencing. One colony was chosen for further investigation. Plasmid was extracted from liquid cultures of one selected colony and chemically competent BL21-DE3 (New England Biolabs) cells were transformed and grown on ten 12 × 12 cm LB agar 50 µg/mL kanamycin and 20 µM IPTG plates. The cells were sonicated and proteins were isolated using nickel-sepharose protein purification resin (Cytiva). The concentrations of the isolated proteins were determined using Nanopore and Bradford assay using Pierce Coomassie Protein Assay Kit (ThermoFisher) (see [Bradford assay data analysis](https://github.com/AnnaToi01/GFP_Robustness/tree/main/Abs_Fluor_analysis/Bradford_protein_concentrations)). The quality was further assessed using SDS-PAGE and Western Blotting.

## Urea sensitivity assays <a name="methods_urea"></a>

Absorbance and fluorescence spectra on Biotek SynergyH1 plate readers were measured for
16 cgreGFP variants. For absorbance, 200 µL reaction mixtures of 17.6 µM purified protein in 1 × PBS and either 0 or 9 M urea were prepared. The absorbance was then measured in 5 nm steps from 300 nm to
700 nm for approx. 60 hr at 42 ℃ in 96-well clear and flat-bottomed plates. For fluorescence,
200 µL samples contained 0.15 µM purified protein in 1 × PBS and either 0 or 9 M urea.
The samples were excited by the wavelength of 420 nm and the emission was measured in
5 nm steps from 450 nm to 700 nm for for approx. 60 hr at 42 ℃ in 96-well black-walled
and flat-bottomed plates. See [data and its analysis](https://github.com/AnnaToi01/GFP_Robustness/tree/main/Abs_Fluor_analysis/Mut_robustness).

## Thermosensitivity assays <a name="methods_thermo"></a>

The fluorescence of 16 purified cgreGFPs was measured in different urea concentrations
(from 0 to 8 M, in 1 M intervals) during heating from 20 ℃ to 99 ℃ at an increase rate of
approx. 2 ℃ /min on a Roche LightCycler 480 monitoring the SYBR-Green channel (excita-
tion at 465 nm, collection at 510 nm). For this purpose, 20 µL samples of 0.1 mg/mL purified
protein concentration in 1 × PBS were prepared in white 96-well plates and four technical
replicates were made for each measurement. The melting temperatures were determined as
the peaks of the melting curves averaged over all replicates. See [data and its analysis](https://github.com/AnnaToi01/GFP_Robustness/tree/main/Abs_Fluor_analysis/Thermostability).

# Results and discussion  <a name="res_dis"></a>

## Mutational robustness <a name="mut_rob"></a>

16 cgreGFPs along with the WT cgreGFP were sorted using FACS based on green fluo-
rescence intensity ([provided dataset](https://github.com/AnnaToi01/GFP_Robustness/tree/main/Abs_Fluor_analysis/Mut_robustness/data)). In order to visualize the mutational
robustness of the variants, the sequence divergence from the original sequence (number of
mutations) were plotted against the median measured brightness. The steepness of the descent of the curve, thus
the sharpness of the fitness peak, directly correlates with mutational robustness, as more
fragile proteins lose their functionality quicker as distance from the fitness peak increases. Using custom python script, different functions were fitted to the plot of the number of mutations against the mean brightness. Sigmoid function fitted best, so through its inverse function the number of the mutations needed to reach half of the initial measured brightness was taken as a measure for the mutational robustness of the protein. See [Jupyter notebook](https://github.com/AnnaToi01/GFP_Robustness/blob/main/Abs_Fluor_analysis/Mut_robustness/Mut_robustness.ipynb).

## Urea sensitivity assays <a name="dis_urea"></a>

Absorbance and fluorescence spectra were measured in 1 × PBS (see Fig. 6) and 9 M urea
(see Fig. 7) for 16 cgreGFP variants. 
As time progressed, neither absorbance nor fluorescence
changed in 1 × PBS. As the proteins were kept in a buffer under stable reaction conditions,
no change in the intensity of absorbance or fluorescence was expected. On the contrary, in
9 M urea absorbance as well as fluorescence of the proteins decreased as time progressed,
with fluorescence seeming to be more affected. This could be attributed to the fact, that the
fluorescence relies more on the correct folding of the protein as the chromophore has to be
properly shielded from the environment.

The peak signal intensity over time in 9 M was plotted in order to visualize the urea sensitivity of the proteins. Steeper curves indicate that the protein variant is more sensitive. Several measures have been considered to quantify the urea sensitivity of the proteins. The sigmoid function was taken again and its inverse enabled to calculate the precise time, at which the absorbance/fluorescence is halved. Pearson’s correlation coefficient was then used to calculate the relatedness between the mutational robustness and urea sensitvity of the proteins (see Table 1). 

<p>
  <b>
  Table 1:
  </b> 
  The Pearson’s correlation coefficients and corresponding p-values between different
urea sensitivity measures and the mutational robustness of 16 cgreGFP protein variants and
the WT cgreGFP. Different methods were considered to correctly estimate the urea sensitivity. The
slopes were determined for the linear part of the graphs by linear regression models. As another solution,
the first time-point was taken at which fluorescence/absorbance dropped to less than the half of its initial
value. Finally, sigmoid function was fitted to the curve and the specific time-point was predicted using the
pretrained parameters and the inverse sigmoid function. See <a href="https://github.com/AnnaToi01/GFP_Robustness/blob/main/Abs_Fluor_analysis/Urea/urea_sensitivity.ipynb">data analysis</a>.
</p>


|                            | Abs. corr. coef. | Abs p-value | Fl. corr. coef. | Fl p-value |
|:--------------------------:|:----------------:|:-----------:|:---------------:|:----------:|
|           Slopes           |       0.37       |     0.16    |       0.45      |    0.08    |
| Time at <= half the signal |       0.54       |     0.03    |       0.29      |    0.28    |
|      Sigmoid function      |       0.37       |     0.16    |       0.29      |    0.28    |

## Thermosensitivity Assays <a name="dis_thermo"></a>

The melting temperature of the proteins was taken as the peak of the derivative of the melting curve. As the urea concentration increases, melting temperatures decreases. As the urea concentration increases, melting temperatures decrease. Therefore, the destabilizing effects of heat and chaotropic agent on protein stability are cumulative. 

The correlation between mutational robustness and thermostability decreases and the p-values increase with increasing urea concentration. Therefore, the melting temperatures measured in 1 × PBS have the highest correlation with the mutational robustness. This could be explained by the possibility that the simultaneous exposure to heat and the chaotropic agent disrupts the protein stability in many different, nonlinear
ways.


# Conclusion <a name="conclusion"></a>

Some correlation between the mutational robustness and the thermodynamic
stability of the investigated cgreGFPs has been found. However, this correlation appeared
to be weak and unreliable, based on the p-values. Possibly some additional assays, such as
differential scanning fluorimetry (DSF), circular dichroism (CD), and differential scanning
calorimetry (DSC), could be run in order to better estimate the thermosensitivity of the
15 von 27 proteins [4]. Otherwise, some other denaturing agents, e.g. guanidine hydrochloride, or
assays measuring sensitivity to pH changes could also be used to quantify the thermodynamic
stability of the proteins and relate it to the measured mutational robustness.



# Code availability <a name="code"></a>

All functions used for data processing and visualization are stored in `utils.py` files. The main part of data analysis and visualization can be found in corresponding jupyter notebooks.

# Usage <a name="usage"></a>

All code was run on **Python 3.9.7** on **Ubuntu 21.04** and **Ubuntu 22.04**. 

## Software Requirements <a name="Software"></a>

* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg height=20> Python 3.9.7
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/ubuntu.svg height = 20> Ubuntu 21.04 or Ubuntu 22.04
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/gnubash.svg height=20> Bash

## Installation <a name="installation"></a>

1. You need `git` to be installed. Open terminal (`Crtl+Alt+t`) and run following commands:

```bash
git clone https://github.com/AnnaToi01/GFP_Robustness.git
cd GFP_Robustness
```

2. Create virtual environment
    * Via `virtualenv`

       * Install virtualenv if it is not installed.
         ```bash
         pip install virtualenv
         ```
       * Create virtual environment
         ```bash
         virtualenv venv --python=3.9
         ```
       * Activate it
         ```bash
         source ./venv/bin/activate
         ```
    * Via `conda`
        * Install Anaconda if not already installed (see [Instructions](https://docs.anaconda.com/anaconda/install/index.html)).
        * Create virtual environment
           ```bash
           conda create --name <env_name> python=3.9
           ```
        * Activate it
           ```bash
           conda activate <env_name>
           ```
 

2. Install necessary libraries
 ```bash
pip install -r requirements.txt
 ```
 
 After all required libraries installation you can launch jupyter notebooks and work with chosen datasets.

   


# References <a name="references"></a>

1. Shimon Bershtein et al. “Robustness-epistasis link shapes the fitness landscape of a
randomly drifting protein”. In: Nature 444.7121 (2006), pp. 929–932. issn: 1476-4687.
doi: 10.1038/nature05385.
2. Luca Ferretti et al. “Evolutionary constraints in fitness landscapes”. In: Heredity 121.5
(2018), pp. 466–481. issn: 1365-2540. doi: 10.1038/s41437-018-0110-1.
3. Inês Fragata et al. “Evolution in the light of fitness landscape theory”. In: Trends in
Ecology & Evolution 34.1 (Jan. 2019), pp. 69–82. issn: 0169-5347. doi: 10.1016/j.
tree.2018.10.009.
4. Louisa Gonzalez Somermeyer et al. “Heterogeneity of the GFP fitness landscape and
data-driven protein design”. In: eLife 11 (2022). Ed. by Daniel J Kliebenstein and
Naama Barkai, e75842. issn: 2050-084X. doi: 10.7554/eLife.75842.
5. Emily C. Hartman and Danielle Tullman-Ercek. “Learning from protein fitness land-
scapes: a review of mutability, epistasis, and evolution”. In: Current Opinion in Systems
Biology 14 (2019), pp. 25–31. issn: 2452-3100. doi: 10.1016/j.coisb.2019.02.006.
6. Ryo Kurahashi, Satoshi Sano, and Kazufumi Takano. “Protein Evolution is Potentially
Governed by Protein Stability: Directed Evolution of an Esterase from the Hyper-
thermophilic Archaeon Sulfolobus tokodaii”. In: Journal of Molecular Evolution 86.5
(2018), pp. 283–292. issn: 1432-1432. doi: 10.1007/s00239-018-9843-y.
7. Natalia P. Malikova et al. “Green-Fluorescent Protein from the Bioluminescent Jellyfish
Clytia gregaria Is an Obligate Dimer and Does Not Form a Stable Complex with the
Ca2+-Discharged Photoprotein Clytin”. In: Biochemistry 50.20 (May 2011), pp. 4232–4241. issn: 0006-2960. doi: 10.1021/bi101671p.
8. Svetlana V. Markova et al. “Green-fluorescent protein from the bioluminescent jelly-
fish Clytia gregaria: cDNA cloning, expression, and characterization of novel recombi-
nant protein”. In: Photochem. Photobiol. Sci. 9 (6 2010), pp. 757–765. doi: 10.1039/
C0PP00023J.
9. S. James Remington. “Green fluorescent protein: a perspective.” eng. In: Protein sci-
ence : a publication of the Protein Society 20 (9 2011), pp. 1509–19.
10. Karen S. Sarkisyan et al. “Local fitness landscape of the green fluorescent protein”. In:
Nature 533.7603 (2016), pp. 397–401. issn: 1476-4687. doi: 10.1038/nature17995.
11. Roger Y. Tsien. “THE GREEN FLUORESCENT PROTEIN”. In: Annu. Rev. Biochem.
67.1 (June 1998), pp. 509–544. issn: 0066-4154. doi: 10.1146/annurev.biochem.67.
1.509.
12. J. Arjan G. M. de Visser and Joachim Krug. “Empirical fitness landscapes and the
predictability of evolution”. In: Nature Reviews Genetics 15.7 (2014), pp. 480–490.
issn: 1471-0064. doi: 10.1038/nrg3744.
13. S. Wright. “The Roles of Mutation, Inbreeding, crossbreeding and Selection in Evolu-
tion”. In: Proceedings of the XI International Congress of Genetics 8 (1932), pp. 209–222.
14. Marc Zimmer. “Green Fluorescent Protein (GFP): Applications, Structure, and Re-
lated Photophysical Behavior”. In: Chem. Rev. 102.3 (Mar. 2002), pp. 759–782. issn:
0009-2665. doi: 10.1021/cr010142r.
