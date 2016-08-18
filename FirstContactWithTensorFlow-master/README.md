
## Hands-on: First Contact With TensorFlow
This hands-on tutorial provides a quick start to building applications using TensorFlow. This repository contains the information required by the TensorFlow Hands-on at [Summer Seminar ETSETB TelecomBCN, 4-8 July 2016 (http://telecomBCN.DeepLearning.Barcelona)] (http://telecomBCN.DeepLearning.Barcelona).


#### Documentation

We will use the book [First Contact with TensorFlow] (http://www.jorditorres.org/first-contact-with-tensorflow-book/) 
as a basic documentation. You can acces a [freely available on-line copy] (http://www.jorditorres.org/first-contact-with-tensorflow/>). The slides used during the hands-on will be also available before start the course.

We assume that the student has some basic knowledge about Python. If not, a Python Quick Start hands-on that will help to start with this language can be found [here (Python Quick Start)](http://www.jorditorres.org/teaching-activity/hands-on-1-python-quick-start/).


#### TensorFlow installation (do it before the course starts)
For the labs, please bring your laptop, and you should have a working installation of Python. TensorFlow has a Python API (plus a C / C ++) that requires the installation of Python 2.7. Nowadays many Linux and UNIX distributions include a recent Python.If this is not the case I assume that any student who take this course knows how to install it from the [general download page]( https://www.python.org/downloads/). 

During the sessions lab the instructor will use IPython/Jupyter. If you are interested to use too, you can obtain it from [here] (https://ipython.org) (optional).

We will use a virtual environment virtualenv to install TensorFlow (this will not overwrite existing versions of Python packages from other projects required by TensorFlow).

First, you should install pip and virtualenv if they are not already installed, like the follow script shows:
```
# Ubuntu/Linux 64-bit
$ sudo apt-get install python-pip python-dev python-virtualenv 

# Mac OS X 
$ sudo easy_install pip
$ sudo pip install --upgrade virtualenv
```
environment virtualenv in the ~/tensorflow directory:

```
$ virtualenv --system-site-packages ~/tensorflow
```

The next step is to activate the virtualenv. This can be done as follows:

```
$ source ~/tensorflow/bin/activate #  with bash 
$ source ~/tensorflow/bin/activate.csh #  with csh
(tensorflow)$
```
The name of the virtual environment in which we are working will appear at the beginning of each command line from now on. Once the virtualenv is activated, you can use pip to install TensorFlow inside it:

```
# Ubuntu/Linux 64-bit, CPU only:
(tensorflow)$ sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.7.1-cp27-none-linux_x86_64.whl 

# Mac OS X, CPU only:
(tensorflow)$ sudo easy_install --upgrade six
(tensorflow)$ sudo pip install --upgrade https://storage.googleapis.com/tensorflow/mac/tensorflow-0.7.1-cp27-none-any.whl
```

The exemples in this hands-on will require also the following packages: 

```
$ sudo pip install numpy
$ sudo pip install matplotlib
```

In order to be sure that everything is working fine, create a simple TensorFlow code and save it with extension ".py". I suggest the following code

```
import tensorflow as tf
a = tf.placeholder("float")
b = tf.placeholder("float")
y = tf.mul(a, b)
sess = tf.Session()
print sess.run(y, feed_dict={a: 3, b: 3})
```
To run the code, it will be enough with the command 

```
$ python test.py
```
If the result is 9, it means that TensorFlow is proferly installed.

Finally, when you’ve finished, you should disable the virtual environment as follows:

```
(tensorflow)$ deactivate
```

#### Day 1 - TensorFlow basics

- [multiplication.py](https://github.com/jorditorresBCN/FirstContactWithTensorFlow/blob/master/multiplicacion.py) 

#### Day 2 - TensorFlow's coding basics

- [regression.py](https://github.com/jorditorresBCN/FirstContactWithTensorFlow/blob/master/regression.py) 

#### Day 3 - TensorFlow basic data structures

- [clustering.py](https://github.com/jorditorresBCN/FirstContactWithTensorFlow/blob/master/clustering.py) 

#### Day 4 - Single Layer Neural Network

- [SingleLayerNeuralNetwork.py](https://github.com/jorditorresBCN/FirstContactWithTensorFlow/blob/master/SingleLayerNeuralNetwork.py)
- [input_data.py](https://github.com/jorditorresBCN/FirstContactWithTensorFlow/blob/master/input_data.py)

#### Day 5 - Multi-Layer Neural Networks

- [MultiLayerNeuralNetwork.py](https://github.com/jorditorresBCN/FirstContactWithTensorFlow/blob/master/MultiLayerNeuralNetworks.py)

#### Handly references

- IPython/Jupyter Notebook documentation: [http://ipython.readthedocs.io/en/stable/](http://ipython.readthedocs.io/en/stable/)
- Matplotlib Python plotting library: [http://matplotlib.org/](http://matplotlib.org/)
- Pandas Python dataframe: [http://pandas.pydata.org/](http://pandas.pydata.org/)
- Numpy Python scientific computation library: [http://numpy.org/](http://numpy.org/)

