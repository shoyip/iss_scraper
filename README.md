# INFN ISS COVID-19 Dashboard Scraper

Availability of granular open data in Italy for COVID-19 related informations such as **infections**, **hospitalizations**, **ICU occupancy** and **deaths** is scarce. The only other complete NUTS3 level openly available to my knowledge is the CEEDS-DEMM [COVID-Pro-Dataset](https://github.com/CEEDS-DEMM/COVID-Pro-Dataset/).

**INFN** (Istituto Nazionale di Fisica Nucleare) has gathered data from the **ISS** (Istituto Superiore di Sanità) and made aggregated analyses and visualizations on the [CovidStat INFN](https://covid19.infn.it/iss/) website.

I made a little script that scrapes the data from the website and exports them out in a `covid_iss.csv` file that can be found in the `data` folder. The data we refer to are already averaged on the basis of a seven days window, and thus are of float type.

A brief explainer notebook (`INFN ISS Dashboard Scraper.ipynb`) can be found in the main folder.

## Usage

You can install the requirements by issuing the following command.

```
pip install -r requirements.txt
```

The script `iss_scraper.py` can also be used directly from the command line. By issuing
```
python iss_scraper.py
```
you will generate the full file `covid_iss.csv`, while by issuing
```
python iss_scraper.py --prov firenze
```
you will generate the single-province dataset.

## Provinces

Available provinces are the following:

```
agrigento, alessandria, ancona, aosta, arezzo, ascoli_piceno, asti, avellino, bari, barletta_andria_trani, belluno, benevento, bergamo, biella, bologna, bolzano, brescia, brindisi, cagliari, caltanissetta, campobasso, caserta, catania, catanzaro, chieti, como, cosenza, cremona, crotone, cuneo, enna, fermo, ferrara, firenze, foggia, forli_cesena, frosinone, genova, gorizia, grosseto, imperia, isernia, laquila, la_spezia, latina, lecce, lecco, livorno, lodi, lucca, macerata, mantova, massa_carrara, matera, messina, milano, modena, monza_brianza, napoli, novara, nuoro, oristano, padova, palermo, parma, pavia, perugia, pesaro_e_urbino, pescara, piacenza, pisa, pistoia, pordenone, potenza, prato, ragusa, ravenna, reggio_di_calabria, reggio_emilia, rieti, rimini, roma, rovigo, salerno, sassari, savona, siena, siracusa, sondrio, sud_sardegna, taranto, teramo, terni, torino, trapani, trento, treviso, trieste, udine, varese, venezia, verbano_cusio_ossola, vercelli, verona, vibo_valentia, vicenza, viterbo
```