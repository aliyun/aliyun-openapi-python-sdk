#!/bin/sh -xe

OPERATION=$2
PACKAGE_VERSION=$1
PYTHON_BIN=`which python3`
if [ $PYTHON_BIN = "" ]; then
    echo "Python 3.x required."
    exit 1
fi 
PYTHON_VERSION=`python3 --version | cut -d ' ' -f 2 | cut -d . -f 1,2`

STAGING_DIR=${HOME}/python-sdk-core-distribute-staging
SOURCE_NAME=aliyun-python-sdk-core
SOURCE_DIR=`pwd`
COPY_DIR=${STAGING_DIR}/copy
UNPACK_DIR=${STAGING_DIR}/unpack
INSTALL_DIR=${STAGING_DIR}/install


if [ $OPERATION = "dist" ]; then
    echo "making package"
    rm ${STAGING_DIR} -rf
    mkdir -p ${COPY_DIR}
    cp -r ${SOURCE_NAME} ${COPY_DIR}/
    cd ${COPY_DIR}/${SOURCE_NAME}

    if [ $PACKAGE_VERSION = "core" ]; then
        rm setup3.py dist *.egg-info -rf; python3 setup.py sdist
    elif [ $PACKAGE_VERSION = "core-v3" ]; then
        rm setup.py dist *.egg-info -rf; mv setup3.py setup.py; python3 setup.py sdist
    fi

fi

if [ $OPERATION = "test" ]; then
    echo "testing package"
    rm $UNPACK_DIR -rf
    rm $INSTALL_DIR -rf
    mkdir -p $UNPACK_DIR
    mkdir -p $INSTALL_DIR
    TAR_FILE=`find ${COPY_DIR}/${SOURCE_NAME}/dist -name aliyun-python-sdk-core*.tar.gz`
    cd $UNPACK_DIR; tar xvf $TAR_FILE
    cd `find . -name aliyun-python-sdk-core*`
    SITE_PACKAGES=$INSTALL_DIR/lib/python$PYTHON_VERSION/site-packages
    mkdir $SITE_PACKAGES -p
    cp -r $SOURCE_DIR/$SOURCE_NAME/tests $SITE_PACKAGES/
    export PYTHONPATH=$SITE_PACKAGES
    python3 setup.py install --prefix=$INSTALL_DIR

    cd $SOURCE_DIR
    export PYTHONPATH=$PYTHONPATH:`ls | grep aliyun-python-sdk- | grep -v core | xargs | sed 's/ /:/g'`
    python3 -m pytest python-sdk-functional-test
fi


if [ $OPERATION = "release" ]; then
    echo "releasing package"
    cd ${COPY_DIR}/${SOURCE_NAME}
    twine upload dist/*
fi
