#CAVE2 NeCTAR Virtual Machines

How-to for launching a CAVE2 environment in a VM for development/testing.

[TOC]

##About

###Intro
The NeCTAR research cloud has experimental GPU powered virtual machines, we have created an image to allow CAVE2 development using these.
There is currently only one available GPU powered VM slot until new hardware is installed so if someone is using it you will not be able to launch another.

###Status
The OpenSUSE 12.3 OS is installed with software that is available on the CAVE2, currently the VR systems installed are only Omegalib due to limited space on the drive.

Volume storage is not yet enabled for these experimental GPU VMs so we can't add more software or example data/apps, CalVR, Electro, SAGE etc will be added when we have the capability.

###What you need
A NeCTAR account (provided through your institution), with access to the CAVE2_Development Project

The VM user login, user (cave) password (provided on request)

A web browser, optionally: ssh & vnc client software

##Starting an Instance

###Login
Go to https://dashboard.rc.nectar.org.au/

Select Monash and log in using your authcate credentials.

###Select project
You will need to request to be added to the CAVE2 project on NeCTAR if not already done.

Once the dashboard loads you will be using your private allocation project. 

Select the **CAVE2_Development** project from the selection at the left.

###Start VM Instance

From: *Instances* list

Click [Launch Instance] (top right)

**Details Tab:**
- Flavour: *cg1-medium* (GPU, 2 CPU cores)
- Instance Boot Source: *Boot from Image*
- Image Name: *CAVE2 Development GPU*

**Access & Security Tab:**
- Keypair: not necessary, password login enabled, used for passwordless login
- Security groups: *VNC* (required for graphical login), *ssh* (recommended)

**Availability Zone Tab:**
- Click *Advanced*, Select *Monash-Test*

You can alternatively launch an instance by selecting it from *Images & Snapshots*
- Select: *CAVE2 Development GPU* Click [Launch]
- Details as above (instance/image selection will be pre-filled)

##Connecting to a running Instance

Once the instance status is "Running" you can connect to the VM.
To login to a text-only session you can connect via your web browser using the VNC client built in to the Dash or via a terminal with SSH.

You will need the account details and the IP address of the instance.

The user account is "cave" (password provided on request).

The IP address will be shown in the dashboard in the Instances list.
The current available GPU slot is at 118.138.255.33, in the future when more are available you may end up with a different IP.

###SSH login

ssh cave@118.138.255.33 

###Dashboard login

Click:
- Instances
- Name of your instance
- Console tab (wait a few seconds)
- "Click here to show only console"

Enter: username "cave", password: by request

##Starting a graphical session
You can use this console login to build software, any binaries compiled will be compatible with the CAVE2 system and can be copied to and run there.

To use a graphical desktop session, you need to start the X server then reconnect via VNC:

###Start the X server
From your console/ssh login run:

```
/scripts/graphical.sh
```

If you are using the VNC console, the display will go black as output has been switched to the NVidia GPU. You can close the console, although it will regain control if you shutdown from the graphical session.

If you are using SSH, you may  want to run

```
nohup /scripts/graphical.sh &> /dev/null&
```

Which will leave your X session running even after you disconnect.

###Connect to the Desktop via VNC

There is a web based NoVNC viewer provided on port 5800:

http://118.138.255.33:5800

(Replace IP if necessary)

Login is the same user (cave) and password as you used previously.

You can also use your favourite desktop VNC client to connect to the instance IP on the default port (5900)

##Using the system

###Installing software

The stable CAVE2 version of Omegalib is provided, when volume storage is enabled, newer versions of Omegalib will be installed.

If you require other software packages installed you will need the superuser password which can be provided on request.

###Running Omegalib Apps

There are example Omegalib app shortcuts on the Desktop

The provided Omegalib config will launch full screen with mouse/keyboard interaction, these controls are not ideal but provide a way to do basic testing.

Apps launch in low quality (high performance) rendering mode by default.

If you can't get back to the desktop from a frozen Omegalib app, you may have to kill it from a separate ssh session.
In case you forgot to add the ssh security group (to open port 22) you can modify your instance and add it while running from the dashboard.

