# ENIMDA Demo

Demonstration for [ENIMDA](https://github.com/embali/enimda/) library


## Setup environment and packages

```
python-3.6 -m venv .env

source .env/bin/activate

pip install -r requirements.txt
```


## Run

```
python demo.py
```


## Examples

Within the images folder in **source** folder you will find source images - with
border (bordered) and without (clear)

In the **detected** folder there are the results of source images processing - 
each image has its borders outlined for visual demonstration


## Accuracy

Using included examples each minimized to 300px and default threshold value (0.5),
detection rate for bordered images is 81.2%, false detection rate for clear images
is 6.9%

With parameter columns set to 0.05 (5%) detection becomes times faster and these
rates are 74-78% and 6-8% respectively

Please be notified that using columns or frames parameters may lead to unstable
result for border detection - it would depend on image nature and structure
