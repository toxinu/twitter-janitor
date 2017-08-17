NAME=twitter_janitor
VERSION=0.1.0

package:
	rm -rf ./build/${VERSION}
	mkdir -p ./build/${VERSION}
	virtualenv ./build/${VERSION}
	./build/${VERSION}/bin/pip install -r requirements.txt
	cd `./build/${VERSION}/bin/python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"` \
		&& zip --exclude \*/__pycache__/\* \
			   --exclude setuptools/\* \
			   -r9 ../../../../${NAME}-${VERSION}.zip *
	zip -g ./build/${NAME}-${VERSION}.zip main.py
	cp ./build/${NAME}-${VERSION}.zip ./build/${NAME}.zip
	stat ./build/${NAME}-${VERSION}.zip
	stat ./build/${NAME}.zip