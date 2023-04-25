# Welcome to StackTHPred: Identifying tumor homing peptides through GBDT-based feature selection with stacking ensemble architecture
This THP prediction tool developed by a team from the Chinese University of Hong Kong (Shenzhen)

We provided our datasets (main, small and multi-class) and you can find them [Datasets](https://github.com/GGCL7/StackTHPred/tree/main/Datasets).

The present study employed five general protein descriptors as features including amino acid composition(AAC), pseudo-amino acid composition(PAAC), physicochemical properties(PHYC), BLOSUM62 and Z-scale. Their extraction codes are in [Feature extraction](https://github.com/GGCL7/StackTHPred/tree/main/Feature%20extraction).

We utilized GBDT algorithm-based feature selection and it code is in [Feature selection](https://github.com/GGCL7/StackTHPred/tree/main/Feature%20selection).

We developed three models based on three datasets, and you can find the pre-stored models at [THP_model](https://github.com/GGCL7/StackTHPred/tree/main/THP_model).
