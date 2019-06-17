# Lookup Vendor Information of Mac Address
Given a Mac Address, lookup of Vendor/Company information of the mac address


####  How to install the Application
```
$ git clone https://github.com/tlian/MacAddrVendorLookup.git
# Install it within Python virtualenv
$ pip install virtualenv
$ virtualenv .venv
$ source .venv/bin/activate
$ cd MacAddrVendorLookup
$ pip install .
```


####  How to run the Application via CLI
*Replace API-KEY in the following command with personal API-KEY found at https://macaddress.io
*Provide correct --macaddress in the following example. For example: mac address of your personal laptop.
```
$ mac-vendor-lookup --help
$ mac-vendor-lookup --macaddress '1a:2b:3c:4d:5e:6f' --api-key <API-KEY>
```


#### How to run the Application in Docker
Note that Docker installation and basic docker familiarity is assumed in the following.
Docker installation guide maybe found at https://docs.docker.com/install/
*Build docker image and Run the image*
```
$ cd MacAddrVendorLookup
$ docker build --build-arg MAL_APIKEY=<API-KEY> --build-arg MAC_ADDRESS='<MACADDRESS>' --tag=macvendorlookup:v0.0.1 .
$ docker run macvendorlookup:v0.0.1
```
