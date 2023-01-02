# Blender GPU Renders on Headless Servers
*(made easy!)*

# Steps:
1. Set up a cloud instance running **Ubuntu** with GPU drivers set up. I recommend Lambda Labs (https://cloud.lambdalabs.com) for pricing and the speed with which you can get going.



1.5. *(Skip this step if you're already set up on your server with your `.blend` file)* Get your KeyFile from your Cloud Provider. In the case of Lambda Labs this is under `ssh keys` on the left-side of the instances dashboard. Create a new key. A ".pem" file should download. Copy the IP address of your instance from the instances dashboardf or the following steps.

Apply correct permissions to the key file:
```
chmod 600 <YOUR_KEY>.pem
```
Upload your .blend file to the Ubuntu server with:
```
scp -i <YOUR_KEY>.pem <YOUR_BLENDER_FILE>.blend ubuntu@<YOUR_IP>:~/
```
Then ssh back into your server and verify it's there.
```
ssh -i <YOUR_KEY.pem> ubuntu@<YOUR_IP>
ls 
# you should see your .blend file listed
```
Remain logged into this session for the remaining steps


2. Clone this script down with 

```
git clone https://github.com/mpapili/BlenderHeadlessGPUScript.git
```
-and cd into the directory with:
```
cd BlenderHeadlessGPUScript/
```

3. Run the `setup.sh` script:
```
./setup.sh
```
*(optional)* verify the install:
```
which blender
# should return /snap/bin/blender
```

4. Render your animation by linking it to the "activate_gpus" script. Assuming your `.blend` file is in the above directory, you would run:
```
blender -b -P activate_gpu.py ./<YOUR_BLENDER_FILE>.blend -a
```

5. *(optional)* On your host machine download the rendered files:

Exit from your Lambda Cloud Instance if you haven't already
```
exit
```
Use `scp` and the same key file to download the finished frames
```
scp -i <YOUR_KEY>.pem "ubuntu@<YOUR_IP>:/tmp/*png" "$(pwd)"
```

Enjoy!
