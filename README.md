# MEARI

<img src="https://user-images.githubusercontent.com/87626172/131877946-3ad59fb4-c608-45d7-b744-97f6dd0d85fd.png" width="135" align = "left">

```
๐ 2021 ๋ฐ์ดํฐ์ฒญ๋์บ ํผ์ค <๋น๋ฆฌ๋ ์์นด๋ฐ๋ฏธ> ๐

Big Leader Academy
- 2021. 06. 28 ~ 2021. 08. 30

AI๋ฅผ ํ์ฉํ ๋น๊ธ์ฌ ์ง๋ฃ๋น ์๊ฐ์ ๊ฒ ์๋น์ค๐
```


<br/>


### ๊ฐ๋ฐํ๊ฒฝ ๋ฐ ์ฌ์ฉํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
|                       ๋ผ์ด๋ธ๋ฌ๋ฆฌ                    |               ๋ชฉ์                  |      
| :------------------------------------------------: | :------------------------------: |
|                        pandas                      |        ๋ฐ์ดํฐ ๋ถ์ ๋ฐ ์ ์ฒ๋ฆฌ      |
|                       lightgbm                     |           ๋จธ์ ๋ฌ๋ ๋ชจ๋ธ          |
|                       xgboost                      |           ๋จธ์ ๋ฌ๋ ๋ชจ๋ธ          |
|                       catboost                     |           ๋จธ์ ๋ฌ๋ ๋ชจ๋ธ          |
|                       sklearn                      |     ๋จธ์ ๋ฌ๋ ๋ชจ๋ธ, ์ฑ๋ฅ์งํ ๋ฑ    | 
|                       optuna                       |       ํ์ดํผํ๋ผ๋ฏธํฐ ์ต์ ํ       |
|                       pickle                       |   ๋จธ์ ๋ฌ๋ ๋ชจ๋ธ ์ ์ฅ ๋ฐ ๋ถ๋ฌ์ค๊ธฐ  |
|                 matplotlib, seaborn                |            ๋ฐ์ดํฐ ์๊ฐํ         |
|                       Nanonets                     |              OCR API            |
|                 google cloud vision                |              OCR API            |
|                        openCV                      |              ์์์ฒ๋ฆฌ            |
|                      rhinoMorph                    |            ํํ์๋ถ์๊ธฐ          |
<br>

### ์๋น์ค workflow
![image](https://user-images.githubusercontent.com/87626172/131874143-de4d3444-1cca-4d11-9b9a-94a83ba880e0.png)


### ๊ธฐ๋ฅ ๊ฐ๋ฐ์ฌ๋ถ/๋ด๋น์

|    ๊ธฐ์      |        ๊ธฐ๋ฅ        | ๋ด๋น์ | ๊ตฌํ ์ฌ๋ถ |
| :---------: | :---------------------: | :----: | :-------: |
|  ๋ฐ์ดํฐ์ ์ฒ๋ฆฌ   |        ๋ฐ์ดํฐ์ ์          |  ์ฑํ  |     โ     |
|  OpenCV + OCR   |        ์๋ฅ์ฝ์ด์ค๊ธฐ         |  ์ฃผ์  |     โ     |
|   NLP    |         ์ฌ์ ์ ์          |  ๊ธฐํ  |     โ     |
|  Machine Learning   |        ์์ธก๋ชจ๋ธ์ ์        |  ๊ท์  |     โ     |
|      ์ดํ์ ์       |        ํ๋กํ ํ์         |  ์ฃผ์  |     โ     |

### 1. ๊ฐ๋ฐํ๊ฒฝ ๋ฐ ํจํค์ง ์ค์น ๊ด๋ จ
   
	๊ฑด๊ฐ๋ณดํ์ฌ์ฌํ๊ฐ์ ๋ด๋ถ์ ํ์๋ง PC์์ ๋ฐ์ดํฐ ์ ์ฒ๋ฆฌ์ ๋จธ์ ๋ฌ๋์ ์งํ   
	OS๋ Windows 64-bit   
	Pycharm์ผ๋ก ํ๋ก๊ทธ๋๋ฐ   
	python 3.8.8   
	ํจํค์ง๋ whlํ์ผ๋ก ์ง์  ์ค์น (packageํด๋ ์ฐธ๊ณ )   
   
   
### 2. ์ ์ฒ๋ฆฌ ๋ฐ EDA
   
	๋ฐ์ดํฐ ์ ์ฒ๋ฆฌ ๋ฐ EDA ์๊ฐํ ์ฝ๋ : code+visualization\preprocessing+EDA\preprocessing+visualization.py   
	๋ฐ์ดํฐ ์ ์ฒ๋ฆฌ ๊ณผ์ ๋ณ๋ก ์บก์ณํ ๊ฒฐ๊ณผ : code+visualization\preprocessing+EDA\preprocessing procedure capture   
	EDA์ ๋ํ ๊ฒฐ๊ณผ : code+visualization\preprocessing+EDA\EDA   
	๊ฑด๊ฐ๋ณดํ์ฌ์ฌํ๊ฐ์์์ ๋ฐ์ ์ง๋ฃ๋นํ์ธ์ ์ฒญ ๋ฐ์ดํฐ์ ๋ํ raw data์ ์ถ๊ฐ๋ก ์์ฒญํ '์์์ข๋ณ์ฝ๋-์์๊ธฐํธ' ํ์คํธ ํ์ผ์ ๋๋ฏธ๋ฅผ ๋ง๋ค์ง ๋ชปํจ   
	์ ์ฒ๋ฆฌ ์ต์ข ๊ฒฐ๊ณผ์ ๋ํ ๋๋ฏธ(์ฆ, ๋จธ์ ๋ฌ๋์ input data)๋ ์์๋ก ์ ์(realLastDF.csv)   
   
   

### 3. ๋จธ์ ๋ฌ๋
   
	code+visualization\ML์ 5๊ฐ์ ๋จธ์ ๋ฌ๋ ๊ด๋ จ python ํ์ผ๊ณผ ๋จธ์ ๋ฌ๋ ์ฝ๋์ input file์ธ realLastDF.csv๊ฐ ์กด์ฌ   
	1) xgboost, catboost, random forest, lightgbm์ ํ์ต์ํจ ํ์ผ   
	2) lightgbm ์ฑ๋ฅ ๊ณ ๋ํ ํ์ผ    
	3) ํ์ดํ๋ผ์ธ์ ํ์ํ model๊ณผ label encoder ๊ฐ์ฒด๋ฅผ ์ ์ฅํ๋ ํ์ผ   
   
	๋จธ์ ๋ฌ๋ ์คํ ๊ฒฐ๊ณผ์ ๋ํ ์๋ฃ๊ฐ code+visualization\ML_results์ ํ์คํธํ์ผ๊ณผ ์ด๋ฏธ์งํ์ผ๋ก ์กด์ฌ   
   
   
   
### 4. ํ์ดํ๋ผ์ธ ๊ด๋ จ
   
	code+visualization\pipeline   
	1) ๋ผ๋ฒจ์ธ์ฝ๋ ๊ฐ์ฒด ํ์ผ 9๊ฐ   
	2) lightgbm model save ํ์ผ 1๊ฐ   
   
      
      
### 5. run this folder ํ์ผ ์ค๋ช
   
	code+visualization\run this folder   
	run this folder ์ ์ฒด๋ฅผ ์ฃผํผํฐ๋ธํธ๋ถ์ ์ฌ๋ ค์ Meari_final_code.ipynb ์คํ   
   
	5-1 ์ต์ข ์ฝ๋ ๊ด๋ จ   
	1) Make_dictionary : ์ฌ์  ๊ตฌ์ถ ์ฝ๋ ํ์ผ   
	2) Meari_final_code : OCR, NLP, ML ์ฌ์ฉ ์ฝ๋ ํ์ผ	   
	   
	5-2 OCR ๊ด๋ จ   
	1) doclmage2.jpg : input file ( ์ง๋ฃ๋น ์ธ๋ถ๋ด์ญ์ )   
	2) hospCode.jpg ( ์ฝ๋ ๊ฒฐ๊ณผ๋ฌผ, ์ฌ์์ฑ )   
	3) patientPK.jpg ( ์ฝ๋ ๊ฒฐ๊ณผ๋ฌผ, ์ฌ์์ฑ )   
	4) croppedImage.jpg ( ์ฝ๋ ๊ฒฐ๊ณผ๋ฌผ, ์ฌ์์ฑ )   
	5) data : nanonets ์ก์ ๊ฒฐ๊ณผ ํ์ผ ( ์ฌ์์ฑ )   
	6) meari-322801-754104bbf5e4a : google API Key   
	7) patient : ํ์ ์ ๋ณด์ ๋ํ table detection ์ฝ๋ ๊ฒฐ๊ณผ๋ฌผ   
	8) diagnosis : ์ง๋ฃ ๋ฐ์ ์ฌํญ์ ๋ํ table detection ์ฝ๋ ๊ฒฐ๊ณผ๋ฌผ   
	   
	5-3 ์ฌ์  ๊ด๋ จ   
	1) stem_MethodDeleted.txt : rhino์ ๊ธฐ๋ณธ์ผ๋ก ํ์ฌ ๋ ๋ช์นญ ์ฌ์  -> ์์  / anaconda3 -> Lib -> site-packages -> rhinoMorph -> resource ํ์ผ์ stem_MethodDeleted.txt ๊ต์ฒด   
	2) insurance.txt : ๊ธ์ฌ ์ฌ์    
	3) insurance_non.txt : ๋น๊ธ์ฌ ์ฌ์    
	4) Dict_list.csv : ๊ธ์ฌ ๋ช์นญ csv ํ์ผ   
	5) Dict_list_non.csv : ๋น๊ธ์ฌ ๋ช์นญ csv ํ์ผ   
	   
	5-4 ๋จธ์ ๋ฌ๋ ๊ด๋ จ : Meari_final_code ์ฃผ์ ์ฐธ๊ณ    
       
          
             
             
             

### Jupyter Notebook ์คํ์ ์ ์ ์ฌํญ
1) run this folder๋ฅผ ๊ทธ๋๋ก ์๋ก๋ -> Meari_final_code.ipynb ์ฝ๋ ์คํ -> cell -> run all ์คํ    
   
2) pip install ~  or import ~ ์ค๋ฅ ํด๊ฒฐ ๋ฐฉ๋ฒ : package version check -> version์ ๋ง๋ package or library download   

   
### Python Version ์ฐธ์กฐ
absl-py                            0.13.0   
addict                             2.4.0   
alabaster                          0.7.12   
anaconda-client                    1.7.2   
anaconda-navigator                 2.0.3   
anaconda-project                   0.9.1   
anyio                              2.2.0   
appdirs                            1.4.4   
argh                               0.26.2   
argon2-cffi                        20.1.0   
asn1crypto                         1.4.0   
astroid                            2.5   
astropy                            4.2.1   
astunparse                         1.6.3   
async-generator                    1.10   
atomicwrites                       1.4.0   
attrs                              20.3.0   
autopep8                           1.5.6   
Babel                              2.9.0   
backcall                           0.2.0   
backports.functools-lru-cache      1.6.4   
backports.shutil-get-terminal-size 1.0.0   
backports.tempfile                 1.0   
backports.weakref                  1.0.post1   
bcrypt                             3.2.0   
beautifulsoup4                     4.9.3   
bitarray                           1.9.2   
bkcharts                           0.2   
black                              19.10b0   
bleach                             3.3.0   
bokeh                              2.3.2   
boto                               2.49.0   
Bottleneck                         1.3.2   
branca                             0.4.2   
brotlipy                           0.7.0   
cachetools                         4.2.2   
certifi                            2020.12.5   
cffi                               1.14.5   
chardet                            4.0.0   
chromedriver                       2.24.1   
chromedriver-autoinstaller         0.2.2   
click                              7.1.2   
cloudpickle                        1.6.0   
clyent                             1.2.2   
colorama                           0.4.4   
comtypes                           1.1.9   
conda                              4.10.3   
conda-build                        3.21.4   
conda-content-trust                0+unknown   
conda-package-handling             1.7.3   
conda-repo-cli                     1.0.4   
conda-token                        0.3.0   
conda-verify                       3.4.2   
contextlib2                        0.6.0.post1   
cryptography                       3.4.7   
cycler                             0.10.0   
Cython                             0.29.23   
cytoolz                            0.11.0   
dask                               2021.4.0   
decorator                          5.0.6   
defusedxml                         0.7.1   
diff-match-patch                   20200713   
distributed                        2021.4.0   
docutils                           0.17   
easyocr                            1.4   
entrypoints                        0.3   
et-xmlfile                         1.0.1   
fastcache                          1.1.0   
filelock                           3.0.12   
flake8                             3.9.0   
Flask                              1.1.2   
flatbuffers                        1.12   
folium                             0.12.1   
fsspec                             0.9.0    
future                             0.18.2    
gast                               0.4.0    
gevent                             21.1.2    
glob2                              0.7   
google-api-core                    2.0.1   
google-auth                        1.33.0   
google-auth-oauthlib               0.4.4   
google-cloud-vision                2.4.2   
google-pasta                       0.2.0   
googleapis-common-protos           1.53.0   
googlemaps                         4.4.5   
greenlet                           1.0.0   
grpcio                             1.34.1   
h5py                               3.1.0   
HeapDict                           1.0.1    
html5lib                           1.1    
idna                               2.10    
imagecodecs                        2021.3.31    
imageio                            2.9.0    
imagesize                          1.2.0    
importlib-metadata                 3.10.0    
iniconfig                          1.1.1    
intervaltree                       3.1.0   
ipykernel                          5.3.4    
ipython                            7.22.0   
ipython-genutils                   0.2.0   
ipywidgets                         7.6.3   
isort                              5.8.0   
itsdangerous                       1.1.0   
jdcal                              1.4.1   
jedi                               0.17.2    
Jinja2                             2.11.3   
joblib                             1.0.1   
JPype1                             1.3.0   
json5                              0.9.5    
jsonschema                         3.2.0   
jupyter                            1.0.0   
jupyter-client                     6.1.12   
jupyter-console                    6.4.0   
jupyter-core                       4.7.1   
jupyter-packaging                  0.7.12   
jupyter-server                     1.4.1   
jupyterlab                         3.0.14   
jupyterlab-pygments                0.1.2   
jupyterlab-server                  2.4.0   
jupyterlab-widgets                 1.0.0   
Keras                              2.4.3   
keras-nightly                      2.5.0.dev2021032900   
Keras-Preprocessing                1.1.2   
keyring                            22.3.0   
kiwisolver                         1.3.1   
lazy-object-proxy                  1.6.0   
libarchive-c                       2.9   
lightgbm                           3.2.1   
llvmlite                           0.36.0   
locket                             0.2.1   
lxml                               4.6.3   
Markdown                           3.3.4   
MarkupSafe                         1.1.1   
matplotlib                         3.3.4   
mccabe                             0.6.1   
menuinst                           1.4.16   
mistune                            0.8.4   
mkl-fft                            1.3.0   
mkl-random                         1.2.1   
mkl-service                        2.3.0   
mmcv                               0.4.3   
mock                               4.0.3   
more-itertools                     8.7.0   
mpmath                             1.2.1     
msgpack                            1.0.2     
multipledispatch                   0.6.0      
mypy-extensions                    0.4.3         
navigator-updater                  0.2.1       
nbclassic                          0.2.6        
nbclient                           0.5.3      
nbconvert                          6.0.7       
nbformat                           5.1.3        
nest-asyncio                       1.5.1       
networkx                           2.5     
nltk                               3.6.1      
nose                               1.3.7      
notebook                           6.3.0         
numba                              0.53.1   
numexpr                            2.7.3    
numpy                              1.19.5        
numpydoc                           1.1.0         
oauthlib                           3.1.1      
olefile                            0.46         
opencv-python                      4.5.2.54       
openpyxl                           3.0.7        
opt-einsum                         3.3.0         
packaging                          20.9       
pandas                             1.3.1         
pandocfilters                      1.4.3           
paramiko                           2.7.2         
parso                              0.7.0          
partd                              1.2.0      
path                               15.1.2         
pathlib2                           2.3.5         
pathspec                           0.7.0         
patsy                              0.5.1           
pdf2image                          1.16.0            
pep8                               1.7.1           
pexpect                            4.8.0       
pickleshare                        0.7.5        
Pillow                             6.2.1         
pip                                21.2.4        
pkginfo                            1.7.0          
pluggy                             0.13.1         
ply                                3.11         
prometheus-client                  0.10.1             
prompt-toolkit                     3.0.17        
proto-plus                         1.19.0          
protobuf                           3.17.3         
psutil                             5.8.0            
ptyprocess                         0.7.0       
py                                 1.10.0        
pyasn1                             0.4.8      
pyasn1-modules                     0.2.8       
pycodestyle                        2.6.0        
pycosat                            0.6.3       
pycparser                          2.20        
pycurl                             7.43.0.6         
pydocstyle                         6.0.0          
pyerfa                             1.7.3      
pyflakes                           2.2.0       
Pygments                           2.8.1       
pylint                             2.7.4         
pyls-black                         0.4.6         
pyls-spyder                        0.3.2        
PyNaCl                             1.4.0      
pyodbc                             4.0.0-unsupported        
pyOpenSSL                          20.0.1           
pyparsing                          2.4.7            
pyreadline                         2.1        
pyrsistent                         0.17.3         
PySocks                            1.7.1         
pytesseract                        0.3.8            
pytest                             6.2.3        
python-bidi                        0.4.2          
python-dateutil                    2.8.1         
python-jsonrpc-server              0.4.0         
python-language-server             0.36.2          
pytz                               2021.1          
PyWavelets                         1.1.1           
pywin32                            227            
pywin32-ctypes                     0.2.0          
pywinpty                           0.5.7             
PyYAML                             5.4.1           
pyzmq                              20.0.0          
QDarkStyle                         2.8.1          
QtAwesome                          1.0.2           
qtconsole                          5.0.3           
QtPy                               1.9.0          
regex                              2021.4.4          
requests                           2.25.1          
requests-oauthlib                  1.3.0          
rhinoMorph                         3.8.0.0         
rope                               0.18.0          
rsa                                4.7.2          
Rtree                              0.9.7          
ruamel-yaml-conda                  0.15.100          
scheduler                          0.6.1          
scikit-image                       0.18.1         
scikit-learn                       0.24.1          
scipy                              1.4.1             
seaborn                            0.11.1          
selenium                           3.141.0         
Send2Trash                         1.5.0                
setuptools                         52.0.0.post20210125            
simplegeneric                      0.8.1           
singledispatch                     0.0.0         
sip                                4.19.13         
six                                1.15.0           
sklearn                            0.0            
sniffio                            1.2.0              
snowballstemmer                    2.1.0          
sortedcollections                  2.1.0          
sortedcontainers                   2.3.0          
soupsieve                          2.2.1         
Sphinx                             4.0.1         
sphinxcontrib-applehelp            1.0.2         
sphinxcontrib-devhelp              1.0.2        
sphinxcontrib-htmlhelp             1.0.3          
sphinxcontrib-jsmath               1.0.1          
sphinxcontrib-qthelp               1.0.3           
sphinxcontrib-serializinghtml      1.1.4          
sphinxcontrib-websupport           1.2.4              
spyder                             4.2.5       
spyder-kernels                     1.10.2       
SQLAlchemy                         1.4.7          
statsmodels                        0.12.2               
sympy                              1.8           
tables                             3.6.1           
tblib                              1.7.0           
tensorboard                        2.5.0          
tensorboard-data-server            0.6.1           
tensorboard-plugin-wit             1.8.0          
tensorflow                         2.5.0         
tensorflow-estimator               2.5.0            
termcolor                          1.1.0          
terminado                          0.9.4              
terminaltables                     3.1.0           
testpath                           0.4.4           
textdistance                       4.2.1           
threadpoolctl                      2.1.0           
three-merge                        0.1.1         
tifffile                           2021.4.8          
toml                               0.10.2          
toolz                              0.11.1           
torch                              1.9.0                 
torchvision                        0.10.0        
tornado                            6.1         
tqdm                               4.59.0         
traitlets                          5.0.5          
typed-ast                          1.4.2           
typeguard                          2.12.1          
typing-extensions                  3.7.4.3          
ujson                              4.0.2         
unicodecsv                         0.14.1         
urllib3                            1.26.4        
watchdog                           1.0.2         
wcwidth                            0.2.5         
webencodings                       0.5.1           
Werkzeug                           1.0.1        
wheel                              0.36.2         
widgetsnbextension                 3.5.1         
win-inet-pton                      1.1.0         
win-unicode-console                0.5              
wincertstore                       0.2            
wrapt                              1.12.1         
xlrd                               2.0.1      
XlsxWriter                         1.3.8         
xlwings                            0.23.0         
xlwt                               1.3.0       
xmltodict                          0.12.0          
yapf                               0.31.0          
zict                               2.0.0          
zipp                               3.4.1         
zope.event                         4.5.0         
zope.interface                     5.3.0             


     
     
      
   
   
### Team_MEARI

| <IMG src="https://github.com/yooseonghyeon.png?size=100" width="150"> | <IMG src="https://github.com/JubyKim.png?size=100" width="150"> | <IMG src="https://github.com/ilovetayy.png?size=100" width="150">| <IMG src="https://github.com/Giggle1998.png?size=100" width="150">
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                            ์ ์ฑํ                            |                            ๊น์ฃผ์                            |                            ์ด๊ท์                            |                            ์ด๊ธฐํ                            |

