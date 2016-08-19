# ENIMDA Demo

Demonstration for [ENIMDA](https://github.com/embali/enimda/) library


## Setup environment and packages

```
pyvenv-3.5 .env

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

Using included examples each resized to 300px for its minimal side and current
threshold value (0.5), detection rate for bordered images is 81.2%, false
detection rate for clear images is 6.9%

With parameter rand set to 0.05 (5%) detection becomes 10 times faster and these
rates are 77.2% and 7.9% respectively, but using rand you may get unstable result
for borders attribute - it depends on image nature and structure
