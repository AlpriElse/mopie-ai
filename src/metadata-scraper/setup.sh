# Install git
sudo yum install git-all

# Install Python 3.7
sudo yum install python37

# Install Aws CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

git clone https://github.com/AlpriElse/mopie-ai.git

cd mopie-ai/metadata-scraper

pip3 install -r requirements.txt