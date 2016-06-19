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
threshold value (0.5), detection rate for  bordered images is 82%, false
detection rate for clear images is 7%


## Performance

With current settings one image is getting processed within 4-5 seconds for
scan mode and 5-15 seconds for detect mode on Intel® Pentium(R) CPU 2117U @
1.80GHz × 2 with 4 Gb RAM
