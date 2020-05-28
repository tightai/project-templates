# required linux install scripts (for this project)

# pytorch (cpu) and fast.ai install
apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*

python3 -m pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
python3 -m pip install fastai