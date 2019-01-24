#!/bin/bash

cd "$HOME"

sudo rm -r /root/.config/autorandr
sudo rm -r /root/.oh-my-zsh
sudo rm /root/.zsh_aliases
sudo rm /root/.zshrc

sudo cp -r $HOME/.config/autorandr /root/.config
sudo cp -r $HOME/.oh-my-zsh /root
sudo cp $HOME/.zsh_aliases /root
sudo cp $HOME/.zshrc /root

sudo sed -i "s/$(whoami)/root/g" /root/.zshrc
sudo sed -i 's/\/home\/root/\/root/g' /root/.zshrc
