#!/bin/bash

set -e

WINE_VERSION="8.0.2"
WINE_TARBALL="wine-${WINE_VERSION}.tar.xz"
WINE_URL="https://dl.winehq.org/wine/source/8.x/$WINE_TARBALL"

WIN64_ONLY=false

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --win64) WIN64_ONLY=true ;;
        *) echo "Unknown option: $1" && exit 1 ;;
    esac
    shift
done

echo "[+] Downloading Wine $WINE_VERSION..."
cd ~
wget -c "$WINE_URL"
tar xf "$WINE_TARBALL"
cd "wine-${WINE_VERSION}"
mkdir -p build && cd build

if [ "$WIN64_ONLY" = true ]; then
    echo "[+] Configuring Wine for 64-bit only..."
    ../configure --enable-win64 --prefix="$HOME/.wine64"
else
    echo "[+] Installing build dependencies (requires sudo)..."
    sudo dpkg --add-architecture i386
    sudo apt update
    sudo apt install -y build-essential gcc g++ flex bison \
        gcc-multilib g++-multilib libc6-dev-i386 libx11-dev:i386 \
        libglib2.0-dev libfreetype6-dev libx11-dev libxext-dev \
        libxrender-dev libxi-dev libxcursor-dev libxrandr-dev \
        libxinerama-dev libxcomposite-dev libpng-dev libjpeg-dev \
        libxml2-dev libxslt1-dev libdbus-1-dev libgnutls28-dev \
        libgphoto2-dev libsane-dev libv4l-dev libpulse-dev \
        libopenal-dev libldap2-dev libmpg123-dev libosmesa6-dev \
        libpcap-dev

    echo "[+] Configuring Wine with 32-bit and 64-bit support..."
    ../configure --prefix="$HOME/.wine-local"
fi

echo "[+] Building Wine (this may take a while)..."
make -j$(nproc)

echo "[+] Installing Wine to your home directory..."
make install

echo "[+] Done!"

if [ "$WIN64_ONLY" = true ]; then
    echo "🔧 Add this to your ~/.bashrc or ~/.zshrc:"
    echo 'export PATH="$HOME/.wine64/bin:$PATH"'
else
    echo "🔧 Add this to your ~/.bashrc or ~/.zshrc:"
    echo 'export PATH="$HOME/.wine-local/bin:$PATH"'
fi
