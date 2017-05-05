This projects contains plots showing evolution of averaged input frequencies of \alpha asynchronous ECAs 
as \alpha changes. Plots for 88 independent ECAs are prepared and with different choice of \alpha:
<ul>
    <li>alpha=0.1,0.2,...,1.0 - plots are in the **fig** directory</li>
    <li>alpha=0.01,0.02,...,1.0 - plots are in the **fig001** directory</li>
</ul>

The project has also source data based on which plots can be generated as well as two python scripts for generating plots.
To generate plots execute
<code>
python graphs_creator.py
</code>
or
<code>
python graphs_creator001.py
</code>

Scripts use numpy and matplotlib.