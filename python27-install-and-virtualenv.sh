
# python 2.7 =================================================================
wget --no-check-certificate https://python.org/ftp/python/2.7.6/Python-2.7.6.tgz

tar xzf Python-2.7.6.tgz
cd      Python-2.7.6

./configure --prefix=$HOME/python27

make
make install

$HOME/python27/bin/python --version

# also add this to your ~/.bash_profile 
export PATH="$HOME/python27/bin:$PATH"

cd -

# virtualenv =================================================================
wget --no-check-certificate https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz

tar xzf virtualenv-1.9.1.tar.gz
cd      virtualenv-1.9.1

python setup.py install

virtualenv --version


