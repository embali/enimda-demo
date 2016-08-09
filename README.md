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
threshold value (0.5), detection rate for bordered images is 81%, false
detection rate for clear images is 7%
